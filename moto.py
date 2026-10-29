from vehiculo import Vehiculo
from cliente import Cliente

class Moto(Vehiculo):
    def __init__(self, placa: str, color: str, dueno: Cliente, cilindrada: int, hora_entrada: int = None):
        super().__init__(placa, color, dueno, hora_entrada)
        self.cilindrada: int = cilindrada

    def calcular_tarifa(self, horas: int) -> int:
        horas_cobradas = max(1, horas)
        return horas_cobradas * 5

    def describir(self) -> str:
        return f"[Moto] {super().describir()} | Cilindrada: {self.cilindrada}cc"