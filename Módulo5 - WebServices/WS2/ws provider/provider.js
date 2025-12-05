// server.js
const http = require('http');
const url = require('url');

// Função para validar CPF (mesma lógica da sua versão PHP/Python)
function validaCPF(cpf) {
  // remove caracteres que não são dígitos
  cpf = cpf.replace(/\D/g, '');

  if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) {
    return false;
  }

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

  return cpf === cpf.slice(0,9) + dig1.toString() + dig2.toString();
}

const server = http.createServer((req, res) => {
  const parsed = url.parse(req.url, true);
  const path = parsed.pathname;
  const method = req.method;

  // permitir resposta como JSON em todos os casos
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  if (path === '/cpf') {
    if (method === 'GET') {
      const query = parsed.query;
      const cpf = query.cpf || query.numero || '';
      const valid = validaCPF(cpf);
      res.statusCode = 200;
      res.end(JSON.stringify({ cpf: cpf, valid: valid }));
      return;
    }

    if (method === 'POST') {
      let body = '';
      req.on('data', chunk => {
        body += chunk;
      });
      req.on('end', () => {
        try {
          const data = JSON.parse(body);
          const cpf = data.cpf || '';
          const valid = validaCPF(cpf);
          res.statusCode = 200;
          res.end(JSON.stringify({ cpf: cpf, valid: valid }));
        } catch (err) {
          res.statusCode = 400;
          res.end(JSON.stringify({ error: 'JSON inválido' }));
        }
      });
      return;
    }
  }

  // Se rota não for /cpf ou método não suportado
  res.statusCode = 404;
  res.end(JSON.stringify({ error: 'endpoint not found' }));
});

const PORT = 8081;
server.listen(PORT, () => {
  console.log(`Servidor JS rodando em http://localhost:${PORT}`);
});
