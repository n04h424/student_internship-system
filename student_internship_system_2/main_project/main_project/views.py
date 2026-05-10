from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")