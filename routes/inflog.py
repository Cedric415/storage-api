from json import dumps as json_dumps
from os import environ
import bottle
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required

app = bottle.Bottle()

## Add a new
@app.post("/inflog/noticia")
def add_a_news(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get news by "noticia_id"
@app.get("/inflog/noticia/<noticia_id>")
def get_news_id(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get news by "usuario_id"
@app.get("/inflog/noticia/<usuario_id>")
def get_news_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get user by usuer_id
@app.post("/inflog/almacen_usuario/<usuario_id>")
def get_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get reports by "noticia_id"
@app.get("/inflog/reportes/<noticia_id>")
def get_report_id(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
