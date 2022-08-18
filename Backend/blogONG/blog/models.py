from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='publicado')
    options=(
        ('draft', 'Draft'),
        ('publicado','Publicado'),
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publicado', null=False, unique=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    status= models.CharField(max_length=10, choices=options, default='draft') 
    objects: models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=50)
    email= models.EmailField()
    contenido = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)
    status= models.BooleanField(default=True)

    class Meta:
        ordering= ("publicado",)

        def __str__(self):
            return f"Comentario de {self.name}"



    




