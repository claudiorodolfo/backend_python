from abc import ABC, abstractmethod
from typing import Type, Dict
from interfaces import Cao, Gato, Pato
from interfaces.animal import Animal

# Fábrica abstrata
class FabricaAnimais(ABC):
    def __init__(self):
        # Registro de tipos de animais que esta fábrica pode criar
        # Cada fábrica concreta deve preencher este dicionário
        self._tipos_animais: Dict[str, Type[Animal]] = {}
        self._inicializar_tipos()
    
    @abstractmethod
    def _inicializar_tipos(self):
        """
        Método abstrato para inicializar o registro de tipos de animais.
        Cada fábrica concreta deve implementar este método para registrar
        os tipos de animais que ela pode criar.
        """
        pass
    
    def criar_animal(self, tipo: str) -> Animal:
        """
        Método genérico para criar qualquer animal registrado.
        Permite adicionar novos animais sem modificar a fábrica abstrata.
        
        Args:
            tipo: Nome do tipo de animal (ex: 'cao', 'gato', 'pato')
            
        Returns:
            Instância do animal solicitado
            
        Raises:
            ValueError: Se o tipo de animal não estiver registrado
        """
        tipo_lower = tipo.lower()
        if tipo_lower not in self._tipos_animais:
            tipos_disponiveis = ', '.join(self._tipos_animais.keys())
            raise ValueError(
                f"Tipo de animal '{tipo}' não está registrado nesta fábrica. "
                f"Tipos disponíveis: {tipos_disponiveis}"
            )
        return self._tipos_animais[tipo_lower]()
    
    # Métodos de conveniência para compatibilidade com código existente
    # Estes métodos podem ser removidos se preferir usar apenas criar_animal()
    def criarCao(self) -> Cao:
        return self.criar_animal('cao')
    
    def criarGato(self) -> Gato:
        return self.criar_animal('gato')
    
    def criarPato(self) -> Pato:
        return self.criar_animal('pato')

