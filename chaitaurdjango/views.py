from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>welcome home</h1>")
def about(request):
    return HttpResponse("<h1>Welcome to Django Project: About page</h1>")
