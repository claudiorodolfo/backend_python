
async function validaCpfGet(cpf) {
    const url = `http://localhost:8000/cpf?numero=${encodeURIComponent(cpf)}`;
  
    try {
      const resp = await fetch(url, {
        method: 'GET',
      });
      if (!resp.ok) {
        throw new Error(`HTTP error: ${resp.status}`);
      }
      const dados = await resp.json();
      console.log("[GET] Resposta:", dados);
      return dados;
    } catch (err) {
      console.error("Erro ao chamar GET:", err);
      return null;
    }
  }
  
  async function validaCpfPost(cpf) {
    const url = 'http://localhost:8000/cpf';
  
    try {
      const resp = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cpf: cpf })
      });
      if (!resp.ok) {
        throw new Error(`HTTP error: ${resp.status}`);
      }
      const dados = await resp.json();
      console.log("[POST] Resposta:", dados);
      return dados;
    } catch (err) {
      console.error("Erro ao chamar POST:", err);
      return null;
    }
  }
  
  // Exemplo de uso
  (async () => {
    const cpf = "11144477735";
  
    console.log("Validando via GET...");
    const resultGet = await validaCpfGet(cpf);
    if (resultGet) {
      console.log("CPF:", resultGet.cpf, "| válido:", resultGet.valido);
    }
  
    console.log("Validando via POST...");
    const resultPost = await validaCpfPost(cpf);
    if (resultPost) {
      console.log("CPF:", resultPost.cpf, "| válido:", resultPost.valido);
    }
  })();
  