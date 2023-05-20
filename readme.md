# Ryu Technology

Este site desarrllado para este proyecto playground es una  aplicación para redactar publicaciones estilo Blog sobre tecnología, ciencia, anime y cultura y comunicarse por un sistema sencillo de chat entre los miembros del sitio; incluye un sistema de búsqueda para las publicaciones. Se busca aplicar tareas sencillas de CRUD: registrar, borrar y editar los usuarios, crear, editar y borrar publicaciones y realizar busquedas en la base de datos

![web principal](./media/readme/imgreadme1.jpg)


## Comenzando 🚀

Este es un proyecto público, puedes decargarte una copia desde la pestaña code o haciendo un Clone 😊

Mira [aquí](https://https://github.com/luiggimarquez/Ryu_tech-Python/tree/proyecto_final) 

El proyecto está formado: 3 aplicaciones **users**, **blog**, **mensajeria**, estas convergen en el **proyecto_final** que es el root del sitio. Cada app tiene sus templates con sus respectivos HTML, sus URLS y sus funciones en views.py

El archivo principal de estilos es style.css, ubicado en el folder **users/static/css**.

Algunos componentes están sacados de boostrap, éste además formatea muchos de los estilos del proyecto de forma automática.

### Pre-requisitos 📋

Se necesita tener instalado Python 🐍: [descargar](https://www.python.org/downloads/) (importante seleccionar añadir Python al Path en Windows) 

Se trabajó en un entorno virtual, por lo que librerías se cargan con el archivo **requirements.txt**. Debes tener instalado algún entorno virtual, en el proyecto se usó **VirtualEnv**

Puedes utilizar Visual Studio Code o Sublime Text para revisarlo 🔧

### Instalación 🔧 👨‍💻

Estas instrucciones están hechas para **Visual Studio Code**, con el cual lo realicé:

* Instalar si hace falta, Python 🐍.

* Instalar VirtualEnv (En consola instalar con `pip install virtualenv`, en Mac escribir `pip3 install virtualenv`)

* Para clonar el repositorio de github del proyecto, copiamos el URL en Github.

![github](./media/readme/githubreadme1.jpg)

* En Visual Studio, crear una carpeta y hacer click derecho -> 

![vsc](./media/readme/visualreadme1.jpg)

Esto nos ubica en la carpeta creada para el proyecto en el terminal

* Escribir del comando `git clone`, pegar el URL del repositorio después  y presionar enter, esto nos crea una carpeta del proyecto llamada **Ryu-Tech-Python**. En el terminal escribimos `cd Ryu-Tech-Python` para entrar en el root del proyecto.

* Crear un entorno virtual entrando en la consola/terminal: `py -m venv venv` en Windows; para Mac escribir `python3 -m venv venv`

* Activar el entorno virtual creado con: `.\venv\Scripts\activate` para windows, para Mac usar `source venv/bin/activate` (si da access denied elevar con SUDO)

Si al ejecutar el **activate** por powerShell en windows se genera un error de permisos, ejecutar en powerShell: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

* Instalar los paquetes/librerías usados en el proyecto con: `pip install -r "requirements.txt"`

Si en esta parte se presenta un error al intentar instalar, posiblemente el problema es PIP, se pueden ejecutar estos dos comandos:

1. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
2. `python get-pip.py`



* Estando ubicados en el root del proyecto (Ryu_tech-Python/) Compila con `py manage.py runserver` en windows, en Mac con ` python3 manage.py runserver`  


Ya podemos acceder en el navegador con el localhost o http://127.0.0.1:8000/ . En caso de tener el puerto ocupado, se puede ejecutar con `py manage.py runserver XXXX` donde XXXX es el puerto que se desee usar



## Construido con 🛠️


* El código está hecho directamente con 🐍 python V 3.11.2 desarollado en Visual Studio Code 1.74.3

* Se uso principalmente el framework Django V 4.1

* Las imágenes no son de mi autoría, todo es material público en internet.

* El layout del frontend está hecho con flexbox  y desarrollado algunos componentes con boostrap 5.3.

* Se usó virtualenv como entorno virtual

* El DB usado es el SQLite proporcionado por Django

* El contenido de los post fue copia de páginas de internet para servir de ejemplo, no son de mi autoría

* La animación usada para mostrar que no hay publicaciones fue tomada de https://lottiefiles.com/

* Los botones, fueron tomados de https://uiverse.io/


## Resumen del proyecto 📜
#

Este Proyecto backend está estructurado en la  arquitectura MVT (Model-View-Template)

Posee tres aplicacion estructuras en la función especifica que cumplen en el proyecto: *users* donde se desarrolla todo lo relativo a registros, login, perfiles, accesos; **blog** donde se desarrolla el código que crea, edita y elimina los post del blog, asi como la busqueda por titulo o por nombre de perfil de usuario; y **mensajeria** que trabaja con el pequeño y simple chat para que los usuarios se comuniquen entre los perfiles de usuario.

>URLS

En nuestro folder principal **proyecto_final**, desde **urls.py** incluimos todas las rutas usadas en la aplicación a través de:

``` 
path("", include('users.urls'))
path("pages/", include('blog.urls'))
path("mensajeria/", include('mensajeria.urls'))
```

Nuestras rutas principales están contenidas en **users.urls.py** y son las siguientes:

* `/` nos dirige al home (index.html) del sitio.
* `Signup/` nos dirige a la página de registro de usuario.
* `login/` permite iniciar sesión.
* `logout/` permite cerrar sesión.
* `profile/` nos dirige al perfil del usuario logueado.
* `profile/user/<id>` nos dirige al perfil el usuario por su id de registro.
* `user/edit/` nos dirige al formulario para editar password, email y nombre y apellido.
* `user/delete/<id>` permite borrar un usuario, solo administradores.
* `profile/edit/` permite editar bio, link,  y avatar.
* `about/` accede a la página about, que tiene los datos del desarrollador de la página


Nuestras rutas principales están contenidas en **blog.urls.py** y son las siguientes:

* `/` nos dirige al listado de publicaciones.
* `create/` nos dirige a la página de creacion del post para el blog.
* `details/<id>` nos muestra el contenido completo de una publicación, a detalle.
* `details/<id>/edit` permite editar una publicación.
* `delete/<id>` Borra una publicación del blog.
* `search/` nos permite buscar publicaciones palabras contenidas en titulo, subtitulo, nombre o apellido del usuario que la redactó.

Nuestras rutas principales están contenidas en **mensajeria.urls.py** y son las siguientes:

* `/` nos dirige al listado de perfiles de usuario.
* `chatRoom/profile/<id>/` nos dirige a la página de creacion un mensaje para el chat (sender).
* `chatRoom/receive` nos muestra el contenido de los mensajes recibidos en un chat (receiver).

adicional está la ruta de administración que se provee por default por Django:

* `admin/` permite entrar al ambiente de administración.

Todas las páginas están restringidas al login a través del decorador **@login_required** (`django.contrib.auth.decorators`), que obliga a estar logueado para navegar en los recursos, así que se debe iniciar sesión para acceder al contenido. Todos los sitios redirigen al **login/** y desde aquí se puede iniciar sesión o ir a la página **signup/** para registrar un nuevo usuario y poder acceder a toda la página.

>Views

A continuacion se detalla el cotenido de cada views del proyecto:

**views.py** en **users**  

*`base`: Esta función es el **home**. En este se carga el index.html que contiene los layouts básicos del sitio: navbar, footer, links a las otras funcionalidades y tiene una imagen Hero solo para decorar.

*`singup`: Esta función tiene la lógica del registro de usuarios. En primer lugar hace una validación si hay un usuario logueado (si hay alguien logueado lo lógico es que no se pueda registrar un nuevo usuario) asi que mediante `request.user.is_authenticated` se valida esto: si hay un usuario activo se redirige a **Home**, si no, se ejecuta la lógica.

Trabaja de la siguiente forma: se valida que método se está recibiendo, GET o POST; si es GET significa que se está cargando la página y renderiza a **singUp.HMTL**, enviandole un diccionario con el form proveniente de **django.contrib.auth.forms** , este es **UserCreationForm** que ya nos da la funcionalidad en Django para crear un usuario. Si por el contrario se recibe un metodo POST, es decir, se enviaron datos desde la página a través del formulario, primero se verifica si los dos password son iguales (el form UserCreationForm incluye un input para confirmar el password y realiza interno la validación), si son diferentes se envía un mensaje de error en el renderizado del la página **signup.html** para informar que los passwords no coinciden, si todo sale bien, se almacena en la base datos (**save()**), se ejecuta el login con **login()** proporcionado por **django.contrib.auth** y redirige a **home** con el usuario ya logueado (una cookie con los datos del login). Aqui se asignan los permisos iniciales para los usuarios, que son solo lectura **("can_view")** con `user.user_permissions.add` y se crea inicialmente el perfil de usuario en blanco, el usuario debe llenarlo luego en su perfil de usuario. 


*`log_out`: esta función llama a **logout()** que es proporcionado por **django.contrib.auth** para cerrar la sesión del usuario: elimina la cookie y se redirige a **Home**

*`log_in`: valida si ya hay un usuario logueado en primer lugar, si lo hay redirige a **home**; si no hay, valida el método que se está recibiendo: si es GET renderiza la vista del login **login.html** enviándole un formulario nativo de django para la autenticación (`AuthenticationForm` de **django.contrib.auth.forms**); si el método recibido es POST, se usa **authenticate()** para validar los datos enviados: si no hay usuario nos devuelve vacío; De ser vacío rederizamos otra vez la vista de **login.html** adjuntandole un error de login, si no es vacío la respuesta de **authenticate**, usamos el metodo login() para validar el usuario y hacer el login. No tiene el decorador `@login_required` por razones obvias, aqui es donde se loguea, pero tiene un decorador llamado `@never_cache` de  **django.views.decorators.cache**, esto evita que una vez que estemos logueados, le demos atrás al navegador y se vea de nuevo el menú de login.

*`Profile`: esta función renderiza simplemente la plantilla **profile.html** para que el usuario pueda ver sus datos registrados y poder escoger cambiar la contraseña y demás datos

*`edituser`: valida primero el método con el que ingresamos a la página, si es **GET** nos muestra la vista generada por el **editUserForm** (form generado a partir de **UserCreationForm** de Django) para editar email, password, nombre y apellido. Para este proyecto se consideró que el username debe ser único y no se debe cambiar. Para borrar los campos restantes, menos el password por motivos de seguridad, se deja el campo en blanco.

*`editProfile`: está basada en clase (CBV) por lo que para validar el login obligatorio usa `@method_decorator`. usando el **UpdateView** de **django.views.generic.edit** nos genera un formulario en nuestra plantilla **editprofile** para actualizar/crear avatar, bio y link y nos redirige a el mismo una vez actualizado 

*`deleteuser`: operación solo permitida a administradores, es una función que solo le sale en el frontend a usuario con el permiso **blog.can_delete**, aunque igualmente se valida en el backend con `request.user.has_perm('blog.can_delete')`; borrar el usuario filtrando por su id, usando `delete()`

*`profileIndividual`: filtra a un usuario por su **id** para que un usuario pueda ver los datos de otros usuarios registrados.

*`about`: simplemente renderiza la plantilla **about.html** del sitio, que contiene algunos datos sobre el creador de este sitio.

**views.py** en **blog**

*`createPage`: aquí primero se valida si el usuario puede crear un **post** con `request.user.has_perm`: solo usuarios con permisos de edición y borrado puede crear publicaciones, asi que si no lo tiene, se rendirige a la plantilla **pages.html** con un mensaje de error, con `messages` de `django.contrib`, colocando la categoría  **error** y un mensaje personalizado. Si el usuario tiene permiso de crear, renderiza **newpage.html**, que nos muestra el formulario para crear elpost; luego se recibe del formulario la info que viene en el método POST y la chequea con `form.is_valid()`; si se genera un error, renderiza de nuevo la plantilla **newpage.html** con un mensaje de error, referente a  los datos ingresados; si todo esta bien, redirige a **pages.html**

*`pagesListView`: Nos renderiza la página principal de las publicaciones del blog, que tiene todas las listas de publicaciones, si existieran, o un mensaje indicando que no hay ninguna. En esta funcion validamos un flag llamado "canDelete" y pregunta si el usuario tiene permiso "can_delete" y de tenerlo pone la variable en True y muestra dos opciones adicionales en la lista de publicaciones para editar y borrar directamente sobre la publicación; si un usuario es de permiso "can_edit" o "can_view" no muestra estos dos botones.

*`pageDetailView`: recibiendo el **id** de la publicación de "leer mas", nos muestra una página **pageDetails.html** con todo el detalle de la publicación: título, subtítulo, imagen y cuerpo de la publicación. En esta página salen por defecto los botones de  **editar** y **borrar** la publicación para todos los usuarios, pero solo solo accesibles por chequeo de permisos, que son hechos en otras funciones.

*`pageEdit`: primera validación de esta función es la de permisos, solo pueden editar "can_edit" y "can_delete", si la persona no tiene permisos, la regresa a "pageDetails.html" con su mensaje de error **No tienes permisos para realizar esta operación**. Si 
el usuario puede acceder, cargara en el metodo GET el sitio renderizando el **PostEditForm** con los datos almacenados en el database; mediante el método Post se envían las modificaciones, pero el cambio de imagen solo la puede hacer el administrador, es decir, usuarios con permisos "can_delete", si no tiene permiso y se intenta cambiar la imagen del post renderizará la página con un mensaje de error

*`deletePage`: verifica si el usuario tiene el permiso "can_delete", busca por **id** en el database y borra el post con **delete()**. Borrado el post redirige a **pages.html**. Si no tiene permiso, redirecciona a **pageDetails.html** con el mensaje de error. La función esta disponible en **pageDetails.html** y en los **cards** de **pages.html** solo para administradores.



>Models

Se utilizaron 3 modelos para almacenar en la base de datos, tienen el siguiente formato:

Cursos: 

```
class Curso (models.Model):
   
    curso = models.CharField(max_length=100)
    numero_cursada = models.IntegerField(unique=True)
    docente = models.ForeignKey(Profesores, null=True, blank=True, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Estudiantes, blank=True)

```
Estudiantes
```
class Estudiantes (models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    edad = models.IntegerField() 
    email = models.EmailField(max_length=100, unique=True)

```

Profesores

```
class Profesores (models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    email= models.EmailField(max_length=100, unique=True)
    profesion = models.CharField(max_length=100)

```

Aquí se definieron DNI, Mails y número de cursada como atributo **unique** para que no se permita en la DB otro dato igual (ningún alumno puede tener el mismo DNI, ningún profesor puede tener el mismo DNI, las cursadas tiene un número único)

>forms

Para los formularios se usó una clase de Django llamada ModelForm de **django.form** para cargar los formularios que se usaron en los HTML con los datos que existen en cada modelo en **models.py**, por eso en las funciones de los views.py se añaden a los renderizados de los HTML las clases de estos forms generados aquí. Se hacen a partir de los modelos:

EstudiantesForm

```
class EstudiantesForm(ModelForm):
    class Meta:
        model = Estudiantes
        fields =['name','lastname', 'dni', 'edad', 'email']

```
ProfesoresForm

```

class ProfesoresForm(ModelForm):
    class Meta:
        model = Profesores
        fields = ['name','lastname', 'dni','email','profesion' ]

```

CursosForm

```
class CursosForm(ModelForm):
    alumnos = forms.ModelMultipleChoiceField(
                        queryset=Estudiantes.objects.all().order_by('name'),
                        widget=forms.CheckboxSelectMultiple,required=False)
    class Meta:
        model = Curso
        fields = ['curso','numero_cursada', 'docente','alumnos']

```

## Funcionamiento 📜
#

Hay dos usuarios **superadmin**:

```
* usuario: luiggi_marquez
* password: Luiggi123

* usuario: admin
* password: Admin123

```
Con esto podemos entrar al panel de administración si hace falta. También podemos iniciar sesión para la aplicación web; se pueden registrar nuevos usuarios, pero estos no tienen acceso al panel de administración.

![web1](./App_1/static/images/loginreadme1.jpg)

Podemos iniciar sesión con estos usuarios o crear uno nuevo en **signup**. Todos los vínculos están protegidos y al no tener usuario logueado redireccionan al login.html (excepto singup.html y el panel de administración)

**home** solo contiene un Hero, una sección about y los vínculos para navegar en el sitio

![web2](./App_1/static/images/homereadme1.jpg)

el navbar contiene al final el link para hacer **logout**

![web3](./App_1/static/images/navbarreadme1.jpg)

**Estudiantes**

Aquí podemos agregar estudiantes en el formulario:

![web4](./App_1/static/images/estudiantesreadme1.jpg)

**Profesores**

Aquí agregamos profesores con el formulario:

![web5](./App_1/static/images/profesoresreadme1.jpg)

**Cursos**

Aquí agregaremos las cursadas:

![web6](./App_1/static/images/cursadasreadme1.jpg)

**Busquedas**

Las busquedas se realizan por el número de las cursadas:

![web7](./App_1/static/images/busquedasreadme1.jpg)

Al encontrar una se despliega debajo un card con los resultados

![web8](./App_1/static/images/busquedasreadme2.jpg)

Estan registradas cursadas 1, 2 y 3


>Otros datos

* Se usó herancia de templates, teniendo como base index.HTML y en los demás HTML se uso jinja2 para heredar navbar, footers, vínculos y para validaciones como **if** y ciclo **for**

* En App_1 esta el folder **static** que contiene el archivo css y las imágenes usadas en el favicon, readme y el Hero de la página Home.

* Se deja el archivo **requirements.txt** para replicar el entorno virtual

* Se añadieron a admin.py de App_1 los modelos para que aparezcan en el panel de administracion y puedan ser editados desde ahí.

* En setting de Preentrega_3 folder, se añadió ]`LOGIN_URL = "login"` para que las rutas protegidas se redirijan a **login** si no hay sesión 

## Autor✒️

Este proyecto fue realizado para las clases de Python de CoderHouse por:

**Ing. Luiggi Márquez** - [GitHub Profile](https://github.com/luiggimarquez) ✌️

Buenos Aires, Argentina 2023
