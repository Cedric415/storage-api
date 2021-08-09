from json import dumps as json_dumps
from os import environ
import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required
from modules.inflog import(
add_user,
get_users,
add_noticia
)

app = bottle.Bottle()

## Add a new user
@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        username = str(payload['username'])
        password = str(payload['password'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        email = str(payload['email'])
        print("Datos Aceptados")
        respuesta = add_user(**payload)
        print(respuesta)
        print("Done")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)

@app.get("/users")
def get_all_info(*args, **kwargs):
    try:
       respuesta = get_users()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Añadir nueva noticia
@app.post("/<id>/noticia")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_noticia = str(payload['id_noticia'])
        titulo = str(payload['titulo'])
        noticia = str(payload['noticia'])
        fuente = str(payload['fuente'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        usuario = str(payload['usuario'])
        print("Datos Aceptados")
        respuesta = add_notica(**payload)
        print(respuesta)
        print("Done")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)

@app.get("/noticias")
def get_noticias(*args, id_noticia=None, titulo=None, **kwargs):
    try:
       respuesta = get_noticias(id_noticia,titulo)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)
