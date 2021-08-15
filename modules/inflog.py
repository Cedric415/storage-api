import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)


def add_user(id = None, username = None, password = None, fecha = None, email = None):

    print("Datos del usuario")
    print(id, username, password, fecha, email)
    print("Capturado")


    data_almacen = {
        "id": id,
        "username": username,
        "password": password,
        "fecha": fecha,
        "email": email,
    }
    nombre_archivo = f"{username}-{id}-{password}-{fecha}-{email}.json"
    datos_usuario = store_string(
        "user/users",
        nombre_archivo,
        json.dumps(data_almacen)
    )
    return datos_usuario

def get_users(id=None, username=None):
    query_result = query_storage(
        "user/users",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
        print("done")
    if username is not None:
        return [
           r
           for r in query_result["content"]
           if username in r
        ]

def add_noticia(id_noticia = None, titulo = None, noticia = None, fuente = None, fecha = None, usuario = None):

    print("Datos de la noticia")
    print(id_noticia, titulo, noticia, fuente, fecha, usuario)
    print("Exito")

    almacenable2 = {
        "id_noticia": id_noticia,
        "titulo": titulo,
        "noticia": noticia,
        "fuente": fuente,
        "fecha": fecha,
        "usuario": usuario,
    }
    nombre_de_archivo = f"{id_noticia}-{titulo}-{noticia}-{fuente}-{fecha}-{usuario}.json"
    datos_noticia = store_string(
        "noticia/noticias",
        nombre_de_archivo,
        json.dumps(almacenable2)
    )
    return datos_noticia

def get_noticias(id_noticia = None):
    query_result = query_storage(
        "noticia/noticias",
    )
    if id_noticia is not None:
        return [
           i
           for i in query_result["content"]
           if id_noticia in i
        ]
        print("Done")


def add_reporte(id_reporte = None, titulo_reporte = None, reporte = None, fecha = None, usuario = None):
    print("Datos del reporte")
    print(id_reporte, titulo_reporte, reporte, fecha, usuario)
    print("Exito")

    almacenable3 = {
        "id_reporte": id_reporte,
        "titulo_reporte": titulo_reporte,
        "reporte": reporte,
        "fecha": fecha,
        "usuario": usuario,
    }
    nombre_de_archivo = f"{id_reporte}-{titulo_reporte}-{reporte}-{fecha}-{usuario}.json"
    datos_reporte = store_string(
        "reporte/reportes",
        nombre_de_archivo,
        json.dumps(almacenable3)
    )
    return datos_reporte

def get_reportes(id_reporte = None, titulo_reporte = None):
        query_result = query_storage(
            "reporte/reportes",
        )
        if id_reporte is not None:
            return [
               i
               for i in query_result["content"]
               if id_reporte in i
            ]
            print("Done")
        if titulo_reporte is not None:
            return [
               i
               for i in query_result["content"]
               if titulo_reporte in i
            ]
            print("Done")
