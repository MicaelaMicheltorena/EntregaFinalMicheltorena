from django import forms
from ckeditor.fields import RichTextFormField

class CrearBlog(forms.Form):
  titulo = RichTextFormField(max_length=50)
  subtitulo = RichTextFormField(max_length=50)
  cuerpo = RichTextFormField(required=False)
  autor = RichTextFormField(max_length=50)
  fecha = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')
  imagen = forms.ImageField(required=False)
  
  
class BlogBusqueda(forms.Form):
    titulo = forms.CharField(max_length=20)