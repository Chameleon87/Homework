from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.forms.widgets import *
from django.core.context_processors import csrf
from forms import CreateUser
from django.contrib.auth.models import User

# Create your views here.
def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('profile')
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
            email = form.cleaned_data['email'], 
            password = form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/profile')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = CreateUser()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))    