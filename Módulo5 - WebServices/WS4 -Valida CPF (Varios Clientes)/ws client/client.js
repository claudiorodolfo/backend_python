// Função assíncrona para validar CPF usando requisição HTTP GET
async function validaCpf(cpf) {
    const url_base = "http://localhost:8080";
    const endpoint = `${url_base}/validar`;
    const parametros = `?cpf=${encodeURIComponent(cpf)}`;
    const url = `${endpoint}${parametros}`;
  
    // Faz a requisição HTTP GET usando fetch API
    const resp = await fetch(url, {method: 'GET',});
    
    // Converte a resposta de JSON para objeto JavaScript
    const dados = await resp.json();

    console.log("[GET] Resposta:", dados);

    // Imprime o CPF e o resultado da validação
    console.log("CPF:", dados.cpf, "| válido:", dados.valido);
  }
  
  // Exemplo de uso: função assíncrona auto-executável (IIFE - Immediately Invoked Function Expression)
  (async () => {
    console.log("Validando via GET...");
    // Chama a função de validação GET
    await validaCpf("11144477735");
  })();
  