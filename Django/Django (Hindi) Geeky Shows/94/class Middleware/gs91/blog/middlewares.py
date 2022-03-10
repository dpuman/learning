

# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One Time Initialization")

#     def __call__(self, request):
#         print('This is Before View')
#         response = self.get_response(request)
#         print("This is After View")
#         return response

# Multiple Middleware
from django.http import HttpResponse


class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Father Initialization")

    def __call__(self, request):
        print('This is Father Before View')
        response = self.get_response(request)
        print("This is Father After View")
        return response


class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mother Initialization")

    def __call__(self, request):
        print('This is Mother Before View')
        # response = self.get_response(request)
        response = HttpResponse("Response From Mother Middleware")
        print("This is Mother After View")
        return response


class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Brother Initialization")

    def __call__(self, request):
        print('This is Brother Before View')
        response = self.get_response(request)
        print("This is Brother After View")
        return response
