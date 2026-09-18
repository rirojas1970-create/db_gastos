from src.config.database import SessionLocal, Base, engine
from src.repositories.gasto_repository import GastoRepository
from src.services.gasto_service import GastoService
from src.services.estadisticas_service import EstadisticasService
from src.controllers.gasto_controller import GastoController

def main():
    Base.metadata.create_all(engine)

    session = SessionLocal()
    repo = GastoRepository(session)
    service = GastoService(repo)
    estadisticas = EstadisticasService(repo)
    controller = GastoController(service, estadisticas)

    controller.menu()

    session.close()

if __name__ == "__main__":
    main()