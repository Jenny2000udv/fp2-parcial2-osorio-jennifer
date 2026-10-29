from abc import ABC, abstractmethod
from cliente import Cliente

class Vehiculo(ABC):
    def __init__(self, placa: str, color: str, dueno: Cliente, hora_entrada: int = None):
        # La placa en minúscula y mayúscula es la misma
        self.placa: str = placa.strip().upper()
        self.color: str = color.strip()
        self.dueno: Cliente = dueno
        self.hora_entrada: int | None = hora_entrada

    @abstractmethod
    def calcular_tarifa(self, horas: int) -> int:
        """Método abstracto para calcular la tarifa en Quetzales."""
        pass

    def describir(self) -> str:
        """Devuelve placa, color y dueño usando el describir() del cliente."""
        return f"Placa: {self.placa} | Color: {self.color} | {self.dueno.describir()}"