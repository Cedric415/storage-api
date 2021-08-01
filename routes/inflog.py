from json import dumps as json_dumps
from os import environ
import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required
from modules.inflog import(add_user)

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
