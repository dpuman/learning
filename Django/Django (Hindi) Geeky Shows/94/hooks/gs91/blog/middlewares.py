

from django.http import HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_view(request, *args, **kwargs):
        # return HttpResponse('This is From Process View')
        return None


class MyProcessExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        msg = exception
        className = exception.__class__.__name__
        print(msg, className)
        return HttpResponse(msg)


class MyProcessTemplateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Dipankar'

        return response
