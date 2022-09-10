from django.shortcuts import render
from django.contrib.auth import authenticate , login 
from django.http import HttpResponse
from .forms import LoginForm
from django.shortcuts import redirect

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                    # return HttpResponse("loged in")
                else:
                    return HttpResponse("User inactive")
            else:
                return HttpResponse("Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html',{"form": form})


