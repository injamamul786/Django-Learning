from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
       

    def __call__(self, request):
        responce = self.get_responce(request)
        return responce

    def process_view(request, *args, **kwargs):
        print("This is process view befoer view")
        # return HttpResponse("This is before view")
        return None 


class MyExceptionMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
       

    def __call__(self, request):
        responce = self.get_responce(request)
        return responce

    def process_exception(self, request, exception):
        print("This is exception process execute when exception method of veiew excute")
        class_name= exception.__class__.__name__
        print(class_name)
        return HttpResponse(exception)
        

class MyTemplateResponseMiddleware:
    def __init__(self, get_responce) -> None:
        self.get_responce = get_responce
       

    def __call__(self, request):
        responce = self.get_responce(request)
        return responce

    def process_template_response(self, request, response):
        print("This is template response process execute when user_info method of veiew excute")
        response.context_data['name'] = 'Imran'
        return response