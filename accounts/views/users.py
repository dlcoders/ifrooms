from django.views.generic import TemplateView

class UsersView(TemplateView):
    template_name = 'pages/admin/users.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    