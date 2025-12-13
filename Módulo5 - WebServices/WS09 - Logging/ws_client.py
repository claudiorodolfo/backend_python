import requests
import json

class RESTCliente:
    def __init__(self, base_url="http://127.0.0.1:8082"):
        self.base_url = base_url

    def listar_tarefas(self):
        """Lista todas as tarefas"""
        print("\n" + "=" * 50)
        print("LISTANDO TODAS AS TAREFAS")
        print("=" * 50)
        
        try:
            response = requests.get(f"{self.base_url}/tarefas")
            response.raise_for_status()
            dados = response.json()
            
            print(f"Total de tarefas: {dados['total']}")
            for tarefa in dados['tarefas']:
                status = "✓" if tarefa['concluida'] else "○"
                print(f"  {status} [{tarefa['id']}] {tarefa['titulo']}")
            
            return dados
        except requests.exceptions.RequestException as e:
            print(f"Erro ao listar tarefas: {e}")
            return None

    def buscar_tarefa(self, tarefa_id):
        """Busca uma tarefa específica"""
        print(f"\n{'=' * 50}")
        print(f"BUSCANDO TAREFA ID: {tarefa_id}")
        print("=" * 50)
        
        try:
            response = requests.get(f"{self.base_url}/tarefa/{tarefa_id}")
            response.raise_for_status()
            tarefa = response.json()
            
            status = "✓ Concluída" if tarefa['concluida'] else "○ Pendente"
            print(f"ID: {tarefa['id']}")
            print(f"Título: {tarefa['titulo']}")
            print(f"Status: {status}")
            
            return tarefa
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Tarefa {tarefa_id} não encontrada")
            else:
                print(f"Erro HTTP: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar tarefa: {e}")
            return None

    def criar_tarefa(self, titulo):
        """Cria uma nova tarefa"""
        print(f"\n{'=' * 50}")
        print(f"CRIANDO TAREFA: {titulo}")
        print("=" * 50)
        
        try:
            dados = {"titulo": titulo}
            response = requests.post(
                f"{self.base_url}/tarefa",
                json=dados,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            tarefa = response.json()
            
            print(f"✓ Tarefa criada com sucesso!")
            print(f"  ID: {tarefa['id']}")
            print(f"  Título: {tarefa['titulo']}")
            
            return tarefa
        except requests.exceptions.RequestException as e:
            print(f"Erro ao criar tarefa: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    erro = e.response.json()
                    print(f"  Detalhes: {erro.get('erro', 'Erro desconhecido')}")
                except:
                    pass
            return None

    def atualizar_tarefa(self, tarefa_id, titulo=None, concluida=None):
        """Atualiza uma tarefa"""
        print(f"\n{'=' * 50}")
        print(f"ATUALIZANDO TAREFA ID: {tarefa_id}")
        print("=" * 50)
        
        try:
            dados = {}
            if titulo is not None:
                dados['titulo'] = titulo
            if concluida is not None:
                dados['concluida'] = concluida
            
            response = requests.put(
                f"{self.base_url}/tarefa/{tarefa_id}",
                json=dados,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            tarefa = response.json()
            
            print(f"✓ Tarefa atualizada com sucesso!")
            print(f"  ID: {tarefa['id']}")
            print(f"  Título: {tarefa['titulo']}")
            print(f"  Status: {'✓ Concluída' if tarefa['concluida'] else '○ Pendente'}")
            
            return tarefa
        except requests.exceptions.RequestException as e:
            print(f"Erro ao atualizar tarefa: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    erro = e.response.json()
                    print(f"  Detalhes: {erro.get('erro', 'Erro desconhecido')}")
                except:
                    pass
            return None

    def deletar_tarefa(self, tarefa_id):
        """Deleta uma tarefa"""
        print(f"\n{'=' * 50}")
        print(f"DELETANDO TAREFA ID: {tarefa_id}")
        print("=" * 50)
        
        try:
            response = requests.delete(f"{self.base_url}/tarefa/{tarefa_id}")
            response.raise_for_status()
            resultado = response.json()
            
            print(f"✓ {resultado.get('mensagem', 'Tarefa deletada com sucesso')}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Erro ao deletar tarefa: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    erro = e.response.json()
                    print(f"  Detalhes: {erro.get('erro', 'Erro desconhecido')}")
                except:
                    pass
            return False

    def verificar_status(self):
        """Verifica o status do servidor"""
        print(f"\n{'=' * 50}")
        print("VERIFICANDO STATUS DO SERVIDOR")
        print("=" * 50)
        
        try:
            response = requests.get(f"{self.base_url}/status")
            response.raise_for_status()
            status = response.json()
            
            print(f"Status: {status['status']}")
            print(f"Timestamp: {status['timestamp']}")
            print(f"Total de tarefas: {status['total_tarefas']}")
            
            return status
        except requests.exceptions.RequestException as e:
            print(f"Erro ao verificar status: {e}")
            return None

def main():
    """Demonstra o uso do cliente REST"""
    cliente = RESTCliente()
    
    print("\n" + "=" * 50)
    print("CLIENTE REST - DEMONSTRAÇÃO")
    print("=" * 50)
    
    # Verifica status do servidor
    cliente.verificar_status()
    
    # Lista tarefas iniciais
    cliente.listar_tarefas()
    
    # Cria novas tarefas
    cliente.criar_tarefa("Estudar Python")
    cliente.criar_tarefa("Fazer exercícios de REST")
    
    # Lista tarefas novamente
    cliente.listar_tarefas()
    
    # Busca uma tarefa específica
    cliente.buscar_tarefa(1)
    
    # Atualiza uma tarefa
    cliente.atualizar_tarefa(1, concluida=True)
    cliente.atualizar_tarefa(3, titulo="Estudar Python Avançado")
    
    # Lista tarefas após atualizações
    cliente.listar_tarefas()
    
    # Deleta uma tarefa
    cliente.deletar_tarefa(2)
    
    # Lista tarefas finais
    cliente.listar_tarefas()
    
    print("\n" + "=" * 50)
    print("DEMONSTRAÇÃO CONCLUÍDA")
    print("=" * 50)
    print("\nVerifique o arquivo 'server.log' para ver os logs do servidor!")

if __name__ == "__main__":
    main()

