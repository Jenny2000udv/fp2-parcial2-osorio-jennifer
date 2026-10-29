class Cliente:
    def __init__(self, nombre: str, telefono: str):
        self.nombre: str = nombre.strip()
        self.telefono: str = telefono.strip()

    def describir(self) -> str:
        return f"Dueño: {self.nombre} (Tel: {self.telefono})"