from vehiculo import Vehiculo
from cliente import Cliente

class Pickup(Vehiculo):
    def __init__(self, placa: str, color: str, dueno: Cliente, carga_ton: int, hora_entrada: int = None):
        super().__init__(placa, color, dueno, hora_entrada)
        self.carga_ton: int = carga_ton

    def calcular_tarifa(self, horas: int) -> int:
        horas_cobradas = max(1, horas)
        return (horas_cobradas * 15) + 10

    def describir(self) -> str:
        return f"[Pickup] {super().describir()} | Carga: {self.carga_ton} Ton"