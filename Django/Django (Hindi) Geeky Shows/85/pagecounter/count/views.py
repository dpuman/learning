from django.shortcuts import render

# Create your views here.


def home(request):
    ct = request.session.get('count', 0)
    newCount = ct+1
    request.session['count'] = newCount
    return render(request, 'count/home.html', {'c': ct})
