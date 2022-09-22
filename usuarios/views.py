from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def novo_usuario(request):
    # saber o tipo de requisição, validar, informar e salvar
    if request.method == 'POST': # saber o tipo
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid(): # validar
            formulario.save() # salvar
            usuario = formulario.cleaned_data.get('username') 
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!') # informar
            return redirect('login')
    else: # se não for POST
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': formulario})
