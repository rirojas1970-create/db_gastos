from src.config.database import SessionLocal, Base, engine
from src.repositories.gasto_repository import GastoRepository
from src.services.gasto_service import GastoService
from src.controllers.gasto_controller import GastoController

def main():
    Base.metadata.create_all(engine)

    session = SessionLocal()
    repo = GastoRepository(session)
    service = GastoService(repo)
    controller = GastoController(service)

    controller.menu()

    session.close()

if __name__ == "__main__":
    main()