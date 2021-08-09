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

def get_users(users=None):
    query_result = query_storage(
        "user/users",
    )
    if users is None:
        return query_result["content"]

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
