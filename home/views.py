import datetime
#
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import re

from django.views.generic import (
    TemplateView,
    CreateView
)
# apps de entrada
from entrada.models import Entry
# Models
from .models import Home, Contact 
# forms
from .forms import Suscribers, SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)          
        # contexto de la portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # contexto para los articulos en el home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        context["form"] = SuscribersForm
        return context
    

def Add_suscription(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()

        # Validación básica de email
        if not email:
            messages.error(request, 'El correo es obligatorio.')
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.error(request, 'Correo inválido.')
        else:
            # Verificar si ya existe
            obj, created = Suscribers.objects.get_or_create(email=email)
            if created:
                messages.success(request, '¡Gracias por suscribirte!')
            else:
                messages.error(request, 'Ya estás suscrito.')

        # Redirigir para evitar reenvío del formulario
        return redirect('/')  # ← nombre de tu URL de inicio

    # Si no es POST, redirige o maneja según necesites
    return redirect('/')


# views.py
def Add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado!')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return redirect('/')
    return redirect('/')
   
