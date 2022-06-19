from django.http import response


class MyMiddleware:
    def __init__(self, get_response) :
        self.get_response = get_response
        print("One time initializations")

    def __call__(self, requset):
        print("This is before view")
        response = self.get_response(requset)
        print("This is after view")
        return response