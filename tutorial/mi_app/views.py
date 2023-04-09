from django.shortcuts import render
from .models import Post

# Create your views here.
def portada(request):
    posts = Post.objects.all() #Envio la información recuperada al template html con render
    return render(request, "mi_app/portada.html", {"posts": posts}) #Solo hago referencia a la carpeta creada dentro de "templates" y al archivo html

def post(request, id): #En la definición de mis URL´s indico que vendra ese "id"
    post = Post.objects.get(id = id)
    return render(request, "mi_app/post.html", {"post": post})