# Inflog
> Autor: Cedric Flores
## Consiste en
_En este proyecto vamos a realizar un blog en la que  tendras que logearte para poder subir noticias, los usuarios subiran noticias cortas y su fuente de informacion en las que se se veran el la noticia quien subio la noticia y la categoria a la que pertenece. (Ejemplo: Tecnoloiga)_
## Aplicacion
_Este proyecto puede ser utilizado mas que nada como un medio de informacion lleno de noticias que puedan subir los mismos usuarios para estar al tanto de las noticias actuales que hay, dependiendo del tema de interes que el usuario desee saber._

## Modelado de datos

_Las entidades con las que trabajaremos seran_,

 - Usuario (usuario_id, nombre, e_mail, password)
 - Noticia (noticia_id, usuario_id, titulo, categoia, noticia, fuente)
 - Reportes (reporte_id, usuario_id, noticia_id, descripcion)

## Interacciones de datos

_Aqui se mostraran algunas interacciones entre los datos que se veran utilizados en este proyecto_

- No se podra subir una noticia sin antes registrarse
- Se podran ver las noticias pero para hacer un comentario sobre la noticia deberas estar registrado
- Se podra realizar reportes sobre las noticias para señalar si estas son falsas o por el estilo
## Consultas de datos
_Algunas de las consultas que se pueden realizar son:_
- Consultar datos de las noticias
  - Por Id
  - Por usuario
  - Por categoria

- Consultar datos de los usuarios
  - Por id

- Consultar lista de noticias
  - Todas
  - Por id
  - Por categoria
## Operaciones de datos

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

## Rutas https



## Ejemplos de mensajes HTTP

## Registro de noticia Nueva
```
{
   "titulo": "El tether asusta a los expertos: puede ser el verdadero 'cisne negro' de las criptomonedas",
   "categoria": "Economia",
   "usuario": "Elm Inion",
   "noticia": "Ya que no es tan mediático, lo primero es presentar al tether. Se trata de una stablecoin o activo digital ligado a un activo del mundo real, en este caso el dólar"
   "Fuente": "https://www.eleconomista.es"
}
```
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

## Ejemplos de interacciones con el servidor
```
POST /inflog/storage_user
```
- Recibe una estructura para registrar un usuario nuevo.
- 201, registra al usuario y regresa un mensaje informando que se ha registrado exitosamente.
- D.O.M regresa un mensaje de falla.

```
POST /inflog/noticia
```
- Recibe una estructura para registrar una noticia nueva.
- 201, sube la noticia y regresa un mensaje informando que se ha subido correctamente.
- D.O.M regresa un mensaje de falla.

```
GET /inflog/storage_user
```
- Recibe una estructura para registrar un usuario nuevo.
- 201, registra al usuario y regresa un mensaje informando que se ha registrado exitosamente.
- D.O.M regresa un mensaje de falla.

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
