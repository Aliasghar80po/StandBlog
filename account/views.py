from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import loginForm, RegisterForm, UserEditForm
from django.core.exceptions import ValidationError


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect("home:main")
    else:
        form = loginForm()
    return render(request, "account/login.html", {'form': form})


# HttpRequest
# HttpResponse
def user_logout(request):
    logout(request)
    return redirect('home:main')

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')

            if password != repeat_password:
                raise ValidationError("Passwords do not match.")

            # ثبت‌نام کاربر با استفاده از مدل کاربری (User)
            user = User.objects.create_user(username=username, email=email, password=password)

            # ورود کاربر به سایت بلافاصله پس از ثبت‌نام
            login(request, user)

            # هدایت کاربر به صفحه‌ی اصلی (home:main)
            return redirect('home:main')

    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, "account/register.html", context=context)

def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/edit.html',{'form':form})
























# print(type(authenticate))
# print(type(user))
# print("............................")
# print(type(request.POST.get))
# print("............................")
# print(type(request.GET))
# print("............................")
# print(type(request.GET.get))
# print("............................")
# print(type(request))
# print(type(render))
# print(type(authenticate))
# print(type(login))
# print(type(request.method))
# print(type(request.user.is_authenticated))
# input ==>print(type(request.user.is_authenticated)) ==> request.user is method in middleware
# request.user equal to true==is_authenticated or false==is_anonymous (type bool)
# input ==>print(type(request.POST.get)) ==> output ==> <class 'django.http.request.QueryDict'> is an <<object>>
# input ==>print(type(request)   ==> output ==> <class 'django.core.handlers.wsgi.WSGIRequest'> is an <<object>>
# Request is an object from the HttpRequest(in file wsgi.py) class, which the WSGIRequest class inherits from the HttpRequest class

# request.GET.get
# request.POST.get
# are methods
#
#
#
#  type request.methode is str Because the get_method function returns one str which is equal to "POST" or "GET"
# def get_method(self):
# Return a string indicating the HTTP request method.
# default_method = "POST" if self.data is not None else "GET"
# return getattr(self, 'method', default_method)
