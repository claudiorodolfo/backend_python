import com.sun.net.httpserver.*;
import java.io.*;
import java.net.InetSocketAddress;
import java.util.stream.Collectors;

public class Provider {

    public static boolean validaCPF(String cpf) {
        cpf = cpf.replaceAll("\\D", "");
        if (cpf.length() != 11 || cpf.chars().distinct().count() == 1)
            return false;

        for (int t = 9; t < 11; t++) {
            int sum = 0;
            for (int i = 0; i < t; i++) {
                sum += Character.getNumericValue(cpf.charAt(i)) * ((t + 1) - i);
            }
            int dig = ((sum * 10) % 11) % 10;
            if (dig != Character.getNumericValue(cpf.charAt(t)))
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8082), 0);
        server.createContext("/cpf", new MyHandler());
        server.start();
        System.out.println("Java CPF Provider rodando em http://localhost:8082");
    }

    static class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange ex) throws IOException {
            String method = ex.getRequestMethod();
            String response = "";

            if (method.equals("GET")) {
                String query = ex.getRequestURI().getQuery();
                if (query != null && query.contains("cpf=")) {
                    String cpf = query.substring(query.indexOf("cpf=") + 4);
                    // Remove outros parâmetros se houver
                    if (cpf.contains("&")) {
                        cpf = cpf.substring(0, cpf.indexOf("&"));
                    }
                    boolean valid = validaCPF(cpf);
                    response = "{\"cpf\":\"" + cpf + "\", \"valid\":" + valid + "}";
                } else {
                    response = "{\"error\": \"parâmetro cpf não encontrado\"}";
                    ex.getResponseHeaders().add("Content-Type", "application/json");
                    ex.sendResponseHeaders(400, response.length());
                    ex.getResponseBody().write(response.getBytes());
                    ex.close();
                    return;
                }
            } 
            else if (method.equals("POST")) {
                InputStreamReader isr = new InputStreamReader(ex.getRequestBody(), "utf-8");
                String body = new BufferedReader(isr).lines().collect(Collectors.joining());
                try {
                    // Parse JSON simples: {"cpf": "11144477735"}
                    String cpf = "";
                    body = body.trim();
                    if (body.startsWith("{") && body.contains("\"cpf\"")) {
                        int cpfIndex = body.indexOf("\"cpf\"");
                        int valueStart = body.indexOf(":", cpfIndex) + 1;
                        // Pula espaços e aspas
                        while (valueStart < body.length() && 
                               (body.charAt(valueStart) == ' ' || body.charAt(valueStart) == '"')) {
                            valueStart++;
                        }
                        int valueEnd = valueStart;
                        while (valueEnd < body.length() && 
                               body.charAt(valueEnd) != '"' && 
                               body.charAt(valueEnd) != ',' && 
                               body.charAt(valueEnd) != '}') {
                            valueEnd++;
                        }
                        cpf = body.substring(valueStart, valueEnd).trim();
                    }
                    if (cpf.isEmpty()) {
                        throw new Exception("CPF não encontrado no JSON");
                    }
                    boolean valid = validaCPF(cpf);
                    response = "{\"cpf\":\"" + cpf + "\", \"valid\":" + valid + "}";
                } catch (Exception e) {
                    response = "{\"error\": \"JSON inválido\"}";
                    ex.getResponseHeaders().add("Content-Type", "application/json");
                    ex.sendResponseHeaders(400, response.length());
                    ex.getResponseBody().write(response.getBytes());
                    ex.close();
                    return;
                }
            } 
            else {
                response = "{\"error\": \"method not allowed\"}";
                ex.sendResponseHeaders(405, response.length());
                ex.getResponseBody().write(response.getBytes());
                ex.close();
                return;
            }

            ex.getResponseHeaders().add("Content-Type", "application/json");
            ex.sendResponseHeaders(200, response.length());
            OutputStream os = ex.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
