from tabnanny import verbose
from django.db import models
from django.conf import settings
#
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
#categories
class Category(TimeStampedModel):
    #fields
    short_name = models.CharField(
        'Nombre Corto',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre',
        max_length=30
    )
    class Meta: 
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.name

#tag
class Tag(TimeStampedModel):
    #fields
    name = models.CharField(
        'Nombre',
        max_length=30
    )
    #meta
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
    def __str__(self):
        return self.name
#entrada
class Entry(TimeStampedModel):
    #fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Image',
        upload_to = 'Entry'
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    def __str__(self):
        return self.title
