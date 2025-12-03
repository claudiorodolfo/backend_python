from concret_builders import ConstrutorComputadorGamer, ConstrutorComputadorEscritorio
from director import DiretorComputador
# --- Cliente (uso) ---
if __name__ == "__main__":
    # montar um PC gamer completo
    builder_gamer = ConstrutorComputadorGamer()
    diretor = DiretorComputador(builder_gamer)
    diretor.fabricarCompleto()
    pc_gamer = diretor.construir()
    print("PC Gamer:", pc_gamer)

    # montar um PC de escritório (básico)
    builder_office = ConstrutorComputadorEscritorio()
    diretor = DiretorComputador(builder_office)
    diretor.fabricarBasico()
    pc_office = diretor.construir()
    print("PC Escritório:", pc_office)