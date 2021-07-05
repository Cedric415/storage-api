# Inflog
> Autor: Cedric Flores

_En este proyecto vamos a realizar un blog en la que  tendras que logearte para poder subir noticias, los usuarios subiran noticias cortas y su fuente de informacion en las que se se veran el la noticia quien subio la noticia y la categoria a la que pertenece. (Ejemplo: Tecnoloiga)_

## Estructura API

_Las entidades con las que trabajaremos seran_,

 - Usuario (nombre, e_mail, usuario, password)
 - Noticia (titulo, categoia, noticia, fuente)
 - Reportes (nombre, usuario, reporte)

## Operacion de almacenamiento de datos

### Operacion a realizar por el usuarios

- Registrarse
: se solicitara nombre, correo electronico, usuario y contraseña
- Actualizacion
: eliminar el usuario para despues rehacerlo.

### Subir una noticia

- Nueva noticia
: Se solicitara titulo de la noticia, la categoria, una sinopsis de la noticia, fuente de informacion(Enlace)
- Actualizar noticia noticia
: Se actualizaran unicamente los datos que desea actualizar (Titulo,categoria, noticia, fuente)

## Operacion de consulta de datos

- Solicitar datos de un usuario
   - básicos
   - noticas subidas
   - usuario
   - fecha
   - id_usuario

- Solicitar datos de una nota
   - básicos
   - autor
   - por fecha
   - por categoria
   - por titulo

## Estructura de solicitud y respuesta

### Registro de un usuario

```
{
    "nombre": "Elva Pasar",
    "e_mail": "elva_pas69@ejemplo.com"
    "usuario": "ElvPas415",
    "password": "..."
}
```
### Registro exitoso

```
{
    "id_usuario": "....",
}
```
### Registro exitoso

```
{
    "code": 500,
    "message": "este es un mensaje de error..."
}
```

## Archivos relacionados

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/noticia/usuario`        | consultar las noticias que ha subido un usuario |
| `/noticia/fecha`          | Consultar las noticias por fecha en especifico |
| `/noticia/categoria`      | Consultar las noticias por categoria de estas |
| `/noticia/query`          | Consultar las noticias por el titulo que tengan |

### Archivo principal y ruta de almacenamiento
- `inflog/inflog.py`

- `inflog/`  



## Construido con

_Estas son algunas de las herramientas utilizadas_
S
* [Python](https://www.python.org)
* [PIP](https://pip.pypa.io/en/stable/installing/)

## Autores ✒️

_Cedric Flores Moreno (Lider de proyecto)_

* **Cedric Flores** - *Trabajo Inicial* - [Cedric415](https://github.com/Cedric415)
