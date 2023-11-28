from django.shortcuts import render
from django.urls import reverse_lazy
from apps.rooms.models import Room
from .forms import RoomForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


def calendar_view(request):
    salas = Room.objects.all()

    filtro_texto = request.GET.get("filtro_texto")
    filtro_sala = request.GET.get("filtro_sala")

    if filtro_texto:
        salas = salas.filter(sala__icontains=filtro_texto)

    if filtro_sala:
        salas = salas.filter(id=filtro_sala)

    escolhas_predio = Room.CHOICES_PREDIO

    return render(
        request,
        "pages/dashboard.html",
        {"salas": salas, "escolhas_predio": escolhas_predio},
    )

class RoomsListView(ListView):
    model = Room
    template_name = 'rooms/rooms_list.html'
    context_object_name = 'rooms'  # Nome da variável a ser usada no template
    # paginate_by = 2
    
class RoomsCreateView(CreateView):
    template_name = 'rooms/rooms_form.html'
    form_class = RoomForm
    success_url =reverse_lazy('room:rooms_list')
    
class RoomsUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'rooms/rooms_form.html'
    pk_url_kwarg = 'id' # Nome da variável na URL
    
    def get_success_url(self):
        return reverse_lazy('room:rooms_list')

class RoomsDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('room:rooms_list')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class RoomsDetailView(DetailView):
    model = Room