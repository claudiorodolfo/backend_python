from builder import ConstrutorComputador

# --- Concrete Builders ---
class ConstrutorComputadorGamer(ConstrutorComputador):
    def construirCpu(self):
        self._pc.cpu = "Intel i9-13900K"

    def construirMemoria(self):
        self._pc.memoria = "32GB DDR5"

    def construirArmazenamento(self):
        self._pc.armazenamento = "1TB SSD NVMe"

    def construirGpu(self):
        self._pc.gpu = "NVIDIA RTX 4080"

    def instalarSistema(self):
        self._pc.sistema_operacional = "Ubuntu 22.04"


class ConstrutorComputadorEscritorio(ConstrutorComputador):
    def construirCpu(self):
        self._pc.cpu = "Intel i5-12400"

    def construirMemoria(self):
        self._pc.memoria = "16GB DDR4"

    def construirArmazenamento(self):
        self._pc.armazenamento = "500GB SSD"

    # sem GPU
    
    def instalarSistema(self):
        self._pc.sistema_operacional = "Windows 11"