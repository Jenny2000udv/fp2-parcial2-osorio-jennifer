from vehiculo import Vehiculo

class Parqueo:
    def __init__(self, nombre: str, capacidad: int = 6):
        self.nombre: str = nombre
        self.capacidad: int = capacidad
        self.estacionados: list[Vehiculo] = []
        self.total_recaudado: int = 0
        self.historial_salidas: list[dict] = []

    def espacios_libres(self) -> int:
        return self.capacidad - len(self.estacionados)

    def registrar_entrada(self, vehiculo: Vehiculo, hora: int) -> bool:
        # Validación de horario de atención: de 6 a 22 horas
        if not (6 <= hora < 22):
            print(f"\n❌ Acceso denegado: El parqueo atiende de 6 a 22 horas (Hora ingresada: {hora}:00 hrs).")
            return False

        # Validación de capacidad (hasta 6 vehículos)
        if len(self.estacionados) >= self.capacidad:
            print(f"\n❌ Parqueo lleno: Capacidad máxima ({self.capacidad}) alcanzada.")
            return False

        # Validación de placa única
        if self.buscar(vehiculo.placa) is not None:
            print(f"\n⚠️ El vehículo con placa {vehiculo.placa} ya se encuentra dentro.")
            return False

        vehiculo.hora_entrada = hora
        self.estacionados.append(vehiculo)
        print(f"\n✅ Entrada registrada: {vehiculo.describir()}")
        print(f"   Hora de ingreso: {hora}:00 hrs | Espacios libres: {self.espacios_libres()}")
        return True

    def buscar(self, placa: str) -> Vehiculo | None:
        placa_buscada = placa.strip().upper()
        for v in self.estacionados:
            if v.placa == placa_buscada:
                return v
        return None

    def registrar_salida(self, placa: str, hora: int) -> int:
        if not (6 <= hora <= 22):
            print(f"\n❌ Fuera de horario de atención (6 a 22 horas).")
            return -1

        vehiculo = self.buscar(placa)
        if vehiculo is None:
            print(f"\n⚠️ No se encontró ningún vehículo con placa '{placa}'.")
            return -1

        if hora < vehiculo.hora_entrada:
            print(f"\n❌ Error: La hora de salida ({hora}:00) no puede ser menor a la de entrada ({vehiculo.hora_entrada}:00).")
            return -1

        # Se cobra por hora entera aunque salga a la misma hora (mínimo 1 hora)
        horas = max(1, hora - vehiculo.hora_entrada)
        total_pago = vehiculo.calcular_tarifa(horas)

        self.total_recaudado += total_pago
        self.estacionados.remove(vehiculo)

        self.historial_salidas.append({
            "vehiculo": vehiculo.describir(),
            "placa": vehiculo.placa,
            "horas": horas,
            "total": total_pago
        })

        print("\n" + "=" * 45)
        print("          COMPROBANTE DE SALIDA              ")
        print("=" * 45)
        print(vehiculo.describir())
        print(f"Hora de entrada:  {vehiculo.hora_entrada}:00 hrs")
        print(f"Hora de salida:   {hora}:00 hrs")
        print(f"Horas cobradas:   {horas} hora(s) entera(s)")
        print(f"Total a pagar:    Q{total_pago}")
        print(f"Espacios libres:  {self.espacios_libres()}")
        print("=" * 45)

        return total_pago

    def listar(self) -> None:
        print(f"\n--- ESTADO DEL PARQUEO: {self.nombre.upper()} ---")
        print(f"Ocupación: {len(self.estacionados)} / {self.capacidad} | Libres: {self.espacios_libres()}")
        if not self.estacionados:
            print("El parqueo está vacío.")
        else:
            for idx, v in enumerate(self.estacionados, 1):
                print(f"  {idx}. {v.describir()} (Entrada: {v.hora_entrada}:00 hrs)")
        print("-" * 50 + "\n")