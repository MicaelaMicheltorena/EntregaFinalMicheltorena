from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.lista_blogs, name="blogs"),
    path("crear-blog/", views.crear_blog, name="crear_blog"),
    path('blog/<int:pk>', views.DetalleBlog.as_view(), name="detalle_blog"),
    path('blog/<int:pk>/editar', views.EditarBlog.as_view(), name="actualizar_blog"),
    path('blog/<int:pk>/borrar', views.BorrarBlog.as_view(), name="borrar_blog"),
]