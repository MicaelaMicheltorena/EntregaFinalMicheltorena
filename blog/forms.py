from django import forms
from ckeditor.fields import RichTextFormField

class CrearBlog(forms.Form):
  titulo = forms.CharField(max_length=200)
  subtitulo = RichTextFormField(required=True)
  cuerpo = RichTextFormField(required=False)
  autor = RichTextFormField(required=True)
  imagen = forms.ImageField(required=False)
  
  
class BlogBusqueda(forms.Form):
    titulo = forms.CharField(max_length=210)
    

class BlogFormulario(forms.Form):
  titulo = forms.CharField(max_length=200)
  subtitulo = RichTextFormField(required=False)
  cuerpo = RichTextFormField(required=False)
  autor = RichTextFormField(required=False)
  imagen = forms.ImageField(required=False )