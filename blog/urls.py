from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_blogs, name="blogs"),
    path("create/", views.crear_blog, name="crear_blog"),
    path('<int:pk>', views.DetalleBlog.as_view(), name="detalle_blog"),
    path('<int:pk>/update', views.EditarBlog.as_view(), name="actualizar_blog"),
    path('<int:pk>/delete', views.BorrarBlog.as_view(), name="borrar_blog"),
]