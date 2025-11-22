from factories import FabricaAnimaisPequenos, FabricaAnimaisMedios, FabricaAnimaisGrandes

def demonstrarAnimais(fabrica):
    """Demonstra a criação e uso de animais através de uma fábrica"""
    print(f"\n{'='*60}")
    print(f"Criando animais de porte: {fabrica.__class__.__name__.replace('FabricaAnimais', '').lower()}")
    print(f"{'='*60}\n")
    
    # Criar animais usando a fábrica
    cao = fabrica.criarCao()
    gato = fabrica.criarGato()
    pato = fabrica.criarPato()
    
    # Demonstrar os animais
    print(f"Cão ({cao.getPorte()}): {cao.latir()}")
    print(f"Gato ({gato.getPorte()}): {gato.miar()}")
    print(f"Pato ({pato.getPorte()}): {pato.grasnar()}")
    print()

if __name__ == "__main__":
    # Demonstrar animais de pequeno porte
    fabricaPequenos = FabricaAnimaisPequenos()
    demonstrarAnimais(fabricaPequenos)
    
    # Demonstrar animais de médio porte
    fabricaMedios = FabricaAnimaisMedios()
    demonstrarAnimais(fabricaMedios)
    
    # Demonstrar animais de grande porte
    fabricaGrandes = FabricaAnimaisGrandes()
    demonstrarAnimais(fabricaGrandes)
    
    print("\n" + "="*60)
    print("Demonstração do padrão Abstract Factory concluída!")
    print("="*60)

