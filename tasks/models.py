from django.db import models
from django.contrib.auth.models import User 

class Bicycle(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bicycles/')
    en_el_carrito = models.BooleanField(default=False)  # Agrega este campo si no está presente

    def __str__(self):
        return self.name
    
def user_directory_path(instance, filename):
    # Define la ruta de almacenamiento para las imágenes de perfil de usuario
    return f'profile_images/user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, default='default.jpg')
    address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    
    def __str__(self):
        return f'Profile of {self.user.username}'
    
class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or str(self.image)
