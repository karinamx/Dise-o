from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después del registro
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})
