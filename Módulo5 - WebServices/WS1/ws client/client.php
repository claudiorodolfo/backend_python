<?php

// ---- GET ----
echo "GET:\n";
$get_result = @file_get_contents("http://localhost:8000/cpf?numero=11144477735");
if ($get_result === false) {
    echo "Erro ao conectar com o servidor\n";
} else {
    echo $get_result . "\n";
}

// ---- POST ----
echo "\nPOST:\n";
$opts = [
    "http" => [
        "method" => "POST",
        "header" => "Content-Type: application/json\r\n",
        "content" => json_encode(["cpf" => "11144477735"])
    ]
];
$context = stream_context_create($opts);
$post_result = @file_get_contents("http://localhost:8000/cpf", false, $context);
if ($post_result === false) {
    echo "Erro ao conectar com o servidor\n";
} else {
    echo $post_result . "\n";
}

?>
