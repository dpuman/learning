from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.


class MyYoutubeReddirect(RedirectView):
    url = 'http://www.youtube.com'


class MyRedirectView(RedirectView):
    # url = '/'
    pattern_name = 'newInfo'
    permanent = True
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        print('Something')
        kwargs['info'] = 'Dipu'
        return super().get_redirect_url(*args, **kwargs)
