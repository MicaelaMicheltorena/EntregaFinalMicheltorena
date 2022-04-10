from ast import AugStore
from multiprocessing.dummy import current_process
from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
  titulo = models.CharField(max_length=50)
  subtitulo = models.CharField(max_length=50)
  cuerpo = RichTextField(blank=True, null=True)
  autor = models.CharField(max_length=50)


  
