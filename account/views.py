from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('yes!')
                else:
                    return HttpResponse('disabled account')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
