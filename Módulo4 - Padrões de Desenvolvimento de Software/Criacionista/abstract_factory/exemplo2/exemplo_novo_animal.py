"""
Exemplo demonstrando como adicionar um novo animal (Coelho) 
SEM modificar a fábrica abstrata FabricaAnimais.

Este exemplo mostra a flexibilidade da nova implementação desacoplada.
"""

from abc import abstractmethod
from interfaces.animal import Animal

# 1. Criar a interface do novo animal (sem modificar a fábrica abstrata)
class Coelho(Animal):
    @abstractmethod
    def saltar(self) -> str:
        pass
    
    @abstractmethod
    def getPorte(self) -> str:
        pass

# 2. Criar as implementações concretas do novo animal
class CoelhoPequeno(Coelho):
    def saltar(self) -> str:
        return "Pulo! (salto pequeno de coelho pequeno)"
    
    def getPorte(self) -> str:
        return "Pequeno"

class CoelhoMedio(Coelho):
    def saltar(self) -> str:
        return "PULO! (salto médio de coelho de médio porte)"
    
    def getPorte(self) -> str:
        return "Médio"

class CoelhoGrande(Coelho):
    def saltar(self) -> str:
        return "PULO PULO! (salto grande de coelho grande)"
    
    def getPorte(self) -> str:
        return "Grande"

# 3. Atualizar as fábricas concretas para incluir o novo animal
# (Apenas as fábricas concretas, NÃO a fábrica abstrata!)

from factories.fabrica_animais_pequenos import FabricaAnimaisPequenos
from factories.fabrica_animais_medios import FabricaAnimaisMedios
from factories.fabrica_animais_grandes import FabricaAnimaisGrandes

# Estender as fábricas existentes para incluir o coelho
class FabricaAnimaisPequenosComCoelho(FabricaAnimaisPequenos):
    def _inicializar_tipos(self):
        # Chama o método da classe pai para inicializar os tipos existentes
        super()._inicializar_tipos()
        # Adiciona o novo animal ao registro existente
        self._tipos_animais['coelho'] = CoelhoPequeno

class FabricaAnimaisMediosComCoelho(FabricaAnimaisMedios):
    def _inicializar_tipos(self):
        super()._inicializar_tipos()
        self._tipos_animais['coelho'] = CoelhoMedio

class FabricaAnimaisGrandesComCoelho(FabricaAnimaisGrandes):
    def _inicializar_tipos(self):
        super()._inicializar_tipos()
        self._tipos_animais['coelho'] = CoelhoGrande

# 4. Demonstrar o uso
if __name__ == "__main__":
    print("\n" + "="*60)
    print("EXEMPLO: Adicionando novo animal (Coelho) sem modificar")
    print("a fábrica abstrata FabricaAnimais")
    print("="*60)
    
    # Criar fábricas com o novo animal
    fabrica_pequenos = FabricaAnimaisPequenosComCoelho()
    fabrica_medios = FabricaAnimaisMediosComCoelho()
    fabrica_grandes = FabricaAnimaisGrandesComCoelho()
    
    # Usar o método genérico para criar o novo animal
    coelho_pequeno = fabrica_pequenos.criar_animal('coelho')
    coelho_medio = fabrica_medios.criar_animal('coelho')
    coelho_grande = fabrica_grandes.criar_animal('coelho')
    
    print(f"\nCoelho Pequeno ({coelho_pequeno.getPorte()}): {coelho_pequeno.saltar()}")
    print(f"Coelho Médio ({coelho_medio.getPorte()}): {coelho_medio.saltar()}")
    print(f"Coelho Grande ({coelho_grande.getPorte()}): {coelho_grande.saltar()}")
    
    # Também funciona com os animais existentes
    cao = fabrica_pequenos.criar_animal('cao')
    print(f"\nCão Pequeno ({cao.getPorte()}): {cao.latir()}")
    
    print("\n" + "="*60)
    print("✓ Novo animal adicionado SEM modificar FabricaAnimais!")
    print("="*60 + "\n")

