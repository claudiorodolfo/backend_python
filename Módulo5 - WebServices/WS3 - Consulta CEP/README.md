# Cliente REST para Consulta de CEP

Projeto de cliente REST que consome o serviço ViaCEP para buscar informações de endereço via requisições HTTP.

## Arquivos

- `ws client/consulta_cep.py`: Cliente que consome o serviço REST do ViaCEP

## Instalação

### Instalar a biblioteca requests

Para instalar a biblioteca `requests` sem usar ambiente virtual (venv), você pode usar uma das seguintes opções:

#### Opção 1: Instalação global (requer permissões de administrador)

```bash
pip3 install requests
```

ou

```bash
python3 -m pip install requests
```

ou 

```bash
python3 -m pip install --user requests
```

ou 

```bash
python3 -m pip install --user --break-system-packages requests
```

#### Opção 2: Instalação apenas para o usuário atual (recomendado)

```bash
pip3 install --user requests
```

ou

```bash
python3 -m pip install --user requests
```

Esta opção instala o pacote apenas para o usuário atual, sem precisar de permissões de administrador.

## Como Usar

### Executar o Cliente

```bash
cd "ws client"
python3 consulta_cep.py
```

O cliente irá consultar o CEP do IFBA (45078900) e exibir os resultados.

## Exemplo de Uso Programático

```python
from consulta_cep import ConsultaCepCliente

# Cria uma instância do cliente
cliente = ConsultaCepCliente()

# Consulta um CEP (aceita com ou sem hífen)
resposta = cliente.consultar("01001000")
# ou
resposta = cliente.consultar("01001-000")

# Verifica se houve erro
if "erro" in resposta and resposta["erro"] is not False:
    if isinstance(resposta["erro"], bool):
        print("Erro: CEP não encontrado")
    else:
        print(f"Erro: {resposta['erro']}")
else:
    print(f"CEP: {resposta['cep']}")
    print(f"Logradouro: {resposta['logradouro']}")
    print(f"Bairro: {resposta['bairro']}")
    print(f"Cidade/UF: {resposta['localidade']} / {resposta['uf']}")
```

## API do ViaCEP

O cliente consome a API pública do ViaCEP:

**Endpoint:** `https://viacep.com.br/ws/{cep}/json/`

**Método:** GET

**Exemplo de Resposta de Sucesso (200):**
```json
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}
```

**Exemplo de Resposta de Erro (CEP não encontrado):**
```json
{
  "erro": true
}
```

## Testando com cURL

```bash
curl https://viacep.com.br/ws/01001000/json/
```

## Funcionalidades

- **Validação de CEP**: Remove automaticamente hífens e espaços antes de validar
- **Tratamento de Erros**: Verifica erros de requisição e CEPs não encontrados
- **Timeout**: Configurado para 5 segundos para evitar requisições travadas
- **Formato Flexível**: Aceita CEPs com ou sem hífen (ex: "01001-000" ou "01001000")

## Requisitos

- Python 3.6 ou superior
- Biblioteca `requests` (versão 2.32.0 ou superior)

## Notas

- O CEP deve ter exatamente 8 dígitos (hífens e espaços são removidos automaticamente)
- O serviço ViaCEP é gratuito e público, não requer autenticação
- A consulta tem timeout de 5 segundos
- O método `consultar()` retorna um dicionário com os dados do CEP ou um dicionário com a chave "erro" em caso de falha
