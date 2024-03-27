# Curso de FastAPI

---

- python -m venv venv
- pip install "fastapi[all]"

## Nota

  También puedes instalarlo parte por parte.

  Esto es lo que probablemente harías una vez que desees implementar tu aplicación en producción:

    pip install fastapi

  También debes instalar uvicorn para que funcione como tu servidor:

    pip install "uvicorn[standard]"

  Y lo mismo para cada una de las dependencias opcionales que quieras utilizar.

---

## Iniciar el server

    uvicorn main:app --reload

## Detener el server

    CTRL + C

---

## Documentación

Documentación con swagger: <http://127.0.0.1:8000/docs>

Documentación con redoc: <http://127.0.0.1:8000/redoc>

---

## JWT

Para instalarlo:

    pip install "python-jose[cryptography]"

Instalar passlib:

    pip install "passlib[bcrypt]"
