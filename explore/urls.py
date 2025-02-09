from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.explore, name='home'),
    path('menu/<int:pk>', views.menu, name='/explore/menu')
    
]
