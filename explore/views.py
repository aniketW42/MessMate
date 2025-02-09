from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mess_owner.models import *
from .models import *
# Create your views here.
@login_required(login_url="/accounts/login")
def explore(request):
    # names = ["Mess1", "Mess2", "Mess3", "Mess4", "Mess5", "Mess6", "Mess7", "Mess8"]
    if request.method == 'POST' and request.POST.get('city') != "Select City":
        city = request.POST.get('city')
        mess_obj = mess.objects.filter(loc=city).values_list('mess_name', 'mess_image')
    else:
        mess_obj = mess.objects.all()
    content = {"mess": mess_obj}
    return render(request, 'explore/explore.html', content)

def menu(request, pk):
    menu_obj = mess_menu.objects.filter(mess_id=pk).first()
    mess_obj = mess.objects.filter(id=pk).first()
    if not menu_obj:
        return render(request, 'menu.html', {'error': 'Menu not found', 'mess': mess_obj})
    return render(request, 'menu.html', {'menu': menu_obj,'mess': mess_obj})