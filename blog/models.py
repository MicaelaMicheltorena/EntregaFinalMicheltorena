from ast import AugStore
from multiprocessing.dummy import current_process
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Blog(models.Model):
  titulo = models.CharField(max_length=200)
  subtitulo = RichTextField(blank=False)
  cuerpo = RichTextField(blank=True, null=True)
  autor = RichTextField(blank=False)
  fecha = models.DateTimeField(default=timezone.now)
  imagen = models.ImageField(upload_to='imagen', blank=True, null=True, )
  
  def __str__(self):
    return "Blog:"
    # return f"{self.titulo}, Autor:{self.autor}"
    