// Função assíncrona para validar CPF usando requisição HTTP GET
// cpf: string contendo o CPF a ser validado
// Retorna uma Promise que resolve com os dados da resposta ou null em caso de erro
async function validaCpfGet(cpf) {
    // Monta a URL com o parâmetro CPF na query string
    // encodeURIComponent: codifica o CPF para ser seguro em URLs (trata caracteres especiais)
    const url = `http://localhost:8080/validar?cpf=${encodeURIComponent(cpf)}`;
  
    // Tenta executar a requisição HTTP
    try {
      // Faz a requisição HTTP GET usando fetch API
      const resp = await fetch(url, {
        // Define o método HTTP como GET
        method: 'GET',
      });
      // Verifica se a resposta HTTP foi bem-sucedida (status 200-299)
      if (!resp.ok) {
        // Se não foi bem-sucedida, lança uma exceção com o código de status
        throw new Error(`HTTP error: ${resp.status}`);
      }
      // Converte a resposta de JSON para objeto JavaScript
      const dados = await resp.json();
      // Imprime a resposta completa no console
      console.log("[GET] Resposta:", dados);
      // Retorna os dados da resposta
      return dados;
    } catch (err) {
      // Se houver erro, imprime mensagem de erro no console
      console.error("Erro ao chamar GET:", err);
      // Retorna null indicando falha
      return null;
    }
  }
  
  // Função assíncrona para validar CPF usando requisição HTTP POST
  // cpf: string contendo o CPF a ser validado
  // Retorna uma Promise que resolve com os dados da resposta ou null em caso de erro
  async function validaCpfPost(cpf) {
    // Define a URL do endpoint (sem parâmetros na query string)
    const url = 'http://localhost:8080/validar';
  
    // Tenta executar a requisição HTTP
    try {
      // Faz a requisição HTTP POST usando fetch API
      const resp = await fetch(url, {
        // Define o método HTTP como POST
        method: 'POST',
        // Define os headers HTTP da requisição
        headers: {
          // Indica que o corpo da requisição é JSON
          'Content-Type': 'application/json'
        },
        // Converte o objeto JavaScript em string JSON e define como corpo da requisição
        body: JSON.stringify({ cpf: cpf })
      });
      // Verifica se a resposta HTTP foi bem-sucedida (status 200-299)
      if (!resp.ok) {
        // Se não foi bem-sucedida, lança uma exceção com o código de status
        throw new Error(`HTTP error: ${resp.status}`);
      }
      // Converte a resposta de JSON para objeto JavaScript
      const dados = await resp.json();
      // Imprime a resposta completa no console
      console.log("[POST] Resposta:", dados);
      // Retorna os dados da resposta
      return dados;
    } catch (err) {
      // Se houver erro, imprime mensagem de erro no console
      console.error("Erro ao chamar POST:", err);
      // Retorna null indicando falha
      return null;
    }
  }
  
  // Exemplo de uso: função assíncrona auto-executável (IIFE - Immediately Invoked Function Expression)
  (async () => {
    // Define o CPF a ser validado
    const cpf = "11144477735";
  
    // Imprime mensagem indicando que será feita validação via GET
    console.log("Validando via GET...");
    // Chama a função de validação GET e aguarda o resultado
    const resultGet = await validaCpfGet(cpf);
    // Se a resposta foi recebida com sucesso (não é null)
    if (resultGet) {
      // Imprime o CPF e o resultado da validação
      console.log("CPF:", resultGet.cpf, "| válido:", resultGet.valido);
    }
  
    // Imprime mensagem indicando que será feita validação via POST
    console.log("Validando via POST...");
    // Chama a função de validação POST e aguarda o resultado
    const resultPost = await validaCpfPost(cpf);
    // Se a resposta foi recebida com sucesso (não é null)
    if (resultPost) {
      // Imprime o CPF e o resultado da validação
      console.log("CPF:", resultPost.cpf, "| válido:", resultPost.valido);
    }
  })();
  