from django.shortcuts import HttpResponse

class BrotherMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
        print("one time execute Brother Middleware")

    def __call__(self, request):
        print("This is before view Brother Middleware")
        """anything hear any function variable anything this run before view run"""
        responce = self.get_responce(request)
        """Anything hear run after view"""
        print("This is after view Brother Middleware")
        return responce

class FatherMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
        print("one time execute Father Middleware")

    def __call__(self, request):
        print("This is before view Father Middleware")
        """anything hear any function variable anything this run before view run"""
        responce = self.get_responce(request)
        # responce = HttpResponse('Go Back from Father Middleware') 

        """Anything hear run after view"""
        print("This is after view Father Middleware")
        return responce
    
class AmmiMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
        print("one time execute Ammi Middleware")

    def __call__(self, request):
        print("This is before view Ammi Middleware")
        """anything hear any function variable anything this run before view run"""
        responce = self.get_responce(request)
        """Anything hear run after view"""
        print("This is after view Ammi Middleware")
        return responce