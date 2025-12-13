#Definir os endpoint para cada operação do CRUD

#USAR este endpoint para retornar todas as pessoas do servidor
#GET http://localhost:8080/pessoas
#GET http://localhost:8080/pessoas?email=joao@gmail.com
#POST http://localhost:8080/pessoas?email=joao@gmail.com&nome=João&idade=30&altura=1.75
#PUT http://localhost:8080/pessoas?email=joao@gmail.com&nome=João&idade=30&altura=1.75
#DELETE http://localhost:8080/pessoas?email=joao@gmail.com
# ipconfig para ver ip da maquina no windows
# ifconfig para ver ip da maquina no linux

import requests

class PessoaCliente:
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.url_completa = f"{self.base_url}/pessoas"

    def buscarPorEmail(self, email: str):
        """Busca uma pessoa por email"""
        
        response = requests.get(f"{self.url_completa}?email={email}")
        if response.status_code == 404:
            return None
        dados_json = response.json()
        pessoa_data = dados_json.get('pessoa', None)
        return pessoa_data

    def listarTodas(self):
        """Lista todas as pessoas"""
        response = requests.get(self.url_completa)
        dados_json = response.json()
        pessoas = dados_json.get('pessoas', [])
        return pessoas
 
    def criar(self, email: str, nome: str = None, idade: int = None, altura: float = None):
        """Cria uma nova pessoa no servidor"""
        params = {"email": email}
        if nome:
            params["nome"] = nome
        if idade is not None:
            params["idade"] = str(idade)
        if altura is not None:
            params["altura"] = str(altura)  

        response = requests.post(self.url_completa, params=params)
        dados_json = response.json()
        pessoa_data = dados_json.get('pessoa', {})
        return pessoa_data

    def atualizar(self, email: str, nome: str = None, idade: int = None, altura: float = None):
        """Atualiza uma pessoa no servidor"""
        # Nota: Se o provider não tiver PUT implementado, pode usar POST com parâmetro adicional
        params = {"email": email}
        if nome:
            params["nome"] = nome
        if idade is not None:
            params["idade"] = str(idade)
        if altura is not None:
            params["altura"] = str(altura)

        response = requests.put(self.url_completa, params=params)
        dados_json = response.json()
        pessoa_data = dados_json.get('pessoa', None)
        return pessoa_data

    def apagar(self, email: str):
        """Apaga uma pessoa do servidor"""
        url_completa = f"{self.base_url}/pessoas"
        params = {"email": email}
        
        response = requests.delete(url_completa, params)
        if response.status_code == 404:
            return False
        response.raise_for_status()
        return True

if __name__ == "__main__":
    p = PessoaCliente()
    pessoas = p.listarTodas()
    print(f"Total de pessoas: {len(pessoas)}")
