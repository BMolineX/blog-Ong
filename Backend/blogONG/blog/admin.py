from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'id','status','slug','autor')
    prepopulated_fields= {'slug': ('titulo',), }



@admin.register(models.Comentarios)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('post', 'nombre','email','publicado','status')
    list_filter= ('status','publicado')
    search_fields= ('nombre', 'email', 'contenido')


admin.site.register(models.Categoria)

