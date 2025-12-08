//javac -cp ".:json-20250517.jar" CPFCliente.java
//java -cp ".:json-20250517.jar" CPFCliente
import java.io.*;
import java.net.*;
import org.json.JSONObject;

public class CPFCliente {
    private String url_base;

    public CPFCliente() {
        this.url_base = "http://localhost:8080";
    }

    public void validar(String cpf) throws Exception {
        //endpoint para a operação de validar CPF
        String endpoint = this.url_base + "/validar";
        
        //dados vão na URL como parâmetros da requisição GET
        String dados = "?cpf=" + cpf;
        URL url = new URL(endpoint + dados);
        
        // Abre uma conexão HTTP com a URL especificada
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        // Cria um BufferedReader para ler a resposta do servidor
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String resposta = in.readLine();
        System.out.println("GET => " + resposta);
        
        // Converte a resposta de JSON para objeto
        JSONObject json = new JSONObject(resposta);
        System.out.println("==============================");
        System.out.println("RESULTADO VALIDAR CPF: " + json.get("valido"));
        System.out.println("==============================");
        in.close();
    }

    public static void main(String[] args) throws Exception {
        CPFCliente cliente = new CPFCliente();
        cliente.validar("11144477735");
        cliente.validar("11111111111");
    }
}
