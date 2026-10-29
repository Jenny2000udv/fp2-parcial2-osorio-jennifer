from vehiculo import Vehiculo
from cliente import Cliente

class Carro(Vehiculo):
    def __init__(self, placa: str, color: str, dueno: Cliente, puertas: int, hora_entrada: int = None):
        super().__init__(placa, color, dueno, hora_entrada)
        self.puertas: int = puertas

    def calcular_tarifa(self, horas: int) -> int:
        horas_cobradas = max(1, horas)
        total = horas_cobradas * 10
        return min(total, 60)

    def describir(self) -> str:
        return f"[Carro] {super().describir()} | Puertas: {self.puertas}"