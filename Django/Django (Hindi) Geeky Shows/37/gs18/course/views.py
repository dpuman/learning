from django.shortcuts import render

# Create your views here.


def courseInfo(request):
    return render(request, 'course/course-info.html')
