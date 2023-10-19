
from django.views.generic import TemplateView

class GrantsView(TemplateView):
    template_name = 'pages/coordinator/grants.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    