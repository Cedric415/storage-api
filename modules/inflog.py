import datetime
import hashlib
import models.auth
from bottle import response, request
import jwt

new =[]
def add_news(noticia_id, titulo, categoria, fecha, noticia, fuente):
    new = {
        "noticia_id": noticia_id,
        "titulo": titulo,
        "categoria": categoria,
        "fecha": fecha,
        "noticia": noticia,
        "fuente": fuente
    }
    news.append(new)
    return json.dumps(new)

def get_news()
    return print(news)
