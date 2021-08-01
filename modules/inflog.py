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
