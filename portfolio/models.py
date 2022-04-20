from django.db import models
from django.db.models.fields import CharField, TextField, URLField
from ckeditor.fields import RichTextField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = models.CharField('Proyecto', max_length=100)
    description = models.TextField('Descripcion', max_length=150)
    content = RichTextField('Contenido')
    image = models.ImageField('Imagen', upload_to="portfolio/images/")
    url = models.URLField('URL', blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title