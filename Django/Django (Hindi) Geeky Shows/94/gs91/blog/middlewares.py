def my_middleware(get_response):
    print('One Time Initialization Codes')

    def my_function(request):
        print('This is Before view')
        response = get_response(request)
        print('This is After View')
        return response
    return my_function
