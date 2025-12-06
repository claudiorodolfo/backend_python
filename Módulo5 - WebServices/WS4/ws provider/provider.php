<?php
// provider.php - Servidor HTTP em PHP para validação de CPF
//php -S localhost:8081 provider.php
// Comando para executar o servidor PHP embutido na porta 8081

// Função para validar CPF usando o algoritmo oficial da Receita Federal
function validaCPF($cpf) {
    // Remove todos os caracteres que não são dígitos usando regex
    $cpf = preg_replace('/\D/', '', $cpf);

    // Verifica se o CPF não tem 11 dígitos OU se todos os dígitos são iguais (regex testa repetição)
    // A regex /^(\d)\1+$/ verifica se todos os dígitos são iguais (captura o primeiro e verifica repetição)
    if (strlen($cpf) != 11 || preg_match('/^(\d)\1+$/', $cpf))
        return false;

    // Loop para calcular os dois dígitos verificadores (posições 9 e 10, índices 9 e 10)
    for ($t = 9; $t < 11; $t++) {
        // Inicializa a variável soma com zero
        $sum = 0;
        // Itera sobre os dígitos do CPF até a posição $t
        for ($i = 0; $i < $t; $i++) {
            // Soma o produto do dígito na posição $i pelo peso (($t + 1) - $i)
            $sum += $cpf[$i] * (($t + 1) - $i);
        }
        // Calcula o dígito verificador: resto da divisão por 11 multiplicado por 10, depois resto por 10
        $dig = (($sum * 10) % 11) % 10;
        // Se o dígito calculado não corresponder ao dígito na posição $t do CPF, retorna false
        if ($dig != $cpf[$t]) return false;
    }

    // Se passou por todas as validações (tamanho, dígitos diferentes, dígitos verificadores corretos), o CPF é válido
    return true;
}

// Obtém o método HTTP da requisição (GET, POST, etc.) da superglobal $_SERVER
$method = $_SERVER["REQUEST_METHOD"];
// Faz parse da URL e extrai apenas o caminho (path) da superglobal $_SERVER["REQUEST_URI"]
$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

// Verifica se o caminho da requisição é /cpf
if ($path === "/cpf") {
    // Verifica se o método é GET e se o parâmetro "cpf" existe na query string
    // isset() verifica se a variável existe e não é null
    if ($method === "GET" && isset($_GET["cpf"])) {
        // Envia resposta JSON com o CPF e o resultado da validação, depois encerra o script
        // json_encode() converte array associativo em string JSON
        echo json_encode(["cpf" => $_GET["cpf"], "valid" => validaCPF($_GET["cpf"])]);
        // exit encerra a execução do script imediatamente
        exit;
    }

    // Verifica se o método é POST
    if ($method === "POST") {
        // Lê o corpo da requisição (php://input) e faz decode do JSON para array associativo
        // file_get_contents("php://input") lê o corpo bruto da requisição
        // json_decode(..., true) converte JSON em array associativo (true = array, false = objeto)
        $data = json_decode(file_get_contents("php://input"), true);
        // Extrai o valor da chave "cpf" do array (ou string vazia se não existir) usando null coalescing
        // ?? é o operador null coalescing do PHP 7+
        $cpf = $data["cpf"] ?? "";
        // Envia resposta JSON com o CPF e o resultado da validação, depois encerra o script
        echo json_encode(["cpf" => $cpf, "valid" => validaCPF($cpf)]);
        // exit encerra a execução do script imediatamente
        exit;
    }
}

// Se a rota não for /cpf ou método não suportado, define código de status HTTP 404
// http_response_code() define o código de status HTTP da resposta
http_response_code(404);
// Envia resposta JSON de erro indicando que o endpoint não foi encontrado
echo json_encode(["error" => "endpoint not found"]);
