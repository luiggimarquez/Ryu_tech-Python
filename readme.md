# Ryu Technology

Este site desarrllado para este proyecto es una pequeña aplicación para salvar los cursos de un sistema educativo, consiste en registro de estudiantes, de profesores, de cursos y la asignacion almunos y docentes al los cursos; incluye un sistema de busqueda de los cursos donde da la informacion de los miembros que pertenecen a este.

![web principal](./App_1/static/images/imgreadme1.jpg)


## Comenzando 🚀

Este es un proyecto público, puedes decargarte una copia desde la pestaña code o haciendo un Clone 😊

Mira [aquí](https://github.com/luiggimarquez/Ryu_tech-Python/tree/Pre-entrega_3) 

El proyecto está formado por las páginas:  index, estudiantes, cursos, profesores y busqueda, junto a las de login y registro.

El archivo principal dde estilos es style.css, ubicado en el folder App_1/static/css

Algunos componentes estan sacados de boostrap, éste ademas formatea muchos de los estilos del proyecto de forma automática

### Pre-requisitos 📋

Se necesita tener instalado Python: [descargar](https://www.python.org/downloads/) (importante seleccionar añadir Python al Path en windows)

Se trabajo en un entorno virtual, por lo que librerias se cargan con el archivo requirements.txt. Debes tener instalado algún entorno virtual, en el proyecto se usó VirtualEnt

Puedes utilizar Visual Studio Code o Sublime Text para revisarlo 🔧

### Instalación 🔧 👨‍💻

Estas instrucciones están hechas para **Visual Studio Code**, con el cual lo realicé:

*Instalar si hace falta, Python.

* Instalar VirtualEnv (En consola instalar con `pip install virtualenv`, en Mac escribir `pip3 install virtualenv`)

* Para clonar el repositorio de github del proyecto, copiamos el URL en Github

![github](./App_1/static/images/githubreadme1.jpg)

* En Visual Studio, crear una carpeta y hacer click derecho -> 

![vsc](./App_1/static/images/visualreadme1.jpg)

Esto nos ubica en la carpeta creada para el proyecto en el terminal

* Escribir del comando `git clone`, pegar el URL del repositorio después  y presionar enter, esto nos crea una carpeta del proyecto llamada **Ryu-Tech-Python**. En el terminal escribimos `cd Ryu-Tech-Python` para entrar en el root del proyecto.

* Crear un entorno virtual entrando en la consola/terminal: ´py -m venv venv´ en Windows; para Mac escribir `python3 -m venv venv`

* Activar el entorno virtual creado con: `.\venv\Scripts\activate` para windows, para Mac usar `source venv/bin/activate` (si da access denied elevar con SUDO) 

* Instalar los paquetes/librerias usados en el proyecto con: `pip install -r "requirements.txt"` 

* Estando ubicados en el root del proyecto (Ryu_tech-Python/) Compila con `py manage.py runserver` en windows, en Mac con ` python3 manage.py runserver`  


Ya podemos acceder en el navegador con el localhost o http://127.0.0.1:8000/ . En caso de tener el puerto ocuado, se puede ejecutar con `py manage.py runserver XXXX` donde XXXX es el puerto que se desee usar



## Construido con 🛠️


* El código está hecho directamente python V 3.11.2 desarollado en Visual Studio Code 1.74.3

* Se uso principalmente el framework Django V 4.1

* Las imágenes no son de mi autoría, todo es material público en internet.

* El layout del frontend está hecho con flexbox  y desarrollado algunos componentes con boostrap 5.3.

* Se usó virtualenv como entorno virtual

* El DB usado es el SQLite proporcionado por Django


## Resumen del proyecto 📜
#

Este Proyecto backend está estructurado en la  arquitectura MVT (Model-View-Template)

Posee una aplicacion llamada **App_1** donde se desarolla toda la programación

>URLS

En nuestro folder principal **Preentrega_3**, desde **urls.py** incluimos todas las rutas usadas en la aplicacion a traves de **path("", include('App_1.urls'))**

Nuestras rutas principales estan contenidas en App_1.urls.py y son las siguientes:

* `/` nos dirige al home (index.html) del sitio.
* `Signup/` nos dirige a la página de registro de usuario.
* `login/` permite iniciar sesión.
* `logout/` permite cerrar sesión.
* `estudiantes/` nos dirige al formulario para agregar estudiantes.
* `profesores/` nos dirige al formulario para agregar docentes.
* `cursos/` nos dirige al formulario para crear cursadas/materias/cursos.
* `busqueda/` permite buscar las cursadas existentes y mostrar los miembros.
* `admin/` permite entrar al ambiente de administración.

Todas las páginas están restringidas al login a traves del decorador **@login_required** (`django.contrib.auth.decorators`), que obliga a estar logueado para navegar en los recursos, asi que se debe iniciar sesión para acceder al contenido. Todos los sitios redirigen al **login/** y desde aquí se puede iniciar sesión o ir a la página **signup/** para registrar un nuevo usuario y poder acceder a todo la página.

>Views

Todos los views se encuentrar en la app **App_1** en **views.py**.

*`base`: Esta funcion es el home. En este se carga el index.html que contiene los layouts básicos del sitio: navar, footer, links a las otras funcionalidades y tiene una imagen Hero solo para decorar.

*`singup`: Esta función tiene la logica del registro de usuarios. En primer lugar hace una validación si hay un usuario logueado (si hay alguien logueado lo lógico es que no se pueda registrar un nuevo usuario) asi que mediante `request.user.is_authenticated` se valida esto: si hay un usuario activo se redirige a **Home**, si no, se ejecuta la lógica.

Trabaja de la siguiente forma: se valida que método se esta recibiendo, GET o POST; si es GET significa que se está cargando la página y renderiza a **singUp.HMTL**, enviandole un diccionario con el form proveniente de **django.contrib.auth.forms** , este es **UserCreationForm** que ya nos da la funcionalidad en Django para crear un usuario. Si por el contrario se recibe un metodo POST, es decir, se enviaron datos desde la página a través del formulario, primero se verifica con un **if** si los dos password son iguales (el form UserCreationForm incluye un input para confirmar el password), si son diferentes se envia un mensaje de error en el renderizado del la página **signup.html** para informar que los passwords no coinciden, si todo sale bien, se almacena en la base datos (save()), se ejecuta el login con login() proporcionado por **django.contrib.auth** y redirige a **home** con el usuario ya logueado (una cookie con los datos del login)


*`log_out`: esta función llama a logout() que es proporcionado por **django.contrib.auth** para cerrar la sesión del usuario: elimina la cookie y se redirige a **Home**

*`log_in`: válida si ya hay un usuario logueado en primer lugar, si lo hay redirige a **home**, si no hay, valifa le metodo que se está recibiendo: si es GET renderiza la vista del login **login.html** enviandole un formulario nativo de django para la autenticación (`AuthenticationForm` de **django.contrib.auth.forms**); si el método recibido es POST, se usa authenticate() para validar los datos enviados: si no hay usuario nos devuelve vacío; De ser vacio rederizamos otra vez la vista de **login.html** adjuntandole un error de login, si no vacio la respuesta de **authenticate** usamos el metodo login() para validar el usuario con el login

*`estudiantes`: esta función renderiza el formulario para agregar estudiantes a la base de datos; si es un metodo GET, nos renderiza el archivo **estudiantes.html** con el formulario adjunto. si es POST, primero valida la info proveniente del frontend con `ìs_valid()`:

## Autor✒️

Este proyecto fue realizado para las clases de Python de CoderHouse por:

**Ing. Luiggi Márquez** - [GitHub Profile](https://github.com/luiggimarquez) ✌️

Buenos Aires, Argentina 2023
