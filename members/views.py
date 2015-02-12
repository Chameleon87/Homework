from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from member.forms import CreateMember, LoginMember
from member.models import Member
from django.contrib.auth import authenticate, login, logout

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
	    member = Member(user=user, name=form.cleaned_data['name'],)
            member.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = CreateUser()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

#Logging Members on
def LoginMember(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginMember(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
	    password = form.cleaned_data['password']
	    if member is not None:
		login(request, member)
		return HttpResponseRedirect('/profile/')
	    else:
		return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))
        else:
	    return render_to_response('login.html', {'form':form}, context_instance=RequestContext(request))
    else:
	form = LoginMember()
        context = {'form': form}
	return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutMember(request):
    logout(request)
    return HttpResponseRedirect('/')
