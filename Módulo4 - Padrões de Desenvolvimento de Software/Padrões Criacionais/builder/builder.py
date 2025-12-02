from pc_gamer_builder import PCGamerBuilder
from escritorio_builder import EscritorioBuilder
from notebook_builder import NotebookBuilder
from diretor import Diretor, TipoComputador

if __name__ == "__main__":
    # Exemplo 1: PC Gamer com Director
    builderGamer = PCGamerBuilder()
    diretor = Diretor(builderGamer)
    pcGamer = diretor.construir(TipoComputador.PC_GAMER)
    print(f"PC Gamer: {pcGamer}\n")
    
    # Exemplo 2: Computador de Escritório
    builderEscritorio = EscritorioBuilder()
    diretor = Diretor(builderEscritorio)
    pcEscritorio = diretor.construir(TipoComputador.ESCRITORIO)
    print(f"PC Escritório: {pcEscritorio}\n")
    
    # Exemplo 3: Notebook
    builderNotebook = NotebookBuilder()
    diretor = Diretor(builderNotebook)
    notebook = diretor.construir(TipoComputador.NOTEBOOK)
    print(f"Notebook: {notebook}\n")
    
    # Exemplo 4: Construção Customizada
    notebookCustom = (NotebookBuilder()
                     .setCpu("Apple M2 Pro")
                     .setRam("32GB")
                     .setArmazenamento("1TB SSD")
                     .setGpu("GPU Integrada M2")
                     .setMonitor("16\" Retina")
                     .setBateria("100Wh")
                     .setPeso("2.0kg")
                     .construir())
    print(f"Notebook Customizado: {notebookCustom}\n")

