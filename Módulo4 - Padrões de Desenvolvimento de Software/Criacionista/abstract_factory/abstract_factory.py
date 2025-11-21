# Este arquivo foi refatorado e separado em múltiplos arquivos:
# - interfaces.py: Botao, CaixaSelecao (interfaces abstratas)
# - light_theme.py: BotaoClaro, CaixaSelecaoClara
# - dark_theme.py: BotaoEscuro, CaixaSelecaoEscura
# - factories.py: FabricaGUI, FabricaClara, FabricaEscura
# - main.py: renderizarInterface e código de uso
#
# Execute main.py para usar o padrão Abstract Factory

from main import renderizarInterface
from factories import FabricaClara, FabricaEscura

if __name__ == "__main__":
    renderizarInterface(FabricaClara())  # Botão claro / Checkbox claro
    renderizarInterface(FabricaEscura())   # Botão escuro / Checkbox escuro
