from django.views.generic import TemplateView
from .models import Medico

class IndexView(TemplateView):
    template_name = 'index.html'

class SobreView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        context['medicos'] = Medico.objects.order_by('nome').all()
        return context


