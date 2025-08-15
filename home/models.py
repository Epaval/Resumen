from django.db import models
# apps terceros
from model_utils.models import TimeStampedModel

# Create your models here.
class Home(TimeStampedModel):
    """MOdelo de la Pagina Principal"""
    
    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono de Contacto',
        max_length=11
    )
    
    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'
    
    def __str__(self):
        return self.title
    
class Suscribers(TimeStampedModel):
    """Suscripciones"""
    
    email = models.EmailField()
    
    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
    def __str__(self):
        return self.email    
    
class Contact(TimeStampedModel):
    """Formulario de Contacto"""
    
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        return self.full_name   
        
       
   
    
    
        
        
         
    
    