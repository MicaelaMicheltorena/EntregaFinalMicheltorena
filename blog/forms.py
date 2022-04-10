from django import forms
from ckeditor.fields import RichTextFormField

class CrearBlog(forms.Form):
  titulo = forms.CharField(max_length=50)
  subtitulo = forms.CharField(max_length=50)
  cuerpo = RichTextFormField(required=False)
  autor = forms.CharField(max_length=50)
  
  
class BlogBusqueda(forms.Form):
    titulo = forms.CharField(max_length=20)