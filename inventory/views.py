from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InventoryItem
from .forms import InventoryItemForm

@login_required
def inventory_dashboard(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_dashboard')
        else:
            print(form.errors)  # Muestra errores en la consola si el formulario no es válido
    else:
        form = InventoryItemForm()

    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_dashboard.html', {'form': form, 'items': items})
