# urls.py
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('cart/', views.cart, name='cart'),  # Actualiza la importación y agrega la URL para la vista del carrito de compras
    path('add_to_cart/<int:bicycle_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:bicycle_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('perfil/', views.perfil, name='perfil'),
    path('editPerfil/', views.edit_perfil, name='editPerfil'),
    path('teamowawa/', views.teamowawa, name='teamowawa'),
    path('upload/', views.upload_image, name='upload_image'),


















] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

