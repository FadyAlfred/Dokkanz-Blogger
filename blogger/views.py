from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import Register, Login, Post
from .models import User
from .models import Post as Post_model
from . import hashing, verification
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        if request.POST['form_type'] == 'login':
            form = Login(request.POST)
            if form.is_valid():
                email_address = form.cleaned_data['email_address']
                password = form.cleaned_data['password']
                remember = form.cleaned_data['remember']
                user = User.login(email_address, password)
                if user:
                    if remember:
                        response = HttpResponseRedirect('/blogger/home/')
                        response.set_cookie("username", str(user.username), expires='Sun, 15 Jul 2020 00:00:01 GMT')
                        messages.success(request, 'Welcome Back ' + user.username)
                        return response
                    else:
                        response = HttpResponseRedirect('/blogger/home/')
                        response.set_cookie("username", str(user.username), expires='0')
                        messages.success(request, 'Welcome Back ' + user.username)
                        return response
                else:
                    response = HttpResponseRedirect('/blogger/home/')
                    messages.success(request, 'Username or password wrong please try again')
                    return response
        elif request.POST['form_type'] == 'post':
            response = HttpResponseRedirect('/blogger/home/')
            form = Post(request.POST)
            if form.is_valid():
                current_user = request.COOKIES.get("username")
                post = form.cleaned_data['text']
                Post_model.add_post(current_user, post)
            return response
    else:
        current_user = request.COOKIES.get("username")
        if current_user:
            posts = Post_model.get_all()
            template = loader.get_template('index.html')
            login = Login(request.POST)
            post = Post(request.POST)
            return HttpResponse(template.render({'login': login, 'post': post, 'posts': posts, 'user': current_user}, request))
        else:
            posts = Post_model.get_all()
            template = loader.get_template('index.html')
            login = Login(request.POST)
            return HttpResponse(template.render({'login': login, 'posts': posts, 'user': None}, request))


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            email_address = form.cleaned_data['email_address']

        haveError = False

        params = dict()
        if not verification.Verification().nameValied(username):
            params['nameError'] = "That's not a valid username."
            haveError = True

        if not verification.Verification().passwordValied(password):
            params['passwordError'] = "That wasn't a valid password."
            haveError = True

        if not verification.Verification().verfiyPassword(password, repeat_password):
            params['verifyError'] = "Your passwords didn't match."
            haveError = True

        if not verification.Verification().emailValied(email_address):
            params['emailError'] = "That's not a valid email."
            haveError = True

        username_used = User.check_username(username)

        email_used = User.check_email(email_address)

        if username_used and email_address:
            msg = 'this username and email already exist'
            form = Register()
            template = loader.get_template('register.html')
            return HttpResponse(template.render({'form': form, 'userError': msg}, request))

        elif email_used:
            msg = 'this email already exist'
            form = Register()
            template = loader.get_template('register.html')
            return HttpResponse(template.render({'form': form, 'userError': msg}, request))
        elif username_used:
            msg = 'the username already exist'
            form = Register()
            template = loader.get_template('register.html')
            return HttpResponse(template.render({'form': form, 'userError': msg}, request))
        else:
            if not haveError:
                hashed = hashing.Hashing().hashPassword(email_address, password)
                User.register(username, hashed, email_address)
                messages.success(request, 'Welcome ' + username + ' Now You Can Login To Dokkanz Blogger')
                return redirect('index')
            else:
                template = loader.get_template('register.html')
                return HttpResponse(template.render({'form': form, **params}, request))

    else:
        current_user = request.COOKIES.get("username")
        if not current_user:
            form = Register()
            template = loader.get_template('register.html')
            return HttpResponse(template.render({'form': form}, request))
        else:
            response = HttpResponseRedirect('/blogger/home/')
            messages.success(request, 'You Already Have Account')
            return response

def logout(request):
    response = HttpResponseRedirect('/blogger/home/')
    response.delete_cookie("username")
    return response
