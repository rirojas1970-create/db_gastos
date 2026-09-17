# App de Gestión de Gastos

Aplicación de consola para registrar, listar, actualizar y eliminar gastos personales/familiares, con persistencia en MySQL.

## Arquitectura

Proyecto organizado siguiendo principios SOLID, con separación en capas:
- `models/` — entidades de dominio (SQLAlchemy)
- `repositories/` — acceso a datos
- `services/` — lógica de negocio
- `controllers/` — interacción con el usuario (consola)
- `config/` — configuración y conexión a base de datos

## Instalación

1. Cloná el repositorio
2. Creá un entorno virtual: `python -m venv .venv`
3. Activalo: `source .venv/bin/activate`
4. Instalá dependencias: `pip install -r requirements.txt`
5. Creá un archivo `.env` con tus credenciales de MySQL (ver `.env.example`)
6. Ejecutá: `python main.py`

## Variables de entorno necesarias (.env)

```
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
```