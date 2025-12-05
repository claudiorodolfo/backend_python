import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws Exception {

        // ---- GET ----
        URL url = new URL("http://localhost:8000/cpf?numero=11144477735");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        System.out.println("GET => " + in.readLine());
        in.close();

        // ---- POST ----
        URL url2 = new URL("http://localhost:8000/cpf");
        HttpURLConnection post = (HttpURLConnection) url2.openConnection();

        post.setRequestMethod("POST");
        post.setRequestProperty("Content-Type", "application/json");
        post.setDoOutput(true);

        String json = "{\"cpf\":\"11144477735\"}";
        try (OutputStream os = post.getOutputStream()) {
            os.write(json.getBytes());
        }

        BufferedReader resp = new BufferedReader(new InputStreamReader(post.getInputStream()));
        System.out.println("POST => " + resp.readLine());
        resp.close();
    }
}
