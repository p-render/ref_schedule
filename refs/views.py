from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from refs.forms import RegistrationForm, LoginForm
from refs.models import Ref
from django.contrib.auth import authenticate, login, logout

def RefRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.save()
            refs = Ref(user=user, first_name=form.cleaned_data['first_name'])
            refs.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    refs = request.user.get_profile
    context = {'refs': refs}
    return render_to_response('profile.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            refs = authenticate(username=username, password=password)
            if refs is not None:
                login(request, refs)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
            form = LoginForm()
            context = {'form': form}
            return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

# Not working, need help...
def Index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    refs = request.user.get_profile
    context = {'refs': refs}
    return render_to_response('index.html', context, context_instance=RequestContext(request))

def DeleteUser(request):
    if(request.GET.get('mybtn')):
        if request.user.is_authenticated():
            refs = User.objects.delete_user(user=user)
            user.delete(refs)
            return render_to_response('/delete_user.html', context, context_instance=RequestContext(request))
        

    
    
		

