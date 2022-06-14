from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Student
# Create your views here.


class StudentList(ListView):
    model = Student


# class StudentDetailView(DetailView):
#     model = Student

# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'school/student.html'
#     context_object_name = 'stu'
#     pk_url_kwarg = 'id'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'
    context_object_name = 'stu'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_students'] = self.model.objects.all().order_by('name')
        return context
