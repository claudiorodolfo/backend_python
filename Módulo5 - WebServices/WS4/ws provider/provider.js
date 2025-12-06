// server.js - Servidor HTTP em Node.js para validação de CPF
// Importa o módulo http do Node.js para criar um servidor HTTP
const http = require('http');
// Importa o módulo url do Node.js para fazer parse de URLs
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
  // Recebe um slice do CPF (parte dos dígitos) e o peso inicial para o cálculo
  const calcDigito = (cpfSlice, pesoInicial) => {
    // Inicializa a variável soma com zero
    let soma = 0;
    // Itera sobre cada dígito do CPF (slice)
    for (let i = 0; i < cpfSlice.length; i++) {
      // Soma o produto do dígito convertido para inteiro pelo peso (pesoInicial - i)
      soma += parseInt(cpfSlice.charAt(i)) * (pesoInicial - i);
    }
    // Calcula o resto da divisão por 11 e multiplica por 10
    let resto = (soma * 10) % 11;
    // Se o resto for 10, retorna 0, caso contrário retorna o resto
    return (resto === 10 ? 0 : resto);
  };

  // Calcula o primeiro dígito verificador usando os 9 primeiros dígitos e peso 10
  const dig1 = calcDigito(cpf.slice(0, 9), 10);
  // Calcula o segundo dígito verificador usando os 10 primeiros dígitos e peso 11
  const dig2 = calcDigito(cpf.slice(0, 10), 11);

  // Compara se o CPF completo é igual aos 9 primeiros dígitos + dígito1 + dígito2
  // slice(0,9) pega os 9 primeiros dígitos, toString() converte os dígitos calculados para string
  return cpf === cpf.slice(0,9) + dig1.toString() + dig2.toString();
}

// Cria um servidor HTTP que processa requisições
// A função callback recebe req (requisição) e res (resposta) como parâmetros
const server = http.createServer((req, res) => {
  // Faz parse da URL da requisição, o segundo parâmetro true faz parse da query string
  const parsed = url.parse(req.url, true);
  // Extrai o caminho da URL (pathname) - ex: "/cpf"
  const path = parsed.pathname;
  // Extrai o método HTTP da requisição (GET, POST, etc.)
  const method = req.method;

  // permitir resposta como JSON em todos os casos
  // Define o header Content-Type como application/json com charset UTF-8
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  // Verifica se o caminho da requisição é /cpf
  if (path === '/cpf') {
    // Verifica se o método HTTP é GET
    if (method === 'GET') {
      // Extrai os parâmetros da query string
      const query = parsed.query;
      // Tenta obter o CPF do parâmetro "cpf" ou "numero", ou string vazia se não existir
      const cpf = query.cpf || query.numero || '';
      // Valida o CPF usando a função validaCPF
      const valid = validaCPF(cpf);
      // Define o código de status HTTP como 200 (OK)
      res.statusCode = 200;
      // Converte o objeto JavaScript em string JSON e envia a resposta, finalizando a conexão
      res.end(JSON.stringify({ cpf: cpf, valid: valid }));
      // Retorna para evitar processar mais código
      return;
    }

    // Verifica se o método HTTP é POST
    if (method === 'POST') {
      // Inicializa uma string vazia para acumular o corpo da requisição
      let body = '';
      // Evento disparado quando dados são recebidos (pode ser em chunks)
      // O callback recebe cada pedaço (chunk) de dados da requisição
      req.on('data', chunk => {
        // Concatena cada chunk de dados recebido ao body
        body += chunk;
      });
      // Evento disparado quando todos os dados foram recebidos
      req.on('end', () => {
        // Tenta fazer parse do JSON do corpo da requisição
        try {
          // Converte a string JSON em objeto JavaScript
          const data = JSON.parse(body);
          // Extrai o valor da propriedade "cpf" do objeto (ou string vazia se não existir)
          const cpf = data.cpf || '';
          // Valida o CPF usando a função validaCPF
          const valid = validaCPF(cpf);
          // Define o código de status HTTP como 200 (OK)
          res.statusCode = 200;
          // Envia a resposta JSON e finaliza a resposta
          res.end(JSON.stringify({ cpf: cpf, valid: valid }));
        // Se houver erro ao fazer parse do JSON
        } catch (err) {
          // Define o código de status HTTP como 400 (Bad Request)
          res.statusCode = 400;
          // Envia resposta de erro JSON e finaliza a resposta
          res.end(JSON.stringify({ error: 'JSON inválido' }));
        }
      });
      // Retorna para evitar processar mais código
      return;
    }
  }

  // Se rota não for /cpf ou método não suportado (cai aqui se não entrou em nenhum if acima)
  // Define o código de status HTTP como 404 (Not Found)
  res.statusCode = 404;
  // Envia resposta de erro JSON e finaliza a resposta
  res.end(JSON.stringify({ error: 'endpoint not found' }));
});

// Define a porta onde o servidor vai escutar
const PORT = 8081;
// Inicia o servidor na porta especificada
// O callback é executado quando o servidor estiver pronto para receber conexões
server.listen(PORT, () => {
  // Imprime mensagem no console informando que o servidor está rodando
  console.log(`Servidor JS rodando em http://localhost:${PORT}`);
});
