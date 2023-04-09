from django.db import models

#Create your models here. Son clases que permiten definir la estructura de los datos para la base de datos de DJango
#Estos datos Djando los mapeara a objetos
#Deben de crearse("pipenv run python manage.py makemigrations") y ademas aplicarlas("pipenv run python manage.py migrate")
#Una vez los pasos anteriores puedo abrir con SQLite la base de datos que tiene este proyecto y ver lo que he realizado
class Post(models.Model):
    titulo     = models.CharField(max_length = 200, verbose_name = "Título")
    contenido  = models.TextField(verbose_name = "Contenido")
    creacion   = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    modificado = models.DateTimeField(auto_now = True, verbose_name = "Fecha de modificación")

    def __str__(self): #Para que en el panel no nos muestre el por defecto
        return self.titulo

    class Meta: #Para también traducir el "Post" en mi panel de administrador Django
        verbose_name        = "entrada"
        verbose_name_plural = "entradas"

#Cada que hago cambios en mi modelo("Post()") debo crear y aplicar la migración para que quede registrado en la carpeta "migrations"
#Para ejecutar la migración solo en mi APP creada es con("pipenv run python manage.py makemigrations nombre_app")
#Lo mismo con las migraciones, puedo indicar el nombre de la APP


""" Para crear un super usuario se usa 'pipenv run python manage.py createsuperuser' En este caso cree(admin-admin) para probar
Ahora podere acceder a la URL /admin que nos da DJango"""

""" Para entrar a la shell de DJango 'pipenv run python manage.py shell' """