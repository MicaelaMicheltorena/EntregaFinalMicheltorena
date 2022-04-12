from django.shortcuts import render,redirect
from .forms import CrearBlog, BlogBusqueda, BlogFormulario
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


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

class DetalleBlog(DetailView):
    model = Blog
    template_name = "blog/detalle_blog.html"


class BorrarBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"
    success_url = "/pages/"


@login_required
def actualizar_blog(request, id):
    
    blog = Blog.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = BlogFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            blog.titulo = data['titulo']
            blog.subtitulo = data['subtitulo']
            blog.cuerpo = data['cuerpo']
            blog.autor = data['autor']
            blog.imagen = data['imagen']
            blog.save()

            return redirect('blogs')
            
    formulario = BlogFormulario(initial={
        'titulo' : blog.titulo,
        'subtitulo' : blog.subtitulo, 
        'cuerpo' : blog.cuerpo,
        'autor' : blog.autor,
        'imagen' : blog.imagen,
    })
    return render(request, 'blog/blog_update.html', {'formulario': formulario, 'blog': blog})      