from parqueo import Parqueo
from cliente import Cliente
from moto import Moto
from carro import Carro
from pickup import Pickup

def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("⚠️ Ingrese un número entero válido.")

def main():
    parqueo = Parqueo(nombre="Parqueo El Obelisco", capacidad=6)

    while True:
        print("=" * 35)
        print(f"     {parqueo.nombre.upper()}      ")
        print("=" * 35)
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Ver vehiculos estacionados")
        print("4. Buscar vehiculo por placa")
        print("5. Ver resumen del día")
        print("6. Salir")
        print("=" * 35)

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- REGISTRO DE ENTRADA ---")
            
            # Paso 1: Pedir tipo de vehículo ANTES de los datos del cliente
            tipo = input("Tipo de vehículo ([M] Moto, [C] Carro, [P] Pickup): ").strip().upper()

            if tipo not in ["M", "C", "P"]:
                print("❌ Tipo no válido. Solo se permite M, C o P.\n")
                continue

            # Paso 2: Pedir datos del cliente
            nombre_cliente = input("Nombre del cliente: ")
            telefono_cliente = input("Teléfono del cliente: ")
            cliente = Cliente(nombre_cliente, telefono_cliente)

            # Paso 3: Pedir datos del vehículo y atributo específico según subclase
            placa = input("Placa: ")
            color = input("Color: ")
            hora_entrada = pedir_entero("Hora de entrada (entero 6 a 22): ")

            if tipo == "M":
                cilindrada = pedir_entero("Cilindrada en cc (ej. 150): ")
                vehiculo = Moto(placa, color, cliente, cilindrada)
            elif tipo == "C":
                puertas = pedir_entero("Número de puertas (ej. 4): ")
                vehiculo = Carro(placa, color, cliente, puertas)
            elif tipo == "P":
                carga_ton = pedir_entero("Capacidad de carga en toneladas: ")
                vehiculo = Pickup(placa, color, cliente, carga_ton)

            parqueo.registrar_entrada(vehiculo, hora_entrada)

        elif opcion == "2":
            print("\n--- REGISTRO DE SALIDA ---")
            placa = input("Placa del vehículo a retirar: ")
            hora_salida = pedir_entero("Hora de salida (entero 6 a 22): ")
            parqueo.registrar_salida(placa, hora_salida)

        elif opcion == "3":
            parqueo.listar()

        elif opcion == "4":
            placa = input("\nIngresa la placa a buscar: ")
            v = parqueo.buscar(placa)
            if v:
                print(f"\n🔍 [Vehículo Localizado]")
                print(f"   {v.describir()}")
                print(f"   Hora de ingreso: {v.hora_entrada}:00 hrs\n")
            else:
                print(f"\n⚠️ El vehículo con placa '{placa}' no se encuentra en el parqueo.\n")

        elif opcion == "5":
            print("\n" + "=" * 50)
            print("             RESUMEN DEL DÍA             ")
            print("=" * 50)
            print(f"Vehículos dentro actualmente:   {len(parqueo.estacionados)}")
            print(f"Espacios libres:                {parqueo.espacios_libres()}")
            print(f"Servicios cobrados:             {len(parqueo.historial_salidas)}")
            print(f"Total recaudado en caja:        Q{parqueo.total_recaudado}")

            if parqueo.historial_salidas:
                print("\nDetalle de cobros realizados:")
                for item in parqueo.historial_salidas:
                    print(f"  • Placa {item['placa']} | {item['horas']} hr(s) -> Q{item['total']}")
            print("=" * 50 + "\n")

        elif opcion == "6":
            print("\n👋 ¡Gracias por usar el sistema de Parqueo El Obelisco! Hasta pronto.")
            break

        else:
            print("⚠️ Opción no válida. Ingrese un número del 1 al 6.\n")

if __name__ == "__main__":
    main()