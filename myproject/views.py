from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Django!</h1><p>Server is running.</p>")
