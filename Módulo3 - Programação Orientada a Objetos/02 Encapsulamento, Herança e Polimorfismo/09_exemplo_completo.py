"""
Exemplo Completo: Sistema de Pagamento

Este exemplo integra todos os conceitos:
- Encapsulamento (atributos privados/protegidos)
- Getters e Setters (@property)
- Herança (diferentes tipos de funcionários)
- Sobrescrita de métodos (override)
- Polimorfismo (calcular_pagamento)
"""

# ==========================================
# SISTEMA DE PAGAMENTO COMPLETO
# ==========================================

class Funcionario:
    """
    Classe base para funcionários.
    
    Demonstra encapsulamento com atributos protegidos.
    """
    
    def __init__(self, nome, cpf, salario_base):
        """
        Construtor da classe base.
        
        Args:
            nome: Nome do funcionário
            cpf: CPF do funcionário
            salario_base: Salário base
        """
        self._nome = nome
        self._cpf = cpf
        self._salarioBase = salario_base
    
    # PROPRIEDADES COM @property (Encapsulamento)
    @property
    def nome(self):
        """Getter para nome."""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """Setter com validação."""
        if not valor or len(valor.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor.strip()
    
    @property
    def cpf(self):
        """Getter para CPF (read-only)."""
        return self._cpf
    
    @property
    def salarioBase(self):
        """Getter para salário base."""
        return self._salarioBase
    
    @salarioBase.setter
    def salarioBase(self, valor):
        """Setter com validação."""
        if valor < 0:
            raise ValueError("Salário base não pode ser negativo")
        self._salarioBase = valor
    
    # MÉTODO POLIMÓRFICO (será sobrescrito)
    def calcularPagamento(self):
        """
        Calcula o pagamento do funcionário.
        
        Este método será sobrescrito nas subclasses.
        Retorna o salário base por padrão.
        
        Returns:
            Valor do pagamento
        """
        return self._salarioBase
    
    def trabalhar(self):
        """Método genérico de trabalho."""
        print(f"{self._nome} está trabalhando")
    
    def exibirInfo(self):
        """Exibe informações do funcionário."""
        pagamento = self.calcularPagamento()
        print(f"""
        {'=' * 50}
        Funcionário: {self._nome}
        CPF: {self._cpf}
        Cargo: {self.__class__.__name__}
        Salário Base: R${self._salarioBase:.2f}
        Pagamento Total: R${pagamento:.2f}
        {'=' * 50}
        """)


class Vendedor(Funcionario):
    """
    Vendedor herda de Funcionario.
    
    Demonstra herança e sobrescrita de métodos.
    """
    
    def __init__(self, nome, cpf, salario_base, vendas_mes):
        """
        Construtor de Vendedor.
        
        Args:
            nome: Nome do vendedor
            cpf: CPF
            salario_base: Salário base
            vendas_mes: Total de vendas do mês
        """
        super().__init__(nome, cpf, salario_base)
        self._vendas_mes = vendas_mes
    
    @property
    def vendasMes(self):
        """Getter para vendas do mês."""
        return self._vendasMes
    
    @vendasMes.setter
    def vendasMes(self, valor):
        """Setter com validação."""
        if valor < 0:
            raise ValueError("Vendas não podem ser negativas")
        self._vendasMes = valor
    
    def calcularPagamento(self):
        """
        Sobrescreve calcular_pagamento() para incluir comissão.
        
        Comissão: 10% das vendas
        
        Returns:
            Salário base + comissão
        """
        comissao = self._vendasMes * 0.1
        return self._salarioBase + comissao
    
    def trabalhar(self):
        """Sobrescreve trabalhar() com comportamento específico."""
        print(f"{self.nome} está vendendo produtos")


class Gerente(Funcionario):
    """
    Gerente herda de Funcionario.
    
    Demonstra herança e sobrescrita com bônus fixo.
    """
    
    def __init__(self, nome, cpf, salario_base, bonus):
        """
        Construtor de Gerente.
        
        Args:
            nome: Nome do gerente
            cpf: CPF
            salario_base: Salário base
            bonus: Bônus fixo mensal
        """
        super().__init__(nome, cpf, salario_base)
        self._bonus = bonus
        self._departamento = None
    
    @property
    def bonus(self):
        """Getter para bônus."""
        return self._bonus
    
    @bonus.setter
    def bonus(self, valor):
        """Setter com validação."""
        if valor < 0:
            raise ValueError("Bônus não pode ser negativo")
        self._bonus = valor
    
    @property
    def departamento(self):
        """Getter para departamento."""
        return self._departamento
    
    @departamento.setter
    def departamento(self, valor):
        """Setter para departamento."""
        self._departamento = valor
    
    def calcularPagamento(self):
        """
        Sobrescreve calcularPagamento() para incluir bônus.
        
        Returns:
            Salário base + bônus
        """
        return self._salarioBase + self._bonus
    
    def trabalhar(self):
        """Sobrescreve trabalhar() com comportamento específico."""
        if self._departamento:
            print(f"{self.nome} está gerenciando o departamento {self._departamento}")
        else:
            print(f"{self.nome} está gerenciando")


class Desenvolvedor(Funcionario):
    """
    Desenvolvedor herda de Funcionario.
    
    Não sobrescreve calcular_pagamento() - usa implementação do pai.
    """
    
    def __init__(self, nome, cpf, salario_base, linguagem):
        """
        Construtor de Desenvolvedor.
        
        Args:
            nome: Nome do desenvolvedor
            cpf: CPF
            salario_base: Salário base
            linguagem: Linguagem de programação
        """
        super().__init__(nome, cpf, salario_base)
        self._linguagem = linguagem
    
    @property
    def linguagem(self):
        """Getter para linguagem."""
        return self._linguagem
    
    @linguagem.setter
    def linguagem(self, valor):
        """Setter com validação."""
        if not valor:
            raise ValueError("Linguagem não pode ser vazia")
        self._linguagem = valor
    
    def trabalhar(self):
        """Sobrescreve trabalhar() com comportamento específico."""
        print(f"{self.nome} está programando em {self._linguagem}")


# ==========================================
# FUNÇÃO POLIMÓRFICA
# ==========================================

def calcular_folha_pagamento(lista_funcionarios):
    """
    Calcula a folha de pagamento total.
    
    Demonstra polimorfismo: funciona com qualquer funcionário
    que tenha o método calcular_pagamento().
    
    Args:
        lista_funcionarios: Lista de objetos Funcionario
    
    Returns:
        Total da folha de pagamento
    """
    total = 0
    print("\n" + "=" * 60)
    print("FOLHA DE PAGAMENTO")
    print("=" * 60)
    
    for func in lista_funcionarios:
        pagamento = func.calcular_pagamento()
        total += pagamento
        tipo = func.__class__.__name__
        print(f"  {func.nome} ({tipo}): R${pagamento:.2f}")
    
    print(f"\n{'=' * 60}")
    print(f"TOTAL: R${total:.2f}")
    print("=" * 60)
    
    return total


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    """Demonstra o sistema completo."""
    
    print("=" * 60)
    print("SISTEMA DE PAGAMENTO - EXEMPLO COMPLETO")
    print("=" * 60)
    
    # ==========================================
    # 1. CRIANDO FUNCIONÁRIOS (ENCAPSULAMENTO)
    # ==========================================
    
    print("\n" + "=" * 60)
    print("1. CRIANDO FUNCIONÁRIOS")
    print("=" * 60)
    
    # Usando encapsulamento (@property)
    vendedor1 = Vendedor("Ana Silva", "111.111.111-11", 3000, 10000)
    vendedor1.nome = "Ana Silva Santos"  # Usa setter (validação)
    
    gerente1 = Gerente("Bruno Santos", "222.222.222-22", 5000, 1500)
    gerente1.departamento = "Vendas"
    
    dev1 = Desenvolvedor("Carla Costa", "333.333.333-33", 4000, "Python")
    dev2 = Desenvolvedor("Daniel Oliveira", "444.444.444-44", 4500, "Java")
    
    print("✓ Funcionários criados com encapsulamento")
    
    # ==========================================
    # 2. SOBRESCRITA DE MÉTODOS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("2. SOBRESCRITA DE MÉTODOS (OVERRIDE)")
    print("=" * 60)
    
    print("\nCada funcionário trabalha de forma diferente:")
    vendedor1.trabalhar()
    gerente1.trabalhar()
    dev1.trabalhar()
    
    # ==========================================
    # 3. POLIMORFISMO
    # ==========================================
    
    print("\n" + "=" * 60)
    print("3. POLIMORFISMO - CALCULAR PAGAMENTO")
    print("=" * 60)
    
    equipe = [vendedor1, gerente1, dev1, dev2]
    
    print("\nInformações individuais:")
    for func in equipe:
        func.exibir_info()  # Cada um calcula pagamento diferente
    
    # ==========================================
    # 4. FUNÇÃO POLIMÓRFICA
    # ==========================================
    
    calcular_folha_pagamento(equipe)
    
    # ==========================================
    # 5. MODIFICANDO VALORES (ENCAPSULAMENTO)
    # ==========================================
    
    print("\n" + "=" * 60)
    print("4. MODIFICANDO VALORES (ENCAPSULAMENTO)")
    print("=" * 60)
    
    print("\nAumentando vendas do vendedor:")
    print(f"Vendas anteriores: R${vendedor1.vendas_mes:.2f}")
    vendedor1.vendas_mes = 15000  # Usa setter (validação)
    print(f"Novas vendas: R${vendedor1.vendas_mes:.2f}")
    
    print("\nRecalculando pagamento:")
    vendedor1.exibir_info()
    
    # ==========================================
    # RESUMO DOS CONCEITOS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("CONCEITOS APLICADOS")
    print("=" * 60)
    
    print("""
    ✓ ENCAPSULAMENTO: Atributos protegidos (_nome, _salario_base)
    ✓ @property: Getters/setters elegantes
    ✓ HERANÇA: Vendedor, Gerente, Desenvolvedor herdam de Funcionario
    ✓ SOBRESCRITA: calcular_pagamento() e trabalhar() sobrescritos
    ✓ POLIMORFISMO: calcular_folha_pagamento() funciona com qualquer funcionário
    ✓ VALIDAÇÃO: Setters validam dados antes de atribuir
    ✓ CÓDIGO LIMPO: Separação de responsabilidades
    """)


if __name__ == "__main__":
    main()

