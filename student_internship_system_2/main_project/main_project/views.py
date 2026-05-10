from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')
    # when this function is called, go back one level, look for templates, and render 'homepage.html'

def about(request):
    return render(request,'about.html')
    # when this function is called, go back one level, look for templates, and render 'about.html'