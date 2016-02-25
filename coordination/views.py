from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from models import (
    Career,
    Classroom,
    Generation,
    Professor,
    Student,
)


########################################################################################################################
# Create views
########################################################################################################################
class CreateCareerView(CreateView):
    fields = '__all__'
    model = Career
    template_name = 'sicpe/edit/career.html'

    def get_success_url(self):
        return reverse('careers-list')

    def get_context_data(self, **kwargs):
        context = super(CreateCareerView, self).get_context_data(**kwargs)
        context['action'] = reverse('careers-new')

        return context


class CreateClassroomView(CreateView):
    fields = '__all__'
    model = Classroom
    template_name = 'sicpe/edit/classroom.html'

    def get_success_url(self):
        return reverse('classrooms-list')

    def get_context_data(self, **kwargs):
        context = super(CreateClassroomView, self).get_context_data(**kwargs)
        context['action'] = reverse('classrooms-new')

        return context


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


class CreateProfessorView(CreateView):
    fields = '__all__'
    model = Professor
    template_name = 'sicpe/edit/professor.html'

    def get_success_url(self):
        return reverse('professors-list')

    def get_context_data(self, **kwargs):
        context = super(CreateProfessorView, self).get_context_data(**kwargs)
        context['action'] = reverse('professors-new')

        return context


class CreateStudentView(CreateView):
    fields = '__all__'
    model = Student
    template_name = 'sicpe/edit/student.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        context['action'] = reverse('students-new')

        return context


########################################################################################################################
# Delete views
########################################################################################################################
class DeleteCareerView(DeleteView):
    model = Career
    template_name = 'sicpe/delete/career.html'

    def get_success_url(self):
        return reverse('careers-list')


class DeleteClassroomView(DeleteView):
    model = Generation
    template_name = 'sicpe/delete/classroom.html'

    def get_success_url(self):
        return reverse('classrooms-list')


class DeleteGenerationView(DeleteView):
    model = Generation
    template_name = 'sicpe/delete/generation.html'

    def get_success_url(self):
        return reverse('generations-list')


class DeleteProfessorView(DeleteView):
    model = Professor
    template_name = 'sicpe/delete/professor.html'

    def get_success_url(self):
        return reverse('professors-list')


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'sicpe/delete/student.html'

    def get_success_url(self):
        return reverse('students-list')


########################################################################################################################
# Detail views
########################################################################################################################
class CareerView(DetailView):
    model = Career
    template_name = 'sicpe/detail/career.html'

    def get_absolute_url(self):
        return reverse('careers-view', kwargs={'pk': self.id})


class ClassroomView(DetailView):
    model = Classroom
    template_name = 'sicpe/detail/classroom.html'

    def get_absolute_url(self):
        return reverse('classrooms-view', kwargs={'pk': self.id})


class GenerationView(DetailView):
    model = Generation
    template_name = 'sicpe/detail/generation.html'

    def get_absolute_url(self):
        return reverse('generations-view', kwargs={'pk': self.id})


class ProfessorView(DetailView):
    model = Professor
    template_name = 'sicpe/detail/professor.html'

    def get_absolute_url(self):
        return reverse('professors-view', kwargs={'pk': self.employee_number})


class StudentView(DetailView):
    model = Student
    template_name = 'sicpe/detail/student.html'

    def get_absolute_url(self):
        return reverse('students-view', kwargs={'pk': self.registration_number})


########################################################################################################################
# List views
########################################################################################################################
class ListCareerView(ListView):
    model = Career
    template_name = 'sicpe/list/career.html'


class ListClassroomView(ListView):
    model = Classroom
    template_name = 'sicpe/list/classroom.html'


class ListGenerationView(ListView):
    model = Generation
    template_name = 'sicpe/list/generation.html'


class ListProfessorView(ListView):
    model = Professor
    template_name = 'sicpe/list/professor.html'


class ListStudentView(ListView):
    model = Student
    template_name = 'sicpe/list/student.html'


########################################################################################################################
# Update views
########################################################################################################################
class UpdateCareerView(UpdateView):
    fields = '__all__'
    model = Career
    template_name = 'sicpe/edit/career.html'

    def get_success_url(self):
        return reverse('careers-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCareerView, self).get_context_data(**kwargs)
        context['action'] = reverse('careers-edit', kwargs={'pk': self.get_object().id})

        return context


class UpdateClassroomView(UpdateView):
    fields = '__all__'
    model = Classroom
    template_name = 'sicpe/edit/classroom.html'

    def get_success_url(self):
        return reverse('classrooms-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateClassroomView, self).get_context_data(**kwargs)
        context['action'] = reverse('classrooms-edit', kwargs={'pk': self.get_object().id})

        return context


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


class UpdateProfessorView(UpdateView):
    fields = '__all__'
    model = Professor
    template_name = 'sicpe/edit/professor.html'

    def get_success_url(self):
        return reverse('professors-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfessorView, self).get_context_data(**kwargs)
        context['action'] = reverse('professors-edit', kwargs={'pk': self.get_object().registration_number})

        return context


class UpdateStudentView(UpdateView):
    fields = '__all__'
    model = Student
    template_name = 'sicpe/edit/student.html'

    def get_success_url(self):
        return reverse('students-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        context['action'] = reverse('students-edit', kwargs={'pk': self.get_object().registration_number})

        return context
