from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def maintenance_home(request):
    return render(request, 'maintenance/maintenance_home.html')
