# students/urls.py
from django.urls import path
from .views import create_student, list_students, update_student, delete_student

urlpatterns = [
    path('add/', create_student, name='create_student'),
    path('', list_students, name='list_students'),  # The list view at 'students/' URL
    path('update/<int:student_id>/', update_student, name='update_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
]
