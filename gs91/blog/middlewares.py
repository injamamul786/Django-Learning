# def my_middleware(get_responce):
#     print("one time initialization")
#     def my_function(request):
#         print("This is before view")
#         """anything hear any function variable anything this run before view run"""
#         responce = get_responce(request)
#         """Anything hear run after view"""
#         print("This is after view")
#         return responce
#     return my_function

class MyMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
        print("one time execute Class Middleware")

    def __call__(self, request):
        print("This is before view")
        """anything hear any function variable anything this run before view run"""
        responce = self.get_responce(request)
        """Anything hear run after view"""
        print("This is after view")
        return responce
