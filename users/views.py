# type: ignore
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account has been created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/sign-up.html',{'form': form})

@login_required
def profile_page(request):
    return render(request,'users/profile.html')