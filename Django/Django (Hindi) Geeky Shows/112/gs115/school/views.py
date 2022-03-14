from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.


class StudentList(ListView):
    model = Student
    # template_name_suffix = '_get'
    ordering = ['name']
    context_object_name = 'students'
    template_name = 'school/student.html'

    # Filter queryset
    def get_queryset(self):
        return Student.objects.filter(course='Python')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['freashers'] = Student.objects.all().order_by('roll')
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'dipu':
    #         template_name = 'school/dipu.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]

    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'school/superuser.html'
        elif self.request.user.is_staff:
            template_name = 'school/stuff.html'
        else:
            template_name = self.template_name
        return [template_name]
