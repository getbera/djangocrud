# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .stu_form import StudentForm
from django.http import HttpResponse
from .models import Student

from django.contrib.auth.models import User  # tis id for API
from rest_framework import viewsets  #   this is for the API  
from student.serializers import StudentSerializer  # this is for API
#
class Studentviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# # for View 
# from .models import Student_T

# from django.contrib.auth.models import User  # tis id for API
# from rest_framework import viewsets  #   this is for the API  
# from student.serializers import StudentSerializer  # this is for API
# #
# class Studentviewset(viewsets.ModelViewSet):
#     queryset = Student_T.objects.all()
#     serializer_class = StudentSerializer















# Create
def create_student(request):
    if request.method == 'POST':
        s_name=request.POST['name']
        s_age=int(request.POST['age'])
        s_gender=request.POST['gender']
        s_email=request.POST['email']

        if s_age > 20 or s_age < 7:
            return HttpResponse("error, student age is b/n 7 and 20")
        else:
           new_student = Student(name=s_name,age=s_age,gender=s_gender,email=s_email)
           new_student.save()
           return redirect('list_students')
    #     form = StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('list_students')
    # else:
    #     form = StudentForm()
    # return render(request, 'students/create_student.html', {'form': form})
    return render(request, 'students/create_student.html')

# Read
def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

# Update
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update_student.html', {'form': form, 'student': student})

# def update_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)

#     if request.method == 'POST':
#         s_name = request.POST['name']
#         s_age = int(request.POST['age'])
#         s_gender = request.POST['gender']
#         s_email = request.POST['email']

#         if s_age > 20 or s_age < 7:
#             return HttpResponse("Error: student age must be between 7 and 20.")
#         else:
#             # Update student instance directly
#             student.name = s_name
#             student.age = s_age
#             student.gender = s_gender
#             student.email = s_email
#             student.save()
#             return redirect('list_students')
    
#     return render(request, 'students/update_student.html', {'student': student})

# Delete
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'students/delete_student.html', {'student': student})
