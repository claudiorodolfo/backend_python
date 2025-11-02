"""
08 - Bloco finally

Este arquivo demonstra o uso do bloco finally.
"""

print("=" * 60)
print("BLOCO FINALLY")
print("=" * 60)

# ============================================
# FINALLY BÁSICO
# ============================================
print("\n1. FINALLY - Sempre executa:")
print("-" * 60)

try:
    numero = int("42")
    print(f"  Conversão: {numero}")
except ValueError:
    print("  Erro na conversão")
finally:
    print("  Bloco finally sempre executa")

# ============================================
# FINALLY COM LIMPEZA
# ============================================
print("\n2. FINALLY PARA LIMPEZA:")
print("-" * 60)

def processar_dados():
    """Simula processamento com limpeza"""
    recursos = ["recurso1", "recurso2"]
    
    try:
        print(f"  Usando recursos: {recursos}")
        resultado = 10 / 2
        print(f"  Resultado: {resultado}")
    except Exception as e:
        print(f"  Erro: {e}")
    finally:
        # Limpeza sempre executada
        print("  Limpando recursos...")
        recursos.clear()
        print(f"  Recursos limpos: {recursos}")

processar_dados()

# ============================================
# TRY-EXCEPT-FINALLY COMPLETO
# ============================================
print("\n3. TRY-EXCEPT-FINALLY COMPLETO:")
print("-" * 60)

def operacao_segura(valor):
    """Operação com tratamento completo"""
    try:
        if valor < 0:
            raise ValueError("Valor negativo")
        resultado = valor * 2
        print(f"  Processando: {valor} → {resultado}")
        return resultado
    except ValueError as e:
        print(f"  Erro capturado: {e}")
        return None
    finally:
        print("  Operação finalizada (sempre executa)")

print("\nCom valor válido:")
operacao_segura(10)

print("\nCom valor inválido:")
operacao_segura(-5)

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo: Abertura e fechamento de arquivo (simulado)
print("\nExemplo: Gerenciamento de recursos")
print("-" * 60)

arquivo_aberto = False

try:
    print("  Abrindo arquivo...")
    arquivo_aberto = True
    # Simular processamento
    print("  Processando dados...")
    resultado = 10 / 2
    print(f"  Resultado: {resultado}")
except Exception as e:
    print(f"  Erro durante processamento: {e}")
finally:
    if arquivo_aberto:
        print("  Fechando arquivo...")
        arquivo_aberto = False
        print("  Arquivo fechado")

print("\n💡 DICA: finally é útil para:")
print("  • Fechar arquivos")
print("  • Liberar recursos")
print("  • Garantir limpeza")

