from collections import defaultdict
from src.repositories.gasto_repository import GastoRepository

class EstadisticasService:
    def __init__(self, repository: GastoRepository):
        self.repository = repository

    def _filtrar(self, gastos, año=None, mes=None, categoria=None):
        resultado = []
        for g in gastos:
            if año and g.fecha.year != año:
                continue
            if mes and g.fecha.month != mes:
                continue
            if categoria and g.categoria.lower() != categoria.lower():
                continue
            resultado.append(g)
        return resultado

    def total_por_categoria(self, categoria: str, año: int = None, mes: int = None):
        """Total gastado en una categoría específica (ej. Combustible, Gas)"""
        gastos = self.repository.obtener_todos()
        filtrados = self._filtrar(gastos, año=año, mes=mes, categoria=categoria)
        total = sum(g.monto for g in filtrados)
        return {"categoria": categoria, "total": total, "cantidad": len(filtrados)}

    def resumen_por_categoria(self, año: int = None, mes: int = None):
        """Total agrupado por cada categoría (para comparar todas)"""
        gastos = self.repository.obtener_todos()
        filtrados = self._filtrar(gastos, año=año, mes=mes)
        resumen = defaultdict(float)
        for g in filtrados:
            resumen[g.categoria] += g.monto
        return dict(sorted(resumen.items(), key=lambda x: x[1], reverse=True))

    def resumen_por_mes(self, año: int = None):
        """Total agrupado por mes (para ver la evolución mensual)"""
        gastos = self.repository.obtener_todos()
        filtrados = self._filtrar(gastos, año=año)
        resumen = defaultdict(float)
        for g in filtrados:
            clave = f"{g.fecha.year}-{g.fecha.month:02d}"
            resumen[clave] += g.monto
        return dict(sorted(resumen.items()))

    def total_general(self, año: int = None, mes: int = None):
        """Total de todos los gastos en el período"""
        gastos = self.repository.obtener_todos()
        filtrados = self._filtrar(gastos, año=año, mes=mes)
        return sum(g.monto for g in filtrados)