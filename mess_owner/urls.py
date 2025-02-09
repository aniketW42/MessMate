from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-mess/', views.register_mess, name='home'),   
    
]
