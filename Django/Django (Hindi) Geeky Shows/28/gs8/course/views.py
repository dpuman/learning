from django.shortcuts import render
from datetime import datetime
# Create your views here.


def myCourse(request):
    cName = 'Django'
    price = 1250
    rating = 5
    context = {
        'Cname': cName,
        'price': price,
        'rating': rating
    }
    return render(request, 'course/course-one.html', context)


def myFilter(request):
    d = datetime.now()
    context = {
        'text': 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of',
        'nothing': False,
        'dt': d,
        'f': 123.5478,
        'f1': 254.000,
        'f2': 458.240,
    }
    return render(request, 'course/filters.html', context)


def myTagFilter(request):
    student = {
        'stu1': {'name': 'Dipu', 'Roll': 10245},
        'stu2': {'name': 'Apu', 'Roll': 2548},
        'stu3': {'name': 'Topu', 'Roll': 3654},
    }
    names = ['dipu', 'opu', 'topu']
    context = {
        'nm': "Django",
        'st': 5,
        'check': True,
        'stu': student,
        'names': names,
        'empty': []


    }

    return render(request, 'course/tag-filter.html', context)
