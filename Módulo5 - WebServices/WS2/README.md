# Cliente REST para Consulta de CEP

Projeto de cliente REST que consome o serviço ViaCEP para buscar informações de endereço via requisições HTTP.

## Arquivos

- `ws client/consulta_cep.py`: Cliente que consome o serviço REST do ViaCEP
- `ws client/requirements.txt`: Dependências do projeto

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

#### Opção 3: Instalar a partir do requirements.txt

```bash
pip3 install --user -r "ws client/requirements.txt"
```

ou

```bash
python3 -m pip install --user -r "ws client/requirements.txt"
```

## Como Usar

### Executar o Cliente

```bash
cd "ws client"
python3 consulta_cep.py
```

O cliente irá testar automaticamente diferentes CEPs e exibir os resultados.

## Exemplo de Uso Programático

```python
from consulta_cep import ConsultaCepCliente

# Cria uma instância do cliente
cliente = ConsultaCepCliente()

# Consulta um CEP
resposta, codigo = cliente.consultar("01001000")

if codigo == 200:
    print(f"CEP: {resposta['cep']}")
    print(f"Logradouro: {resposta['logradouro']}")
    print(f"Bairro: {resposta['bairro']}")
    print(f"Cidade/UF: {resposta['localidade']} / {resposta['uf']}")
else:
    print(f"Erro: {resposta.get('erro', 'Erro desconhecido')}")
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

## Requisitos

- Python 3.6 ou superior
- Biblioteca `requests` (versão 2.32.0 ou superior)

## Notas

- O CEP deve ter exatamente 8 dígitos (sem hífen)
- O serviço ViaCEP é gratuito e público, não requer autenticação
- A consulta tem timeout de 5 segundos
