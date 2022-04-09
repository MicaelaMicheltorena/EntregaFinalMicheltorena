from django.shortcuts import render, redirect
from accounts.forms import NuestraCreacionUser
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import NuestraCreacionUser, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension

# Create your views here.


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)    
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return render(request, 'indice/index.html', {'msj': f'Iniciaste sesión correctamente con el usuario: {username}'})
            else:
                return render(request, 'accounts/login.html', {'form': form, 'msj': 'No se autenticó'})
            
            
        else:
            return render(request, 'accounts/login.html', {'form': form, 'msj': 'Los datos ingresados no coinciden con un usuario existente.'})
        
    else:
        form = AuthenticationForm()
    
        return render(request, 'accounts/login.html', {'form': form, 'msj':''})
        
        
def registrar(request):
    
    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'indice/index.html', {'msj': f'Se creó correctamente el usuario: {username}'})
        else:
             return render(request, 'accounts/registrar.html', {'form':form, 'msj': ''})    
    
    form = NuestraCreacionUser()
    return render(request,  'accounts/registrar.html', {'form': form, 'msj':''})

@login_required
def editar_usuario(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    
    if request.method == 'POST':
        form = EditFullUser(request.POST, request.FILES)
        
        if form.is_valid():
            #username = form.cleaned_data['username']
            #form.save()
            #return render(request, 'index/index.html', {'msj': f'Se creo el usuario {username}'})
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            #request.user. = form.cleaned_data['email']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.more_description = form.cleaned_data['more_description']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return redirect('inicio')
        else:
             return render(request, 'accounts/editar_usuario.html', {'form':form, 'msj': ''})    
    
    form = EditFullUser(
        initial={
            'email': request.user.email, 
            'password1' : '',  
            'password2' : '', 
            'first_name' : request.user.first_name, 
            'last_name' : request.user.last_name,  
            'avatar' : user_extension_logued.avatar,  
            'link' : user_extension_logued.link, 
            'more_description' : user_extension_logued.more_description 
        }
    )
    return render(request,  'accounts/editar_usuario.html', {'form': form, 'msj':''})
  

@login_required
def usuario_datos(request):
    return render(request, 'accounts/usuario_datos.html', {})