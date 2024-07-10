from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Bicycle, Profile
from django.utils.html import format_html
from .models import CarouselImage

class CuentaAdmin(admin.ModelAdmin):
    list_display = ('user', 'image_tag', 'address', 'date_of_birth', 'phone_number')
    list_filter = ('date_of_birth',)  # Filtro por fecha de nacimiento
    search_fields = ('user__username', 'address')  # Búsqueda por nombre de usuario y dirección

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)

    image_tag.short_description = 'Imagen de perfil'

admin.site.register(Bicycle)
admin.site.register(Profile, CuentaAdmin)
admin.site.register(CarouselImage)
