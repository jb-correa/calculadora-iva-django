from django.shortcuts import redirect, render
from .models import Suma, SumaForm

def suma(request):
    form = SumaForm()
    if request.method == 'POST':
        form = SumaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suma')
    else:
        form = SumaForm()
    return render(request, 'suma/suma.html', {'form': form})
    
 