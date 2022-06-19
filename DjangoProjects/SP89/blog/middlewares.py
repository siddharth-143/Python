from django.http import response, HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print("This is Process View - Before View")
        # return HttpResponse("This is before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print("Exception Occured")
        class_name = exception.__class__.__name__
        print(class_name)
        msg = exception
        print(msg)
        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request) :
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Ventya'
        return response