from json import dumps as json_dumps
from os import environ
import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required
from modules.inflog import(add_user, get_users, add_noticia, get_noticias, add_reporte, get_reportes)

app = bottle.Bottle()

'''
## Add a new user

curl http://localhost:8080/inflog/store  -X POST -H 'Content-Type: application/json'  -d '{"id" : "2" , "username" : "John" , "password" : "pass321" , "fecha":"2021-01-01" , "email" : "estesunejemplot3@ejemplo.com"}'

'''
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

'''
## ver los usuarios generados

curl http://localhost:8080/inflog/3/alonso -X GET

'''
@app.get("/<id>/<username>")
def users(*args, id=None, username=None, **kwargs):
    try:
       respuesta = get_users(id=id, username=username)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

'''
## Añadir una noticia

curl http://localhost:8080/inflog/noticias  -X POST -H 'Content-Type: application/json'  -d '{"id_noticia" : "2" , "titulo" : "Llego el manin" , "categoria" : "Sociales" , "noticia" : "pues que ya llego el manin" , "fuente" : "wikipedia.comelmanin" , "fecha":"2021-01-01" , "usuario" : "IronWill44"}'

'''
@app.post("/noticias")
def noticias(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_noticia = str(payload['id_noticia'])
        titulo = str(payload['titulo'])
        categoria = str(payload['categoria'])
        noticia = str(payload['noticia'])
        fuente = str(payload['fuente'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        usuario = str(payload['usuario'])
        print("Datos Aceptados")
        respuesta = add_noticia(**payload)
        print(respuesta)
        print("Done")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)

'''
## ver los noticias generadas

curl http://localhost:8080/inflog/2 -X GET

'''
@app.get("/<id_noticia>")
def get_noticia(*args, id_noticia=None, **kwargs):
    try:
       respuesta = get_noticias(id_noticia)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

'''
## Añadir un reporte

curl http://localhost:8080/inflog/report  -X POST -H 'Content-Type: application/json'  -d '{"id_reporte" : "2" , "titulo_reporte" : "Llego el manin" , "reporte" : "pues que no llego el manin" , "fecha":"2021-01-01" , "usuario" : "BronzeWill44"}'

'''
@app.post("/report")
def report(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_reporte = str(payload['id_reporte'])
        titulo_reporte = str(payload['titulo_reporte'])
        reporte = str(payload['reporte'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        usuario = str(payload['usuario'])
        print("Datos Aceptados")
        respuesta = add_reporte(**payload)
        print(respuesta)
        print("Done")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)

'''
## ver los reportes generados

curl http://localhost:8080/inflog/2/no_llego_el_manin -X GET

'''
@app.get("/<id_reporte>/<titulo_reporte>")
def get_reporte(*args, id_reporte=None, titulo_reporte=None, **kwargs):
    try:
       respuesta = get_reportes(id_reporte, titulo_reporte)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)
