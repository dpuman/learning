from django.shortcuts import render

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
