from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mess_owner.models import mess
# Create your views here.
def home(request):
    return render(request,'home/home.html')


