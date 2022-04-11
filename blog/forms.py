from django import forms
from ckeditor.fields import RichTextFormField

class CrearBlog(forms.Form):
  titulo = forms.CharField(max_length=200)
  subtitulo = RichTextFormField(required=True)
  cuerpo = RichTextFormField(required=False)
  autor = RichTextFormField(required=True)
  fecha = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')
  imagen = forms.ImageField(required=False)
  
  
class BlogBusqueda(forms.Form):
    titulo = forms.CharField(max_length=210)