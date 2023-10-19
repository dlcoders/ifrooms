from django.shortcuts import render
from rooms.models import Room

def calendar_view(request):
    
    salas = Room.objects.all()
   
    print("TESTE:", salas)
    filtro_texto = request.GET.get('filtro_texto')
    filtro_sala = request.GET.get('filtro_sala')

    if filtro_texto:
        salas = salas.filter(sala__icontains=filtro_texto)
        
    if filtro_sala:
        salas = salas.filter(id=filtro_sala)

    escolhas_predio = Room.CHOICES_PREDIO

    return render(request, 'dashboard.html', {'salas': salas, 'escolhas_predio': escolhas_predio})
