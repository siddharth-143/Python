from django.http import response, HttpResponse


class BrotherMiddleware:
    def __init__(self, get_response) :
        self.get_response = get_response
        print("One time Brother initializations")

    def __call__(self, requset):
        print("This is Brother before view")
        response = self.get_response(requset)
        print("This is Brother after view")
        return response


class FatherMiddleware:
    def __init__(self, get_response) :
        self.get_response = get_response
        print("One time Father initializations")

    def __call__(self, requset):
        print("This is Father before view")
        response = self.get_response(requset)
        # response = HttpResponse("Nikl Lo")
        print("This is Father after view")
        return response

class MotherMiddleware:
    def __init__(self, get_response) :
        self.get_response = get_response
        print("One time Mother initializations")

    def __call__(self, requset):
        print("This is Mother before view")
        response = self.get_response(requset)
        print("This is Mother after view")
        return response