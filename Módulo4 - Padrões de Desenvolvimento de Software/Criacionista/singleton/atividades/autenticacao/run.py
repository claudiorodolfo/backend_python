from autenticacao import AuthManager

if __name__ == "__main__":
    auth1 = AuthManager().getInstance()
    auth2 = AuthManager().getInstance()
    print("Instância única?", auth1 is auth2)  # Deve ser True

    # Registrar usuários
    auth1.registrar("alice", "senhaAlice", "admin")
    auth1.registrar("bob", "senhaBob", "comum")
    auth2.registrar("charlie", "senhaCharlie", "comum")
    auth1.registrar("diana", "senhaDiana", "admin")
    auth2.registrar("erick", "senhaErick", "comum")
    auth1.registrar("fernanda", "senhaFernanda", "admin")
    auth1.registrar("gabriel", "senhaGabriel", "comum")
    auth2.registrar("helena", "senhaHelena", "admin")
    auth1.registrar("igor", "senhaIgor", "comum")
    auth2.registrar("julia", "senhaJulia", "admin")
    
    # Verificar usuários antes do login
    print("Usuários cadastrados antes do login:", auth1.todosUsuariosRegistrados())
    print("-"*30)

    # Tentar autenticar com Alice
    sucesso = auth2.login("alice", "senhaAlice")
    print("Alice logou com sucesso?", sucesso)  # True
    print("-"*30)
    # Tentar autenticar com Bob
    sucesso_bob = auth1.login("bob", "senhaBob")
    print("Bob logou com sucesso?", sucesso_bob)  # True
    print("-"*30) 
    # Tentar autenticar com Helena
    sucesso_helena = auth2.login("helena", "helena")
    print("Helena logou com sucesso?", sucesso_helena)  # True
    print("-"*30)

     # Verificar usuários autenticados
    print("Usuários logados antes do logout:", auth1.todosUsuariosAutenticados())
    print("-"*30)

    # Logout (remove o usuário do dicionário)
    auth2.logout("alice")
    print("Usuário alice removido após logout")
    print("-"*30)

    # Verificar usuários após logout
    print("Usuários logados após logout:", auth2.todosUsuariosAutenticados())
