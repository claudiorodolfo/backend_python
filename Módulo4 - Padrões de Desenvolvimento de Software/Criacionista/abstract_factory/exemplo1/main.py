from factories import FabricaGUI, FabricaClara, FabricaEscura

# Uso
def renderizarInterface(fabrica: FabricaGUI):
    botao = fabrica.criarBotao()
    caixaSelecao = fabrica.criarCaixaSelecao()
    print(botao.renderizar())
    print(caixaSelecao.renderizar())

if __name__ == "__main__":
    renderizarInterface(FabricaClara())  # Botão claro / Checkbox claro
    renderizarInterface(FabricaEscura())   # Botão escuro / Checkbox escuro

