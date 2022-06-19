def my_middleware(get_response):
    print("One time intializations")
    
    def my_function(request):
        print("This is before views")
        response = get_response(request)
        print("This is after views")
        return response
    return my_function