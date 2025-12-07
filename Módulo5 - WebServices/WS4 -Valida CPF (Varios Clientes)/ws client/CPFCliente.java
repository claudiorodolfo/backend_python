import java.io.*;
import java.net.*;

public class CPFCliente {
    public static void main(String[] args) throws Exception {
        // ---- GET ----
        // Cria um objeto URL com o endpoint e parâmetro CPF na query string
        String parametros = "?cpf=11144477735";
        String enpoint = "http://localhost:8080/validar";
        URL url = new URL(enpoint+parametros);
        // Abre uma conexão HTTP com a URL especificada
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        // Cria um BufferedReader para ler a resposta do servidor
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        System.out.println("GET => " + in.readLine());
        in.close();
    }
}
