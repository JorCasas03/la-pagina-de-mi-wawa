from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import CarouselImage

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=100, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'address', 'date_of_birth', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # Asegúrate de inicializar los datos del usuario y perfil si ya existen
        if self.instance.user:
            self.initial['email'] = self.instance.user.email
            self.initial['first_name'] = self.instance.user.first_name
            self.initial['last_name'] = self.instance.user.last_name
            self.initial['address'] = self.instance.address or ''  # Asigna cadena vacía si es None
            self.initial['date_of_birth'] = self.instance.date_of_birth or None  # Deja None si es None
            self.initial['phone_number'] = self.instance.phone_number or ''  # Asigna cadena vacía si es None

    def save(self, commit=True):
        # Guarda los datos del perfil y usuario
        profile = super(EditProfileForm, self).save(commit=False)
        if commit:
            profile.save()
            self.instance.user.first_name = self.cleaned_data['first_name']
            self.instance.user.last_name = self.cleaned_data['last_name']
            self.instance.user.save()
            profile.address = self.cleaned_data['address']
            profile.date_of_birth = self.cleaned_data['date_of_birth']
            profile.phone_number = self.cleaned_data['phone_number']
            profile.save()
        return profile
    
class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image', 'description']
