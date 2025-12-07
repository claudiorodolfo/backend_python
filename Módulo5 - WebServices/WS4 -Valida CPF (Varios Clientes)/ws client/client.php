<?php
    class CPFCliente {
        private $url_base;
        
        public function __construct() {
            $this->url_base = "http://localhost:8080";
        }
        
        public function validar($cpf) {
            $endpoint = $this->url_base . "/validar";
            $dados = "?cpf=" . urlencode($cpf);
            
            $resultado = @file_get_contents($endpoint . $dados);
            
            // Decodifica o JSON retornado
            $dados_json = json_decode($resultado, true);
            
            // Exibe o resultado formatado
            echo str_repeat("=", 30) . "\n";
            echo "RESULTADO VALIDAR CPF: " . ($dados_json['valido'] ? 'true' : 'false') . "\n";
            echo str_repeat("=", 30) . "\n";
        }
    }
    
    // ---- GET ----
    echo "GET:\n";
    $cliente = new CPFCliente();
    $cliente->validar("11144477735");
?>
