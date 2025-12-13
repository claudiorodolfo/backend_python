from ws_client_pessoa import PessoaCliente

def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("MENU - CRUD PESSOA")
    print("="*50)
    print("1. Criar nova pessoa")
    print("2. Buscar pessoa por email")
    print("3. Listar todas as pessoas")
    print("4. Atualizar pessoa")
    print("5. Apagar pessoa")
    print("0. Sair")
    print("="*50)

def criar_pessoa(cliente: PessoaCliente):
    """Cria uma nova pessoa"""
    print("\n--- Criar Nova Pessoa ---")
    email = input("Email: ").strip()
    
    if not email:
        print("Erro: Email é obrigatório!")
        return
    
    nome = input("Nome (opcional): ").strip() or None
    idade_str = input("Idade (opcional): ").strip()
    altura_str = input("Altura (opcional): ").strip()
    
    idade = int(idade_str) if idade_str else None
    altura = float(altura_str) if altura_str else None
    
    try:
        pessoa_criada = cliente.criar(email, nome, idade, altura)
        print(f"\n✓ Pessoa criada com sucesso!")
        exibir_pessoa(pessoa_criada)
    except Exception as e:
        print(f"Erro ao criar pessoa: {e}")

def buscar_por_email(cliente: PessoaCliente):
    """Busca uma pessoa por email"""
    print("\n--- Buscar Pessoa por Email ---")
    email = input("Email: ").strip()
    
    if not email:
        print("Erro: Email é obrigatório!")
        return
    
    try:
        pessoa = cliente.buscarPorEmail(email)
        
        if pessoa:
            print(f"\n Pessoa encontrada:")
            exibir_pessoa(pessoa)
        else:
            print(f"\n Pessoa com email '{email}' não encontrada.")
    except Exception as e:
        print(f"Erro ao buscar pessoa: {e}")

def listar_todas(cliente: PessoaCliente):
    """Lista todas as pessoas"""
    print("\n--- Listar Todas as Pessoas ---")
    try:
        pessoas = cliente.listarTodas()
        
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
        else:
            print(f"\nTotal de pessoas: {len(pessoas)}")
            print("-" * 50)
            for i, pessoa in enumerate(pessoas, 1):
                print(f"\n[{i}]")
                exibir_pessoa(pessoa)
                print("-" * 50)
    except Exception as e:
        print(f"Erro ao listar pessoas: {e}")

def atualizar_pessoa(cliente: PessoaCliente):
    """Atualiza uma pessoa"""
    print("\n--- Atualizar Pessoa ---")
    email = input("Email da pessoa a atualizar: ").strip()
    
    if not email:
        print("Erro: Email é obrigatório!")
        return
    
    # Verifica se a pessoa existe
    try:
        pessoa_existente = cliente.buscarPorEmail(email)
        
        if not pessoa_existente:
            print(f"Erro: Pessoa com email '{email}' não encontrada.")
            return
        
        print(f"\nPessoa atual:")
        exibir_pessoa(pessoa_existente)
        print("\nInforme os novos dados (deixe em branco para manter o valor atual):")
        
        nome = input(f"Nome [{pessoa_existente.get('nome') or ''}]: ").strip()
        nome = nome if nome else pessoa_existente.get('nome')
        
        idade_str = input(f"Idade [{pessoa_existente.get('idade') or ''}]: ").strip()
        idade = int(idade_str) if idade_str else pessoa_existente.get('idade')
        
        altura_str = input(f"Altura [{pessoa_existente.get('altura') or ''}]: ").strip()
        altura = float(altura_str) if altura_str else pessoa_existente.get('altura')
        
        resultado = cliente.atualizar(email=email, nome=nome, idade=idade, altura=altura)
        
        if resultado:
            print(f"\n✓ Pessoa atualizada com sucesso!")
            exibir_pessoa(resultado)
        else:
            print("Erro: Não foi possível atualizar a pessoa.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro ao atualizar pessoa: {e}")

def apagar_pessoa(cliente: PessoaCliente):
    """Apaga uma pessoa"""
    print("\n--- Apagar Pessoa ---")
    email = input("Email da pessoa a apagar: ").strip()
    
    if not email:
        print("Erro: Email é obrigatório!")
        return
    
    # Verifica se a pessoa existe
    try:
        pessoa_existente = cliente.buscarPorEmail(email)
        
        if not pessoa_existente:
            print(f"Erro: Pessoa com email '{email}' não encontrada.")
            return
        
        print(f"\nPessoa a ser apagada:")
        exibir_pessoa(pessoa_existente)
        
        confirmacao = input("\nTem certeza que deseja apagar? (s/N): ").strip().lower()
        
        if confirmacao == 's':
            resultado = cliente.apagar(email)
            
            if resultado:
                print(f"\n✓ Pessoa apagada com sucesso!")
            else:
                print("Erro: Não foi possível apagar a pessoa.")
        else:
            print("Operação cancelada.")
    except Exception as e:
        print(f"Erro ao apagar pessoa: {e}")

def exibir_pessoa(pessoa: dict):
    """Exibe os dados de uma pessoa formatados"""
    print(f"  Email: {pessoa.get('email', 'N/A')}")
    print(f"  Nome: {pessoa.get('nome') or 'Não informado'}")
    print(f"  Idade: {pessoa.get('idade') or 'Não informado'}")
    print(f"  Altura: {pessoa.get('altura') or 'Não informado'}")

def main():
    """Função principal que executa o menu"""
    cliente = PessoaCliente()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            criar_pessoa(cliente)
        elif opcao == "2":
            buscar_por_email(cliente)
        elif opcao == "3":
            listar_todas(cliente)
        elif opcao == "4":
            atualizar_pessoa(cliente)
        elif opcao == "5":
            apagar_pessoa(cliente)
        elif opcao == "0":
            print("\nSaindo... Até logo!")
            break
        else:
            print("\n Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()

