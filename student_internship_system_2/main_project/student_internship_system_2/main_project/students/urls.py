from django.urls import path
from . import views

from django.urls import path

from . import views
# go back one level and import the views.py file

urlpatterns =   [
                    path('student_homepage/',views.student_homepage),
                    # when [http://127.0.0.1:8000/students/] has [student_homepage/] after, this function is called
                    

                    path('student_about_page/',views.student_about_page)
                    # when [http://127.0.0.1:8000/students/] has [student_about_page/] after, this function is called

                   
                ]