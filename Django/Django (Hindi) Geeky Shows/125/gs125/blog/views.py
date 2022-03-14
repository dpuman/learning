from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.


def home(request):

    all_blog = Blog.objects.all().order_by('id')
    paginator = Paginator(all_blog, 3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'blogs': page_obj})
