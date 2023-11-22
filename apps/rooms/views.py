from django.shortcuts import render
from apps.rooms.models import Room

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

class CoordinatorCreateRoomFormView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = 'pages/coordinator/forms/form_room.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    

# Gerenciar Salas
class RoomsView(TemplateView):
    template_name = 'pages/coordinator/rooms.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    

def calendar_view(request):
    
    salas = Room.objects.all()
   
    filtro_texto = request.GET.get('filtro_texto')
    filtro_sala = request.GET.get('filtro_sala')

    if filtro_texto:
        salas = salas.filter(sala__icontains=filtro_texto)
        
    if filtro_sala:
        salas = salas.filter(id=filtro_sala)

    escolhas_predio = Room.CHOICES_PREDIO

    return render(request, 'pages/dashboard.html', {'salas': salas, 'escolhas_predio': escolhas_predio})
