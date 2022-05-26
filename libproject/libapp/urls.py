from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('books', views.allbooks, name= 'books'),
    path('teacher_login',views.teach, name='teacher_login'),
    path('student_login',views.student, name='student_login'),

    path('remove', views.removebooks, name='remove'),
    path('remove/<int:bkid>', views.removebooks, name='remove'),
    path('filter', views.filterbooks, name='filter'),
    path('addbooks', views.addbooks, name='addbooks'),
    path('allstudent', views.allstudent, name='allstudent'),
    path('allteacher', views.allteacher, name='allteacher'),
]
