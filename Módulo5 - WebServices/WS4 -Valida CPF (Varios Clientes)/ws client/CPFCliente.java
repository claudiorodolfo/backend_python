import java.io.*;
import java.net.*;
import org.json.JSONObject;

public class CPFCliente {
    private String url_base;

    public CPFCliente() {
        this.url_base = "http://localhost:8080";
    }

    public static void main(String[] args) throws Exception {
        // ---- GET ----
        CPFCliente cliente = new CPFCliente();
        String enpoint = cliente.url_base + "/validar";        
        String dados = "?cpf=11144477735";
        URL url = new URL(enpoint+dados);
        // Abre uma conexão HTTP com a URL especificada
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        // Cria um BufferedReader para ler a resposta do servidor
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String resposta = in.readLine();
        System.out.println("GET => " + resposta);
        
        // Converte a resposta de JSON para objeto
        JSONObject json = new JSONObject(resposta);
        System.out.println("RESULTADO VALIDAR CPF: " + json.get("valido"));
        in.close();
    }
}
