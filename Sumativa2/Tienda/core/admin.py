from django.contrib import admin
from .models import Juegos, Usuario, Perfil, UserProfile


class ProductoAdmin(admin.ModelAdmin):
    list_display= ['id', 'nombre', 'precio', 'cantidad', 'imagen']
    list_editable= ['precio']
    search_fields= ['nombre']
    list_per_page= 5

# Register your models here.   
admin.site.register(Juegos, ProductoAdmin)
admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(UserProfile)