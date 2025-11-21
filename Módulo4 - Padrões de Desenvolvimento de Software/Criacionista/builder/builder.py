"""
Exemplo de uso do padrão Builder para construção de computadores
"""
from pc_gamer_builder import PCGamerBuilder
from escritorio_builder import EscritorioBuilder
from notebook_builder import NotebookBuilder
from diretor import Diretor, TipoComputador

if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO PADRÃO BUILDER")
    print("=" * 60)
    
    # Builder 1: PC Gamer
    print("\n1. Construindo PC Gamer:")
    print("-" * 60)
    builderGamer = PCGamerBuilder()
    diretor = Diretor(builderGamer)
    pcGamer = diretor.construir(TipoComputador.PC_GAMER)
    print(pcGamer)
    
    # Builder 2: Computador de Escritório
    print("\n2. Construindo Computador de Escritório:")
    print("-" * 60)
    builderEscritorio = EscritorioBuilder()
    diretor = Diretor(builderEscritorio)
    pcEscritorio = diretor.construir(TipoComputador.ESCRITORIO)
    print(pcEscritorio)
    
    # Builder 3: Notebook
    print("\n3. Construindo Notebook:")
    print("-" * 60)
    builderNotebook = NotebookBuilder()
    diretor = Diretor(builderNotebook)
    notebook = diretor.construir(TipoComputador.NOTEBOOK)
    print(notebook)
    
    # Demonstração de uso direto do builder (sem diretor)
    print("\n4. Construção customizada (sem diretor):")
    print("-" * 60)
    notebookCustom = (NotebookBuilder()
                     .setCpu("Apple M2 Pro")
                     .setRam("32GB")
                     .setArmazenamento("1TB SSD")
                     .setGpu("GPU Integrada M2")
                     .setMonitor("16\" Retina")
                     .setBateria("100Wh")
                     .setPeso("2.0kg")
                     .construir())
    print(notebookCustom)
    
    # Demonstração de construção customizada usando o diretor
    print("\n5. Construção customizada (com diretor, sem tipo):")
    print("-" * 60)
    builderCustom = NotebookBuilder()
    diretorCustom = Diretor(builderCustom)
    builder = diretorCustom.construir()  # Retorna o builder para configuração manual
    notebookCustom2 = (builder
                      .setCpu("Intel i7-13700H")
                      .setRam("32GB DDR5")
                      .setArmazenamento("2TB SSD")
                      .setGpu("RTX 4070")
                      .setMonitor("17\" 4K")
                      .setBateria("99Wh")
                      .setPeso("2.5kg")
                      .construir())
    print(notebookCustom2)

