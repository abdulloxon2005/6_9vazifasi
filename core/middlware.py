from django.http import HttpResponseForbidden,HttpRequest
class LogMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request:HttpRequest):
        print("viewdan oldingi kod")
        if request.path =="/salom":
            return HttpResponseForbidden(  )
        return HttpResponseForbidden()
        response = self.get_response(request)
        print("viewdan keyingi kod")

        return response