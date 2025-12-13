<?php
// provider.php - Servidor HTTP em PHP para validação de CPF
// Baseado no código Python provider.py
// Comando para executar: php -S 127.0.0.1:8083 provider.php

// Classe CPFService - Serviço fornecido pelo Web Service Provider
class CPFService {
    
    // Método público para validar CPF
    public function validarCpf($cpf) {
        // Remove todos os caracteres não numéricos do CPF, mantendo apenas dígitos
        $cpf_limpo = preg_replace('/[^0-9]/', '', $cpf);
        
        // Verifica se o CPF tem exatamente 11 dígitos após a limpeza
        if (strlen($cpf_limpo) != 11) {
            return false;
        }
        
        // Verifica se todos os dígitos são iguais (ex: 11111111111, 22222222222)
        if (preg_match('/^(\d)\1+$/', $cpf_limpo)) {
            return false;
        }
        
        // Calcula os dígitos verificadores
        $dig1 = $this->calcDigito($cpf_limpo, 10);
        $dig2 = $this->calcDigito($cpf_limpo, 11);
        
        // Compara os dois últimos dígitos do CPF com os dígitos calculados
        $digitos_verificadores = substr($cpf_limpo, -2);
        return $digitos_verificadores === $dig1 . $dig2;
    }
    
    // Método privado para calcular um dígito verificador do CPF
    private function calcDigito($cpf, $peso) {
        $s = 0;
        for ($i = 0; $i < $peso - 1; $i++) {
            $s += intval($cpf[$i]) * ($peso - $i);
        }
        $resto = ($s * 10) % 11;
        if ($resto == 10) {
            return 0;
        } else {
            return $resto;
        }
    }
}

// Obtém o método HTTP da requisição
$method = $_SERVER["REQUEST_METHOD"];

// Faz parse da URL e extrai o caminho (path)
$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

// Verifica se o caminho da requisição é /validar
if (strpos($path, "/validar") === 0) {
        
    // Verifica se o método é GET
    if ($method === "GET") {
        // Verifica se o parâmetro "cpf" existe na query string
        if (isset($_GET["cpf"])) {
            echo "Requisição GET recebida - Validar CPF\n";
            
            // Realiza a operação de validação
            $valida = new CPFService();
            $resultado = $valida->validarCpf($_GET["cpf"]);
            
            // Envia a resposta para o cliente
            header('Content-type: application/json');
            http_response_code(200);
            $msg_retorno = ["cpf" => $_GET["cpf"], "valido" => $resultado];
            echo json_encode($msg_retorno, JSON_UNESCAPED_UNICODE);
            exit;
        } else {
            // Retorna erro 400 quando o parâmetro cpf não é fornecido
            header('Content-type: application/json');
            http_response_code(400);
            $msg_erro = [
                "error" => "Parâmetro 'cpf' não fornecido"
            ];
            echo json_encode($msg_erro, JSON_UNESCAPED_UNICODE);
            exit;
        }
    } else {
        header('Content-type: application/json');
        http_response_code(405);
        $msg_erro = [
            "erro" => "Method Not Allowed",
            "mensagem" => "Método HTTP '" . $method . "' não é permitido. Apenas o método GET é suportado para este endpoint.",
            "metodo_permitido" => "GET"
        ];
        echo json_encode($msg_erro, JSON_UNESCAPED_UNICODE);
        exit;
    }
} else {
    // Retorna erro 404 quando o endpoint não é /validar
    header('Content-type: application/json');
    http_response_code(404);
    $msg_erro = [
        "error" => "Endpoint não encontrado"
    ];
    echo json_encode($msg_erro, JSON_UNESCAPED_UNICODE);
    exit;
}