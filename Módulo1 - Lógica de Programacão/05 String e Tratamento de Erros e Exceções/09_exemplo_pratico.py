"""
09 - Exemplo Prático Completo

Este arquivo combina strings e tratamento de exceções.
"""

print("=" * 70)
print("SISTEMA DE VALIDAÇÃO E PROCESSAMENTO DE DADOS")
print("=" * 70)

# ============================================
# FUNÇÕES DE VALIDAÇÃO
# ============================================

def validar_email(email):
    """Valida formato de email"""
    email = email.strip().lower()
    
    if not "@" in email:
        raise ValueError("Email inválido: falta @")
    
    partes = email.split("@")
    if len(partes) != 2:
        raise ValueError("Email inválido: formato incorreto")
    
    usuario, dominio = partes
    if not usuario or not dominio:
        raise ValueError("Email inválido: usuário ou domínio vazio")
    
    if "." not in dominio:
        raise ValueError("Email inválido: domínio inválido")
    
    return email

def validar_idade(idade_str):
    """Valida e converte idade"""
    try:
        idade = int(idade_str)
        
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        if idade > 120:
            raise ValueError("Idade inválida (máximo 120)")
        
        return idade
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Idade deve ser um número")
        raise

def processar_usuario(nome, email, idade_str):
    """Processa dados do usuário"""
    try:
        # Normalizar nome
        nome_normalizado = nome.strip().title()
        
        # Validar email
        email_validado = validar_email(email)
        
        # Validar idade
        idade_validada = validar_idade(idade_str)
        
        # Criar dicionário com dados
        usuario = {
            "nome": nome_normalizado,
            "email": email_validado,
            "idade": idade_validada
        }
        
        return usuario, None
        
    except ValueError as e:
        return None, str(e)
    except Exception as e:
        return None, f"Erro inesperado: {e}"

# ============================================
# EXEMPLOS DE USO
# ============================================

print("\n=== EXEMPLO 1: Dados válidos ===")
usuario, erro = processar_usuario("  joão silva  ", "joao@email.com", "25")

if erro:
    print(f"Erro: {erro}")
else:
    print(f"✓ Usuário cadastrado:")
    print(f"  Nome: {usuario['nome']}")
    print(f"  Email: {usuario['email']}")
    print(f"  Idade: {usuario['idade']} anos")

print("\n=== EXEMPLO 2: Email inválido ===")
usuario, erro = processar_usuario("Maria", "email-invalido", "30")
if erro:
    print(f"✗ Erro: {erro}")

print("\n=== EXEMPLO 3: Idade inválida ===")
usuario, erro = processar_usuario("Carlos", "carlos@email.com", "abc")
if erro:
    print(f"✗ Erro: {erro}")

print("\n=== EXEMPLO 4: Idade negativa ===")
usuario, erro = processar_usuario("Ana", "ana@email.com", "-5")
if erro:
    print(f"✗ Erro: {erro}")

print("\n" + "=" * 70)
print("RESUMO")
print("=" * 70)
print("\n✓ Validação de dados com tratamento de exceções")
print("✓ Normalização de strings (strip, title, lower)")
print("✓ Validação de formato (email)")
print("✓ Conversão segura de tipos (int)")
print("✓ Mensagens de erro claras")
print("✓ Código robusto e seguro")

print("\n" + "=" * 70)

