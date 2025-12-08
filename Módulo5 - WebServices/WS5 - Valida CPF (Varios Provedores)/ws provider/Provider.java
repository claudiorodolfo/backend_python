//javac -cp ".:json-20250517.jar" Provider.java
//java -cp ".:json-20250517.jar" Provider
import com.sun.net.httpserver.*;
import java.io.*;
import java.net.InetSocketAddress;
import java.net.URI;
import org.json.JSONObject;

// Classe Provider para lidar com as requisições HTTP
class WSProvider implements HttpHandler {
    
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        String method = exchange.getRequestMethod();
        String path = exchange.getRequestURI().getPath();
        
        if ("GET".equals(method)) {
            handleGET(exchange, path);
        } else if ("POST".equals(method)) {
            handlePOST(exchange);
        } else {
            JSONObject errorJson = new JSONObject();
            errorJson.put("error", "method not allowed");
            sendErrorResponse(exchange, 405, errorJson.toString());
        }
    }
    
    public void handleGET(HttpExchange exchange, String path) throws IOException {
        if (path.startsWith("/validar")) {
            System.out.println("Requisição GET recebida - Validar CPF");
            
            URI uri = exchange.getRequestURI();
            String query = uri.getQuery();
            
            if (query == null || !query.contains("cpf=")) {
                JSONObject errorJson = new JSONObject();
                errorJson.put("error", "parâmetro cpf não encontrado");
                sendErrorResponse(exchange, 400, errorJson.toString());
                return;
            }
            
            // Extrai o CPF da query string
            String cpf = extractCPF(query);
            
            // Realiza a operação de validação
            CPFService valida = new CPFService();
            boolean resultado = valida.validarCpf(cpf);
            
            // Envia a resposta para o cliente usando JSONObject
            JSONObject responseJson = new JSONObject();
            responseJson.put("cpf", cpf);
            responseJson.put("valido", resultado);
            sendResponse(exchange, 200, responseJson.toString());
        } else {
            JSONObject errorJson = new JSONObject();
            errorJson.put("error", "endpoint não encontrado");
            sendErrorResponse(exchange, 404, errorJson.toString());
        }
    }
    
    public void handlePOST(HttpExchange exchange) throws IOException {
        // Este provider só aceita requisições GET
        JSONObject errorJson = new JSONObject();
        errorJson.put("error", "Método POST não permitido. Use GET /validar?cpf=...");
        String resposta = errorJson.toString();
        exchange.getResponseHeaders().add("Content-Type", "application/json");
        exchange.getResponseHeaders().add("Allow", "GET");
        exchange.sendResponseHeaders(405, resposta.length());
        OutputStream os = exchange.getResponseBody();
        os.write(resposta.getBytes());
        os.close();
    }
    
    private String extractCPF(String query) {
        int cpfIndex = query.indexOf("cpf=");
        if (cpfIndex == -1) {
            return "";
        }
        String cpf = query.substring(cpfIndex + 4);
        if (cpf.contains("&")) {
            cpf = cpf.substring(0, cpf.indexOf("&"));
        }
        return cpf;
    }
    
    private void sendResponse(HttpExchange exchange, int statusCode, String response) throws IOException {
        exchange.getResponseHeaders().add("Content-Type", "application/json");
        exchange.sendResponseHeaders(statusCode, response.length());
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }
    
    private void sendErrorResponse(HttpExchange exchange, int statusCode, String response) throws IOException {
        sendResponse(exchange, statusCode, response);
    }
}

// Serviço fornecido pelo Web Service Provider
class CPFService {
    public boolean validarCpf(String cpf) {
        // Remove todos os caracteres não numéricos do CPF, mantendo apenas dígitos
        String cpfLimpo = cpf.replace(".", "").replace("-", "");
        
        // Verifica se o CPF tem exatamente 11 dígitos após a limpeza
        if (cpfLimpo.length() != 11) {
            return false;
        }
        
        // Verifica se todos os dígitos são iguais (ex: 11111111111, 22222222222)
        char primeiroDigito = cpfLimpo.charAt(0);
        boolean todosIguais = true;
        for (int i = 1; i < cpfLimpo.length(); i++) {
            if (cpfLimpo.charAt(i) != primeiroDigito) {
                todosIguais = false;
                break;
            }
        }
        if (todosIguais) {
            return false;
        }
        
        // Calcula os dígitos verificadores
        int dig1 = calcDigito(cpfLimpo, 10);
        int dig2 = calcDigito(cpfLimpo, 11);
        
        // Compara os dois últimos dígitos do CPF com os dígitos calculados
        String ultimosDigitos = cpfLimpo.substring(9);
        String digitosCalculados = String.valueOf(dig1) + String.valueOf(dig2);
        return ultimosDigitos.equals(digitosCalculados);
    }
    
    // Define função interna para calcular um dígito verificador do CPF
    private int calcDigito(String cpf, int peso) {
        int s = 0;
        for (int i = 0; i < peso - 1; i++) {
            s += Character.getNumericValue(cpf.charAt(i)) * (peso - i);
        }
        int resto = (s * 10) % 11;
        if (resto == 10) {
            return 0;
        } else {
            return resto;
        }
    }
}

// Classe principal do provider
public class Provider {
    public static void main(String[] args) throws IOException {
        // Inicia o servidor HTTP na porta 8080
        HttpServer servidor = HttpServer.create(new InetSocketAddress("127.0.0.1", 8080), 0);
        servidor.createContext("/", new WSProvider());
        servidor.start();
        System.out.println("Servidor iniciado em http://127.0.0.1:8080");
    }
}
