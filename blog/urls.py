from django.urls import path 
from .views import crear_blog, lista_blogs

urlpatterns = [
    path("blogs/", lista_blogs, name="blogs"),
    path("crear-blog/", crear_blog, name="crear_blog"),
]