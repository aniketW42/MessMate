from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from accounts.models import MessmateUser
from explore.models import mess_menu

from . models import mess
# Create your views here.
def register_mess(request):
    if request.method =='POST':
        mess_name = request.POST.get('mess_name')
        owner_name = request.POST.get('owner_name')
        loc = request.POST.get('address')
        mess_image = request.FILES.get('mess-image')
        if mess.objects.filter(mess_name=mess_name).exists():
            messages.warning(request, 'Mess name already exists, try using different mess name')
        else:
            if request.user.is_authenticated:
                mess.objects.create(user_id = request.user,  mess_name= mess_name, mess_owner_name = owner_name, loc = loc, mess_image = mess_image)
            else:
                messages.error(request, 'You need to be logged in to register a mess')
                return redirect('login')
            user = MessmateUser.objects.filter( username = request.user.username ).first()
            user.is_mess_owner = True
            user.save()
            messages.success(request, 'Mess registered successfully')
            # return redirect('/')

    return render(request,'register_mess.html')

def mess_owner_dashboard(request):

    if request.method == 'POST':
        menu = request.POST.get('menu-text')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        mess_obj = mess.objects.filter(user_id=request.user).first()
        menu_obj = mess_menu.objects.filter(mess_id = mess_obj).first()
        if menu_obj is None:
            mess_menu.objects.create(mess_id = mess_obj, menu = menu, from_time = from_time, to_time = to_time)
        else:
            menu_obj.menu = menu
            menu_obj.from_time = from_time
            menu_obj.to_time = to_time
            menu_obj.save()
        messages.success(request, 'Menu added successfully')
        return redirect('/dashboard')

    mess_obj = mess.objects.filter(user_id=request.user).first()
    menu_obj = mess_menu.objects.filter(mess_id = mess_obj).first()
    if menu_obj is None:
        menu_obj = 'No menu available'
     
    return render(request, 'dashboard.html' , {'mess': mess_obj , 'menu': menu_obj})