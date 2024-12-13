from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def inventory_home(request):
    return render(request, 'inventory/inventory_home.html')
