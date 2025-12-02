from computador import Computador
from computador_builder import ComputadorBuilder
from pc_gamer_builder import PCGamerBuilder

if __name__ == "__main__":
    builder = PCGamerBuilder()
    builder.setCpu("Intel i9-13900K")
    builder.setRam("32GB DDR5")
    builder.setGpu("RTX 4080")
    computador = builder.construir()
    print(f"Computador: {computador}\n")
    
    computador2 = (PCGamerBuilder()
                   .setCpu("AMD Ryzen 9")
                   .setRam("64GB")
                   .setGpu("RTX 4090")
                   .construir())
    print(f"Computador 2: {computador2}")

