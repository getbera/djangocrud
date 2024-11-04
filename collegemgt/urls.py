# collegemgt/urls.py
from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student.urls')),  
    path('api/v1/', include('student.api_urls')),
]



