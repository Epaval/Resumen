from django import forms

# models
from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):
    class Meta:
        model = Suscribers
        fields = (
            'email',
        )
        
# applications/home/forms.py
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']  # ← "message"   