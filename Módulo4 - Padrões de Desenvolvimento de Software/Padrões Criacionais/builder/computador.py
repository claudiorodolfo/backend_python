class Computador:
    
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.armazenamento = None
        self.gpu = None
        self.monitor = None
        self.bateria = None
        self.peso = None

    def __str__(self):
        componentes = f"cpu={self.cpu}, ram={self.ram}, armazenamento={self.armazenamento}, gpu={self.gpu}"
        if self.monitor:
            componentes += f", monitor={self.monitor}"
        if self.bateria:
            componentes += f", bateria={self.bateria}, peso={self.peso}"
        return f"Computador({componentes})"

