from ast import AugStore
from multiprocessing.dummy import current_process
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Blog(models.Model):
  titulo = RichTextField(max_length=50)
  subtitulo = RichTextField(max_length=50)
  cuerpo = RichTextField(blank=True, null=True)
  autor = RichTextField(max_length=50)
  fecha = models.DateTimeField(default=timezone.now)
  imagen = models.ImageField(upload_to='imagen', blank=True, null=True, )
  
  def __str__(self):
    return f'{self.titulo}'
    