// Importa classes do pacote com.sun.net.httpserver para criar servidor HTTP
import com.sun.net.httpserver.*;
// Importa classes de I/O do Java (InputStreamReader, BufferedReader, OutputStream, etc.)
import java.io.*;
// Importa InetSocketAddress para especificar endereço e porta do servidor
import java.net.InetSocketAddress;
// Importa Collectors para operações de stream (juntar linhas)
import java.util.stream.Collectors;

// Classe principal do provider de validação de CPF
public class Provider {

    // Método estático para validar CPF usando o algoritmo oficial da Receita Federal
    public static boolean validaCPF(String cpf) {
        // Remove todos os caracteres que não são dígitos usando regex (\\D significa não-dígito)
        cpf = cpf.replaceAll("\\D", "");
        // Verifica se o CPF não tem 11 dígitos OU se todos os caracteres são iguais (distinct().count() == 1)
        if (cpf.length() != 11 || cpf.chars().distinct().count() == 1)
            return false;

        // Loop para calcular os dois dígitos verificadores (posições 9 e 10, índices 9 e 10)
        for (int t = 9; t < 11; t++) {
            // Inicializa a variável soma com zero
            int sum = 0;
            // Itera sobre os dígitos do CPF até a posição t
            for (int i = 0; i < t; i++) {
                // Soma o produto do dígito na posição i (convertido para int) pelo peso ((t + 1) - i)
                sum += Character.getNumericValue(cpf.charAt(i)) * ((t + 1) - i);
            }
            // Calcula o dígito verificador: resto da divisão por 11 multiplicado por 10, depois resto por 10
            int dig = ((sum * 10) % 11) % 10;
            // Se o dígito calculado não corresponder ao dígito na posição t do CPF, retorna false
            if (dig != Character.getNumericValue(cpf.charAt(t)))
                return false;
        }
        // Se passou por todas as validações (tamanho, dígitos diferentes, dígitos verificadores corretos), o CPF é válido
        return true;
    }

    // Método principal que inicia o servidor HTTP
    // args: argumentos da linha de comando (não utilizados neste caso)
    // throws IOException: pode lançar exceção de I/O ao criar o servidor
    public static void main(String[] args) throws IOException {
        // Cria um servidor HTTP na porta 8082 (0 significa usar backlog padrão)
        HttpServer server = HttpServer.create(new InetSocketAddress(8082), 0);
        // Cria um contexto para a rota /cpf e associa ao handler MyHandler
        server.createContext("/cpf", new MyHandler());
        // Inicia o servidor (cria threads para processar requisições)
        server.start();
        // Imprime mensagem informando que o servidor está rodando
        System.out.println("Java CPF Provider rodando em http://localhost:8082");
    }

