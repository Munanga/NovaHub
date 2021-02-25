from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created.')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Updated account changes.')
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UserUpdateForm(instance=request.user)

    context = {"form": form}

    return render(request, "users/profile.html", context)

