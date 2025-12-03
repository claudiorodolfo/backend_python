# --- Produto ---
class Computador:
    """Produto: representa um computador com várias partes configuráveis."""
    def __init__(self):
        self.cpu = None
        self.memoria = None
        self.armazenamento = None
        self.gpu = None
        self.sistema_operacional = None

    def __str__(self):
        partes = []
        if self.cpu: partes.append(f"CPU: {self.cpu}")
        if self.memoria: partes.append(f"Memória: {self.memoria}")
        if self.armazenamento: partes.append(f"Armazenamento: {self.armazenamento}")
        if self.gpu: partes.append(f"GPU: {self.gpu}")
        if self.sistema_operacional: partes.append(f"Sistema Operacional: {self.sistema_operacional}")
        return ", ".join(partes)