from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from models import (
    Generation
)


########################################################################################################################
# Create views
########################################################################################################################
class CreateGenerationView(CreateView):
    fields = '__all__'
    model = Generation
    template_name = 'sicpe/edit/generation.html'

    def get_success_url(self):
        return reverse('generations-list')

    def get_context_data(self, **kwargs):
        context = super(CreateGenerationView, self).get_context_data(**kwargs)
        context['action'] = reverse('generations-new')

        return context


########################################################################################################################
# Delete views
########################################################################################################################
class DeleteGenerationView(DeleteView):
    model = Generation
    template_name = 'sicpe/delete/generation.html'

    def get_success_url(self):
        return reverse('generations-list')


########################################################################################################################
# Detail views
########################################################################################################################
class GenerationView(DetailView):
    model = Generation
    template_name = 'sicpe/detail/generation.html'

    def get_absolute_url(self):
        return reverse('generations-view', kwargs={'pk': self.id})


########################################################################################################################
# List views
########################################################################################################################
class ListGenerationView(ListView):
    model = Generation
    template_name = 'sicpe/list/generation.html'


########################################################################################################################
# Update views
########################################################################################################################
class UpdateGenerationView(UpdateView):
    fields = '__all__'
    model = Generation
    template_name = 'sicpe/edit/generation.html'

    def get_success_url(self):
        return reverse('generations-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateGenerationView, self).get_context_data(**kwargs)
        context['action'] = reverse('generations-edit', kwargs={'pk': self.get_object().id})

        return context