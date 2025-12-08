const http = require('http');
const url = require('url');

// Função para validar CPF (mesma lógica da sua versão PHP/Python)
function validaCPF(cpf) {
  // remove caracteres que não são dígitos usando regex (substitui tudo que não é dígito por string vazia)
  cpf = cpf.replace(/\D/g, '');

  // Verifica se o CPF não tem 11 dígitos OU se todos os dígitos são iguais (regex testa se é repetição)
  if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) {
    return false;
  }

  // Função auxiliar para calcular um dígito verificador do CPF
  const calcDigito = (cpfSlice, pesoInicial) => {
    let soma = 0;

    for (let i = 0; i < cpfSlice.length; i++) {
      soma += parseInt(cpfSlice.charAt(i)) * (pesoInicial - i);
    }
    let resto = (soma * 10) % 11;
    return (resto === 10 ? 0 : resto);
  };

  const dig1 = calcDigito(cpf.slice(0, 9), 10);
  const dig2 = calcDigito(cpf.slice(0, 10), 11);

  // Compara se o CPF completo é igual aos 9 primeiros dígitos + dígito1 + dígito2
  return cpf === cpf.slice(0,9) + dig1.toString() + dig2.toString();
}

// Cria um servidor HTTP que processa requisições
const server = http.createServer((req, res) => {
  const parsed = url.parse(req.url, true);
  // Extrai o caminho da URL (pathname) - ex: "/cpf"
  const path = parsed.pathname;
  // Extrai o método HTTP da requisição (GET, POST, etc.)
  const method = req.method;

  // permitir resposta como JSON em todos os casos
  res.setHeader('Content-Type', 'application/json; charset=utf-8');


  if (path === '/validar') {
    if (method === 'GET') {
      const query = parsed.query;  
      const cpf = query.cpf;
      
      // Verifica se o parâmetro cpf está ausente
      if (!cpf || cpf === '') {
        res.statusCode = 400;
        res.end(JSON.stringify({ 
          error: "Parâmetro 'cpf' não fornecido"
        }));
        return;
      }
      
      const valido = validaCPF(cpf);
      // Define o código de status HTTP como 200 (OK)
      res.statusCode = 200;
      res.end(JSON.stringify({ cpf: cpf, valido: valido }));
      return;
    } else {
      // Retorna erro 405 para métodos HTTP não permitidos
      res.statusCode = 405;
      res.end(JSON.stringify({ 
        erro: 'Method Not Allowed',
        mensagem: `Método HTTP '${method}' não é permitido. Apenas o método GET é suportado para este endpoint.`,
        metodo_solicitado: method,
        metodo_permitido: 'GET'
      }));
      return;
    }
  } else {
    // Retorna erro 404 quando o endpoint não é /validar
    res.statusCode = 404;
    res.end(JSON.stringify({ 
      error: 'Endpoint não encontrado'
    }));
    return;
  }
});

const PORT = 8081;
// Inicia o servidor na porta especificada
server.listen(PORT, () => {
  console.log(`Servidor JS rodando em http://localhost:${PORT}`);
});
