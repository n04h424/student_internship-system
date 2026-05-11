from django.shortcuts import render

def student_homepage(request):
    return render(request,'students/student_homepage.html')

def student_about_page(request):
    return render(request,'students/student_about_page.html')

