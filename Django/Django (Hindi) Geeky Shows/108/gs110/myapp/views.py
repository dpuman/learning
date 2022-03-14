from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class ClassView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')

##########################################


class MyView(View):
    name = 'Dipu'

    def get(self, request):
        return HttpResponse(self.name)


class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
