# Inflog
> Autor: Cedric Flores
## Consiste en
_En este proyecto vamos a realizar un blog en la que  tendras que logearte para poder subir noticias, los usuarios subiran noticias cortas y su fuente de informacion en las que se se veran el la noticia quien subio la noticia y la categoria a la que pertenece. (Ejemplo: Tecnoloiga)_
## Aplicacion
_Este proyecto puede ser utilizado mas que nada como un medio de informacion lleno de noticias que puedan subir los mismos usuarios para estar al tanto de las noticias actuales que hay, dependiendo del tema de interes que el usuario desee saber._

## Modelado de datos

_Las entidades con las que trabajaremos seran_,

 - Usuario (usuario_id, nombre, e_mail, password)
 - Noticia (noticia_id, usuario_id, titulo, categoria, fecha, noticia, fuente)
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
  - por fecha

- Consultar datos de los usuarios
  - Por id

- Consultar lista de noticias
  - Todas
  - Por id
  - Por categoria
  - Por fecha
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
| Path                  | Descripción |
| --------------------- | ----------- |
|  /inflog/noticia          |   se podran consultar todas las noticias
|  /inflog/noticia/<noticia_id>         |  Se podra consultar las noticias por medio de su identificador unico
|  /inflog/noticia/<usuario_id>          |  Se podra consultar las noticias subidas por un usuario
|  /inflog/almacen_usuario/<usuario_id> |   Se podra consultar la informacion del usuario         
|  /inflog/reportes/<noticia_id>/ | Se podran consultar los reportes hechos hacia una noticia por medio de su id

## Ejemplos de mensajes HTTP

### Registro de noticia Nueva
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
POST /inflog/almacen_usuario
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
GET /inflog/noticia
```
- Regresa los datos de una noticia
- 200, despliega la informacion de la noticia solicitada.
- D.O.M regresa un mensaje de falla.

```
GET /inflog/noticia/<usuario_id>
```
- Regresa los datos de las noticias subidas por un usuario
- 200, despliega la informacion sobre los noticias realizadas por un usuario.
- D.O.M regresa un mensaje de falla.

```
GET /inflog/reportes
```
- Regresa los datos de los reportes hechos.
- 200, despliega la informacion sobre los reportes realizados.
- D.O.M regresa un mensaje de falla.

```
GET /inflog/reportes/<noticia_id>
```
- Regresa los datos de los reportes hechos hacia una noticia.
- 200, despliega la informacion sobre los reportes realizados hacia una noticia.
- D.O.M regresa un mensaje de falla.

## Plan de implementacion (Aspecto General)

_Con este proyecto se busca crear una pagina web donde un usuario puede acceder a la pagina web para buscar noticias sobre algun tema en particular que desee investigar ya que en esta pagina estaran divididas por categoria como pueden ser noticias tecnologias, sobre economia, etc. Asi como se puden visualizar noticias tambien se podran subir noticias que tu encuentres en internet para asi contribuir a la pagina, para esto se requerira de un registro previo para poder subir noticias y tambien para poder realizar reportes sobre alguno noticia ya sea por que la noticia se encuentre mal categorizada asi como una noticia que pudiese llegar a ser "Fake" o simplemente una noticia no relevante._

##  Plan de implementacion (Aspecto Tecnico)
### Modulos de codigo necesarios
- Las rutas son necesarias ya que en estas se encuentra el como esta estructurado el proyecto y el como funcionara.

- Las funciones de almacenamiento seran necesarias para archivar la informacion que sea subida al proyecto.

- Funciones para agregar, eliminar o editar datos que sean subidos al proyecto.


### Metodos de almacenamiento requeridos
- Almacenamiento por medio de archivos locales archivos locales.

### Plan para la codificacion de los modulos
_Los modulos seran planeados e implementeados a medida que se vaya desarrollando el proyecto para verficar y confirmar de que se va encargar cada modula para el funcionamiento del proyecto sea efectivo._

### Plan para la verificacion de la calidad del producto
_Una vez el proyecto se encuetre finalizado o al menos utilizable se realizaran una serie de pruebas para verificar que el funcionamiento del proyecto sea correcto se subiran noticias, se registraran usuarios, se eliminaran usuarios, etc. Todas estas pruebas para verficar que la pagina no tenga alguna fisura al momento de querer utilizarla._

# Computo en la nube

## Commit
- Crear un fork del proyecto storage-api
- Entregable, señalar cual es el commit-hash, apartir del que ustedes realizaron el fork:
| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de Fork|   812228b0e369322b4c541fc8f18a51efd47a6932

- Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones
- Entregable, señalar el commit-hash que contiene la creación de dichos archivos.


| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de docs/inflog.md| 1e1705b5c9874492a3ec7e2b17598ccb8d8385ad  
|  Creacion de: modules/inflog.py| 20155a2bc33890f88d9bf4253b575ff656a4eda0
|  Creacion de: models/inflog.py| 20155a2bc33890f88d9bf4253b575ff656a4eda0
|  Creacion de: routes/inflog.py| 20155a2bc33890f88d9bf4253b575ff656a4eda0

## Construido con

_Estas son algunas de las herramientas utilizadas_

* [Python](https://www.python.org)
* [PIP](https://pip.pypa.io/en/stable/installing/)

## Autores ✒️

_Cedric Flores Moreno (Lider de proyecto)_

* **Cedric Flores** - *Trabajo Inicial* - [Cedric415](https://github.com/Cedric415)
