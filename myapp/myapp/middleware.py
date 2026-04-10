from django.urls import reverse
from django.shortcuts import redirect
class RedirectAuthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            paths_to_redirect = [reverse('blog:register'),reverse('blog:login')]
            
            if request.path in paths_to_redirect:
                return redirect('blog:index')
        
        response = self.get_response(request)
        return response

class RestrictUnauthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        paths_to_restirct = [reverse('blog:dashboard')]
        if not request.user.is_authenticated:
            if request.path in paths_to_restirct:
                return redirect('blog:login')
        
        response = self.get_response(request)
        return response
    
