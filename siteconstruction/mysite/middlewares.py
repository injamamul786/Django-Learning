from django.shortcuts import render

class SiteMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self,request, *args, **kwds):
        print(" Call from middleware before view")
        # response = self.get_response(request) #this go to view file
        # response = HttpResponse("page under construction") # here we can return anything like template file for Http or any thing
        response = render(request, "mysite/site.html")
        print("Call from middleware after view")
        return response