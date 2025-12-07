<?php

// ---- GET ----
// Imprime cabeçalho indicando que será feita uma requisição GET
echo "GET:\n";
// Faz requisição HTTP GET usando file_get_contents
// @ suprime avisos de erro (será tratado manualmente)
// A URL inclui o parâmetro CPF na query string (?cpf=11144477735)
$get_result = @file_get_contents("http://localhost:8080/validar?cpf=11144477735");
// Verifica se a requisição falhou (retornou false)
if ($get_result === false) {
    // Imprime mensagem de erro caso não consiga conectar ao servidor
    echo "Erro ao conectar com o servidor\n";
} else {
    // Se a requisição foi bem-sucedida, imprime a resposta recebida
    echo $get_result . "\n";
}

// ---- POST ----
// Imprime uma linha em branco e cabeçalho indicando que será feita uma requisição POST
echo "\nPOST:\n";
// Define as opções para o contexto de stream HTTP
$opts = [
    // Configurações para o protocolo HTTP
    "http" => [
        // Define o método HTTP como POST
        "method" => "POST",
        // Define o header Content-Type indicando que o corpo é JSON
        // \r\n é necessário para o formato correto do header HTTP
        "header" => "Content-Type: application/json\r\n",
        // Converte o array PHP em JSON e define como conteúdo do corpo da requisição
        "content" => json_encode(["cpf" => "11144477735"])
    ]
];
// Cria um contexto de stream com as opções definidas
// O contexto será usado para configurar a requisição HTTP
$context = stream_context_create($opts);
// Faz requisição HTTP POST usando file_get_contents com o contexto criado
// @ suprime avisos de erro (será tratado manualmente)
// false indica que não deve usar include_path
// $context passa as opções HTTP (método POST, headers, body)
$post_result = @file_get_contents("http://localhost:8080/validar", false, $context);
// Verifica se a requisição falhou (retornou false)
if ($post_result === false) {
    // Imprime mensagem de erro caso não consiga conectar ao servidor
    echo "Erro ao conectar com o servidor\n";
} else {
    // Se a requisição foi bem-sucedida, imprime a resposta recebida
    echo $post_result . "\n";
}

?>
