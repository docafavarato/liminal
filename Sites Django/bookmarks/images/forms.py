from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image
from urllib import request

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('A URL não é permitida. Apenas jpg, jpeg e png.')
        
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        
        # Baixar a imagem
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        
        if commit:
            image.save()
        return image