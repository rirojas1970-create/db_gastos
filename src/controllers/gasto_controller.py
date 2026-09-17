from datetime import datetime
from src.services.gasto_service import GastoService

class GastoController:
    def __init__(self, service: GastoService):
        self.service = service

    def menu(self):
        while True:
            print("\n=== Gestión de Gastos ===")
            print("1. Registrar gasto")
            print("2. Listar gastos")
            print("3. Actualizar gasto")
            print("4. Eliminar gasto")
            print("5. Salir")
            opcion = input("Elegí una opción: ").strip()

            if opcion == "1":
                self._registrar_gasto()
            elif opcion == "2":
                self._listar_gastos()
            elif opcion == "3":
                self._actualizar_gasto()
            elif opcion == "4":
                self._eliminar_gasto()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción inválida, intentá de nuevo.")

    def _registrar_gasto(self):
        nombre = input("Nombre del gasto: ").strip()
        categoria = input("Categoría (ej. Combustible, Gas, Supermercado): ").strip()
        monto = self._pedir_monto()
        fecha = self._pedir_fecha()

        try:
            gasto = self.service.registrar_gasto(nombre, categoria, monto, fecha)
            print(f"✅ Gasto registrado: {gasto.nombre} - ${gasto.monto} ({gasto.fecha})")
        except ValueError as e:
            print(f"❌ Error: {e}")

    def _listar_gastos(self):
        gastos = self.service.listar_gastos()
        if not gastos:
            print("No hay gastos registrados todavía.")
            return
        print("\n--- Gastos registrados ---")
        for g in gastos:
            print(f"{g.id} | {g.fecha} | {g.categoria:15} | {g.nombre:20} ${g.monto}")

    def _actualizar_gasto(self):
        self._listar_gastos()
        valor = input("\nID del gasto a actualizar (o vacío para cancelar): ").strip()
        if valor == "":
            print("Cancelado.")
            return
        try:
            gasto_id = int(valor)
        except ValueError:
            print("❌ Ingresá un número de ID válido.")
            return

        try:
            actual = self.service.obtener_gasto(gasto_id)
        except ValueError as e:
            print(f"❌ Error: {e}")
            return

        print(f"\nEditando: {actual.nombre} | {actual.categoria} | ${actual.monto} | {actual.fecha}")
        print("Dejá vacío el campo que no querés cambiar.\n")

        nombre = input(f"Nombre [{actual.nombre}]: ").strip() or None
        categoria = input(f"Categoría [{actual.categoria}]: ").strip() or None

        monto_input = input(f"Monto [{actual.monto}]: ").strip()
        monto = None
        if monto_input:
            try:
                monto = float(monto_input)
            except ValueError:
                print("❌ Monto inválido, se mantiene el valor actual.")

        fecha_input = input(f"Fecha [{actual.fecha}] (AAAA-MM-DD): ").strip()
        fecha = None
        if fecha_input:
            try:
                fecha = datetime.strptime(fecha_input, "%Y-%m-%d").date()
            except ValueError:
                print("❌ Fecha inválida, se mantiene el valor actual.")

        try:
            gasto = self.service.actualizar_gasto(
                gasto_id, nombre=nombre, categoria=categoria, monto=monto, fecha=fecha
            )
            print(f"✅ Actualizado: {gasto.nombre} - ${gasto.monto} ({gasto.fecha})")
        except ValueError as e:
            print(f"❌ Error: {e}")

    def _eliminar_gasto(self):
        self._listar_gastos()
        valor = input("\nID del gasto a eliminar (o vacío para cancelar): ").strip()
        if valor == "":
            print("Cancelado.")
            return
        try:
            gasto_id = int(valor)
        except ValueError:
            print("❌ Ingresá un número de ID válido.")
            return

        try:
            gasto = self.service.eliminar_gasto(gasto_id)
            print(f"🗑️ Eliminado: {gasto.nombre} - ${gasto.monto}")
        except ValueError as e:
            print(f"❌ Error: {e}")

    def _pedir_monto(self):
        while True:
            valor = input("Monto: ").strip()
            try:
                monto = float(valor)
                if monto <= 0:
                    print("El monto debe ser mayor a cero.")
                    continue
                return monto
            except ValueError:
                print("Ingresá un número válido (ej. 1500.50).")

    def _pedir_fecha(self):
        while True:
            valor = input("Fecha (AAAA-MM-DD, dejar vacío para hoy): ").strip()
            if valor == "":
                return datetime.today().date()
            try:
                return datetime.strptime(valor, "%Y-%m-%d").date()
            except ValueError:
                print("Formato inválido. Usá AAAA-MM-DD (ej. 2026-09-16).")