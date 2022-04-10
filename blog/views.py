from django.shortcuts import render,redirect
from .forms import CrearBlog, BlogBusqueda
from django.contrib.auth.decorators import login_required
from .models import Blog

@login_required 
def crear_blog(request):
  if request.method == "POST":
    formulario = CrearBlog(request.POST)
    
    if formulario.is_valid():
      data = formulario.cleaned_data
      nuevo_blog = Blog(titulo = data["titulo"], subtitulo = data["subtitulo"], cuerpo=data["cuerpo"], autor=data["autor"])
      nuevo_blog.save()
      return redirect("inicio")
    
  formulario = CrearBlog()
  return render(request, "blog/crear_blog.html" , {"formulario": formulario})

def lista_blogs(request):
    
    titulo_a_buscar = request.GET.get('titulo', None)
    
    if titulo_a_buscar is not None:
        blogs = Blog.objects.filter(titulo__icontains=titulo_a_buscar)
    else:
        blogs = Blog.objects.all()
        
    form = BlogBusqueda()
    return render(request, "blog/lista_blogs.html", {'form': form, 'blogs': blogs})
