"""
01 - INTRODUÇÃO A PADRÕES DE PROJETO (DESIGN PATTERNS)
=====================================================

O que são Padrões de Projeto?
------------------------------
Padrões de projeto são soluções comprovadas para problemas recorrentes no 
desenvolvimento de software. Eles representam melhores práticas que foram 
identificadas e documentadas pela comunidade de desenvolvedores ao longo dos anos.

Benefícios do uso de padrões:
1. Reutilização de código testado e comprovado
2. Comunicação: desenvolvedores compartilham linguagem comum
3. Manutenibilidade: código mais organizado e fácil de entender
4. Escalabilidade: soluções que suportam crescimento
5. Redução de bugs: padrões são soluções maduras e testadas

Classificação dos Padrões
--------------------------
Os padrões são classificados em três categorias principais:

1. PADRÕES CRIACIONAIS (Creational Patterns)
   - Focam no processo de criação de objetos
   - Exemplos: Singleton, Factory Method, Builder, Prototype
   - Problema que resolvem: Como criar objetos de forma flexível?

2. PADRÕES ESTRUTURAIS (Structural Patterns)
   - Focam na composição de classes e objetos
   - Exemplos: Adapter, Decorator, Facade, Proxy
   - Problema que resolvem: Como organizar classes e objetos?

3. PADRÕES COMPORTAMENTAIS (Behavioral Patterns)
   - Focam na comunicação entre objetos
   - Exemplos: Observer, Strategy, Command, Template Method
   - Problema que resolvem: Como objetos interagem e se comunicam?

Exemplos Práticos de Aplicação
------------------------------
"""

# EXEMPLO 1: Problema sem padrão vs. com padrão
# ==============================================

# SEM PADRÃO: Criação direta de objetos
class ConexaoMySQL:
    def conectar(self):
        return "Conectado ao MySQL"

class ConexaoPostgreSQL:
    def conectar(self):
        return "Conectado ao PostgreSQL"

# Problema: código acoplado, difícil de estender
def usar_banco_dados(tipo):
    if tipo == "mysql":
        conexao = ConexaoMySQL()
    elif tipo == "postgresql":
        conexao = ConexaoPostgreSQL()
    return conexao.conectar()

# COM PADRÃO FACTORY (que veremos depois):
# - Código mais flexível
# - Fácil adicionar novos tipos
# - Baixo acoplamento


# EXEMPLO 2: Quando usar padrões
# ===============================

# CASO 1: Configuração global única (Singleton)
# Problema: Precisamos garantir uma única instância de configuração
configuracoes_globais = {}  # Sem padrão - múltiplas instâncias possíveis

# CASO 2: Diferentes formatos de saída (Strategy)
# Problema: Precisamos escolher entre diferentes algoritmos em runtime
def gerar_relatorio(formato):
    if formato == "pdf":
        # código para PDF
        pass
    elif formato == "html":
        # código para HTML
        pass
    # Sem padrão: múltiplos if/elif difíceis de manter


# EXEMPLO 3: Adicionar funcionalidades dinamicamente (Decorator)
# ===============================================================

def processar_dados(dados):
    """Função simples"""
    return dados.upper()

# Problema: Como adicionar logging, validação, cache sem modificar função?
# Sem padrão: modificar função original (viola princípio aberto/fechado)
# Com Decorator: envolver função com novas funcionalidades


if __name__ == "__main__":
    print("=" * 60)
    print("INTRODUÇÃO A PADRÕES DE PROJETO")
    print("=" * 60)
    
    print("\n1. Exemplo de problema sem padrão:")
    resultado = usar_banco_dados("mysql")
    print(f"   Resultado: {resultado}")
    
    print("\n2. Classificação dos Padrões:")
    print("   - Creational (Criação)")
    print("   - Structural (Estruturais)")
    print("   - Behavioral (Comportamentais)")
    
    print("\n3. Benefícios:")
    print("   ✓ Reutilização de código")
    print("   ✓ Comunicação entre desenvolvedores")
    print("   ✓ Manutenibilidade")
    print("   ✓ Escalabilidade")
    print("   ✓ Redução de bugs")