    // Classe interna que implementa HttpHandler para processar requisições HTTP
    static class MyHandler implements HttpHandler {
        // Método obrigatório da interface HttpHandler que processa cada requisição
        // ex: objeto HttpExchange que contém informações da requisição e permite enviar resposta
        // throws IOException: pode lançar exceção de I/O ao processar a requisição
        @Override
        public void handle(HttpExchange ex) throws IOException {
            // Obtém o método HTTP da requisição (GET, POST, etc.)
            String method = ex.getRequestMethod();
            // Inicializa a string de resposta vazia
            String response = "";

            // Verifica se o método HTTP é GET
            if (method.equals("GET")) {
                // Obtém a query string da URI da requisição
                String query = ex.getRequestURI().getQuery();
                // Verifica se a query string não é nula e contém o parâmetro "cpf="
                if (query != null && query.contains("cpf=")) {
                    // Extrai o valor do CPF da query string (substring a partir de "cpf=" + 4 caracteres)
                    String cpf = query.substring(query.indexOf("cpf=") + 4);
                    // Remove outros parâmetros se houver (se contém "&", pega apenas até o "&")
                    if (cpf.contains("&")) {
                        cpf = cpf.substring(0, cpf.indexOf("&"));
                    }
                    // Valida o CPF usando o método validaCPF
                    boolean valid = validaCPF(cpf);
                    // Monta a resposta JSON como string manualmente (concatenação de strings)
                    // valid é boolean, então será convertido para "true" ou "false" na string
                    response = "{\"cpf\":\"" + cpf + "\", \"valid\":" + valid + "}";
                } else {
                    // Se o parâmetro cpf não foi encontrado, monta resposta de erro
                    response = "{\"error\": \"parâmetro cpf não encontrado\"}";
                    // Adiciona header Content-Type como application/json
                    // getResponseHeaders() retorna um objeto Headers para manipular headers HTTP
                    ex.getResponseHeaders().add("Content-Type", "application/json");
                    // Envia resposta com status 400 (Bad Request) e tamanho da resposta em bytes
                    // sendResponseHeaders() envia os headers HTTP, incluindo status code
                    ex.sendResponseHeaders(400, response.length());
                    // Escreve os bytes da resposta no corpo da resposta
                    // getBytes() converte a string para array de bytes usando encoding padrão
                    ex.getResponseBody().write(response.getBytes());
                    // Fecha a conexão HTTP
                    ex.close();
                    // Retorna para evitar processar mais código
                    return;
                }
            } 
            // Verifica se o método HTTP é POST
            else if (method.equals("POST")) {
                // Cria um InputStreamReader para ler o corpo da requisição com encoding UTF-8
                InputStreamReader isr = new InputStreamReader(ex.getRequestBody(), "utf-8");
                // Lê todas as linhas do corpo da requisição e junta em uma única string
                String body = new BufferedReader(isr).lines().collect(Collectors.joining());
                // Tenta fazer parse do JSON do corpo da requisição
                try {
                    // Parse JSON simples: {"cpf": "11144477735"}
                    // Inicializa string vazia para o CPF
                    String cpf = "";
                    // Remove espaços em branco do início e fim do body
                    body = body.trim();
                    // Verifica se o body começa com "{" e contém a chave "cpf"
                    if (body.startsWith("{") && body.contains("\"cpf\"")) {
                        // Encontra a posição da string "cpf" no body
                        int cpfIndex = body.indexOf("\"cpf\"");
                        // Encontra a posição do ":" após "cpf" e avança 1 posição
                        int valueStart = body.indexOf(":", cpfIndex) + 1;
                        // Pula espaços e aspas
                        // Enquanto não chegou ao fim e o caractere atual é espaço ou aspas, avança
                        while (valueStart < body.length() && 
                               (body.charAt(valueStart) == ' ' || body.charAt(valueStart) == '"')) {
                            valueStart++;
                        }
                        // Inicializa o índice do fim do valor
                        int valueEnd = valueStart;
                        // Enquanto não chegou ao fim e o caractere atual não é aspas, vírgula ou chave de fechamento
                        while (valueEnd < body.length() && 
                               body.charAt(valueEnd) != '"' && 
                               body.charAt(valueEnd) != ',' && 
                               body.charAt(valueEnd) != '}') {
                            valueEnd++;
                        }
                        // Extrai o CPF como substring entre valueStart e valueEnd, removendo espaços
                        cpf = body.substring(valueStart, valueEnd).trim();
                    }
                    // Se o CPF estiver vazio após o parse, lança exceção
                    if (cpf.isEmpty()) {
                        throw new Exception("CPF não encontrado no JSON");
                    }
                    // Valida o CPF usando o método validaCPF
                    boolean valid = validaCPF(cpf);
                    // Monta a resposta JSON como string
                    response = "{\"cpf\":\"" + cpf + "\", \"valid\":" + valid + "}";
                // Se houver erro ao fazer parse do JSON
                } catch (Exception e) {
                    // Monta resposta de erro JSON
                    response = "{\"error\": \"JSON inválido\"}";
                    // Adiciona header Content-Type como application/json
                    ex.getResponseHeaders().add("Content-Type", "application/json");
                    // Envia resposta com status 400 (Bad Request) e tamanho da resposta
                    ex.sendResponseHeaders(400, response.length());
                    // Escreve os bytes da resposta no corpo da resposta
                    ex.getResponseBody().write(response.getBytes());
                    // Fecha a conexão
                    ex.close();
                    return;
                }
            } 
            // Se o método HTTP não for GET nem POST (PUT, DELETE, PATCH, etc.)
            else {
                // Monta resposta de erro indicando método não permitido
                response = "{\"error\": \"method not allowed\"}";
                // Envia resposta com status 405 (Method Not Allowed) e tamanho da resposta
                // 405 indica que o método HTTP usado não é permitido para este endpoint
                ex.sendResponseHeaders(405, response.length());
                // Escreve os bytes da resposta no corpo da resposta
                ex.getResponseBody().write(response.getBytes());
                // Fecha a conexão HTTP
                ex.close();
                // Retorna para evitar processar mais código
                return;
            }

            // Se chegou aqui, a requisição foi processada com sucesso (GET ou POST válido)
            // Adiciona header Content-Type como application/json
            ex.getResponseHeaders().add("Content-Type", "application/json");
            // Envia resposta com status 200 (OK) e tamanho da resposta em bytes
            // 200 indica que a requisição foi processada com sucesso
            ex.sendResponseHeaders(200, response.length());
            // Obtém o OutputStream para escrever a resposta
            // getResponseBody() retorna um OutputStream para escrever o corpo da resposta
            OutputStream os = ex.getResponseBody();
            // Escreve os bytes da resposta no corpo da resposta
            os.write(response.getBytes());
            // Fecha o OutputStream (também fecha a conexão HTTP)
            os.close();
        }
    }
}
