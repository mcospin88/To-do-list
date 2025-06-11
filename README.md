# To-Do List API con FastAPI

Este es un proyecto backend desarrollado con **FastAPI** que gestiona tareas (to-do list). Permite a los usuarios crear, leer, actualizar y eliminar tareas. Utiliza SQLAlchemy como ORM y PostgreSQL como base de datos principal.

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)

## Estructura del proyecto

- **app/main.py**: Inicia la aplicación FastAPI.
- **app/database.py**: Define la conexión con PostgreSQL y el motor SQLAlchemy.
- **app/models.py**: Contiene la definición del modelo `Task` para la base de datos.
- **app/schemas.py**: Define los esquemas Pydantic según el estándar JSON:API.
- **app/routers.py**: Contiene los endpoints (rutas) para la API.

## Instalación y ejecución local

1. **Clonar este repositorio**

```bash
git clone https://github.com/tuusuario/todolist-api.git
cd todolist-api
```

2. **Crear y activar un entorno virtual**

```bash
python -m venv venv
source venv/bin/activate 
```

3. **Instalar las dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**

```bash
uvicorn app.main:app --reload
```

Esto levantará el servidor en `http://127.0.0.1:8000`.

## Uso con Docker
Desde la raíz del proyecto, se puede construir y levantar la aplicación ejecutando:

```bash
docker-compose up --build
```

Este comando:

- Construye la imagen de la aplicación a partir del `Dockerfile`.
- Levanta dos servicios: `web` (la aplicación FastAPI) y `db` (la base de datos PostgreSQL).
- Expone la API en `http://localhost:8000`.
- Crea y guarda los datos de PostgreSQL en un volumen persistente llamado `postgres_data`.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Eso levanta el servidor FastAPI y lo expone en el puerto `8000`. Por lo tanto, la API queda disponible en:  
[http://localhost:8000](http://localhost:8000)

- Si se modifica el código fuente y se quiere ver reflejado, se puede reiniciar Docker con:

```bash
docker compose down
docker compose up --build
```

---
## Pruebas de la API con Postman

Para probar los endpoints de la API mientras se ejecuta en Docker, se puede usar Postman o cualquier cliente HTTP.
Como el contenedor expone el puerto 8000 en la máquina local, simplemente se usa la URL: http://localhost:8000


---

## Endpoints disponibles

- `GET /tasks/` → Lista todas las tareas activas
- `GET /tasks/{id}` → Obtiene una tarea por ID
- `POST /tasks/` → Crea una nueva tarea
- `PUT /tasks/{id}` → Actualiza una tarea existente
- `PATCH /tasks/{id}` → Actualiza parcialmente una tarea
- `DELETE /tasks/{id}` → Marca una tarea como eliminada (soft delete)
- `GET /tasks/deleted/` → Lista todas las tareas eliminadas
- `POST /tasks/{id}/restore/` → Restaura una tarea previamente eliminada

---

## Formato de las respuestas (JSON:API)

Todas las respuestas están estructuradas bajo el estándar [JSON:API](https://jsonapi.org/). Esto implica:

- Los datos están envueltos bajo una clave `"data"`.
- Cada objeto tiene `"type"`, `"id"` y `"attributes"`.

Ejemplo de respuesta al hacer un `GET`:

```json
{
  "data": {
    "type": "task",
    "id": "1",
    "attributes": {
      "title": "Comprar leche",
      "description": "Ir al super a comprar leche deslactosada",
      "completed": false
    }
  }
}
```

---

## Ejemplos de peticiones JSON

### Crear una tarea (`POST /tasks/`)

```json
{
  "data": {
    "type": "task",
    "attributes": {
      "title": "Estudiar FastAPI",
      "description": "Leer la documentación oficial y hacer pruebas",
      "completed": false
    }
  }
}
```

### Actualizar una tarea completamente (`PUT /tasks/1`)

```json
{
  "data": {
    "type": "task",
    "id": "1",
    "attributes": {
      "title": "Estudiar FastAPI y SQLAlchemy",
      "description": "Revisar documentación, practicar ejemplos reales",
      "completed": true
    }
  }
}
```

### Actualizar parcialmente una tarea (`PATCH /tasks/1`)

```json
{
  "data": {
    "type": "task",
    "id": "1",
    "attributes": {
      "completed": true
    }
  }
}
```

### Eliminar una tarea (Soft Delete) (`DELETE /tasks/1`)

No requiere cuerpo (`body`). Solo se envia la petición y se marcará como eliminada internamente. No se muestra más en las listas `GET`.

---

## Soft Delete implementado

Cuando se elimina una tarea con `DELETE`, esta no se borra de la base de datos. Se marca como eliminada con un campo especial. Esto permite:

- Recuperar tareas en el futuro.
- Evitar pérdidas accidentales.

Las rutas `GET` automáticamente ocultan tareas eliminadas.

---

## Autor

María Cospin
