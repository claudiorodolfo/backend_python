// Importa classes para entrada e saída de dados
import java.io.*;
// Importa classes para comunicação em rede (URL, HttpURLConnection)
import java.net.*;

// Define a classe Client que contém o método main
public class Client {
    // Método principal do programa, ponto de entrada da aplicação
    // throws Exception: permite que exceções sejam propagadas sem tratamento
    public static void main(String[] args) throws Exception {

        // ---- GET ----
        // Cria um objeto URL com o endpoint e parâmetro CPF na query string
        URL url = new URL("http://localhost:8000/cpf?numero=11144477735");
        // Abre uma conexão HTTP com a URL especificada
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        // Define o método HTTP da requisição como GET
        con.setRequestMethod("GET");

        // Cria um BufferedReader para ler a resposta do servidor
        // InputStreamReader: converte bytes em caracteres
        // con.getInputStream(): obtém o stream de entrada da resposta
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        // Lê a primeira linha da resposta e imprime no console
        System.out.println("GET => " + in.readLine());
        // Fecha o BufferedReader, liberando recursos
        in.close();

        // ---- POST ----
        // Cria um objeto URL com o endpoint (sem parâmetros na query string)
        URL url2 = new URL("http://localhost:8000/cpf");
        // Abre uma conexão HTTP com a URL especificada
        HttpURLConnection post = (HttpURLConnection) url2.openConnection();

        // Define o método HTTP da requisição como POST
        post.setRequestMethod("POST");
        // Define o header Content-Type indicando que o corpo é JSON
        post.setRequestProperty("Content-Type", "application/json");
        // Habilita o envio de dados no corpo da requisição (necessário para POST)
        post.setDoOutput(true);

        // Define a string JSON com o CPF a ser validado
        String json = "{\"cpf\":\"11144477735\"}";
        // Try-with-resources: garante que o OutputStream seja fechado automaticamente
        try (OutputStream os = post.getOutputStream()) {
            // Converte a string JSON em bytes e escreve no corpo da requisição
            os.write(json.getBytes());
        }

        // Cria um BufferedReader para ler a resposta do servidor
        // InputStreamReader: converte bytes em caracteres
        // post.getInputStream(): obtém o stream de entrada da resposta
        BufferedReader resp = new BufferedReader(new InputStreamReader(post.getInputStream()));
        // Lê a primeira linha da resposta e imprime no console
        System.out.println("POST => " + resp.readLine());
        // Fecha o BufferedReader, liberando recursos
        resp.close();
    }
}
