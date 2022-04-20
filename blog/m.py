from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
import datetime


class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField("Nombre", max_length = 100)
    last_name = models.CharField("Apellido", max_length = 100)
    email = models.EmailField("Correo", max_length = 100)
    status = models.BooleanField("Activo/Inactivo", default = True)
    date_created = models.DateField("Fecha de alta", auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"Autor: {self.name} {self.last_name}"


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField("Titulo", max_length = 100, blank = False, null = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    description = models.CharField(
        "Descripcion", max_length = 150, blank = False, null = False
    )
    content = RichTextField()
    image = models.ImageField("Imagen", upload_to = 'blog/images')
    date_posted = models.DateField("Fecha de creacion", datetime.date.today)
    status = models.BooleanField("Publicado/No publicado", default = True)
    slug = models.SlugField(
        "Slug", max_length = 100, unique = True, blank = False, null = False
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title