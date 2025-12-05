<?php
//php -S localhost:8081 provider.php

function validaCPF($cpf) {
    $cpf = preg_replace('/\D/', '', $cpf);

    if (strlen($cpf) != 11 || preg_match('/^(\d)\1+$/', $cpf))
        return false;

    for ($t = 9; $t < 11; $t++) {
        $sum = 0;
        for ($i = 0; $i < $t; $i++) {
            $sum += $cpf[$i] * (($t + 1) - $i);
        }
        $dig = (($sum * 10) % 11) % 10;
        if ($dig != $cpf[$t]) return false;
    }

    return true;
}

$method = $_SERVER["REQUEST_METHOD"];
$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

if ($path === "/cpf") {
    if ($method === "GET" && isset($_GET["cpf"])) {
        echo json_encode(["cpf" => $_GET["cpf"], "valid" => validaCPF($_GET["cpf"])]);
        exit;
    }

    if ($method === "POST") {
        $data = json_decode(file_get_contents("php://input"), true);
        $cpf = $data["cpf"] ?? "";
        echo json_encode(["cpf" => $cpf, "valid" => validaCPF($cpf)]);
        exit;
    }
}

http_response_code(404);
echo json_encode(["error" => "endpoint not found"]);
