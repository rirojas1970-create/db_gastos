from src.models.gasto import Gasto

class GastoRepository:
    def __init__(self, session):
        self.session = session

    def guardar(self, gasto: Gasto):
        self.session.add(gasto)
        self.session.commit()
        return gasto

    def obtener_todos(self):
        return self.session.query(Gasto).all()

    def obtener_por_id(self, gasto_id: int):
        return self.session.get(Gasto, gasto_id)

    def actualizar(self, gasto_id: int, **campos):
        gasto = self.session.get(Gasto, gasto_id)
        if gasto is None:
            return None
        for campo, valor in campos.items():
            if valor is not None and hasattr(gasto, campo):
                setattr(gasto, campo, valor)
        self.session.commit()
        return gasto

    def eliminar(self, gasto_id: int):
        gasto = self.session.get(Gasto, gasto_id)
        if gasto:
            self.session.delete(gasto)
            self.session.commit()
        return gasto