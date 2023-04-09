from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificado') #Para mostrar en el panel mis campos "DateTimeField" del modelo como lectura
    list_display    = ('titulo', 'creacion', 'modificado') #Campos de columnas que quiero mostrar en la lista de "entradas" del panel DJango
    date_hierarchy  = 'creacion'   #Para filtar en función de las fechas


# Register your models here.
admin.site.register(Post, PostAdmin)   #Para registrar el modelo antes creado en mi panel de administración DJango, también puedo poner decorador en lugar de esta linea