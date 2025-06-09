# To-Do List API con FastAPI

Este es un proyecto backend desarrollado con **FastAPI** que gestiona tareas (to-do list). Permite a los usuarios crear, leer, actualizar y eliminar tareas de manera eficiente. Utiliza SQLAlchemy como ORM y SQLite como base de datos para almacenamiento local.

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

## Instalación y ejecución

1. **Clona este repositorio**

```bash
git clone https://github.com/tuusuario/todolist-api.git
cd todolist-api
```

2. **Crea y activa un entorno virtual**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecuta la aplicación**

```bash
uvicorn app.main:app --reload
```

Esto levantará el servidor en `http://127.0.0.1:8000`.

## Endpoints disponibles

- `GET /tasks/` → Lista todas las tareas
- `GET /tasks/{id}` → Obtiene una tarea por ID
- `POST /tasks/` → Crea una nueva tarea
- `PUT /tasks/{id}` → Actualiza una tarea existente
- `PATCH /tasks/{id}` → Actualiza parcialmente una tarea (solo algunos campos)
- `DELETE /tasks/{id}` → Elimina una tarea

## Estado del proyecto

Este proyecto está en etapa funcional básica.

## Autor: 
María Cospin
