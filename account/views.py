from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout
from django.views.generic import CreateView, ListView,  DeleteView, UpdateView
from .backend import Backend
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CreateUser, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import User
from django.contrib import messages

# from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def login_user(request):
	if request.method == "GET":

		return render(request, 'login.html')

	email = request.POST.get('email')
	password = request.POST.get('password')
			
	user = Backend.authenticate(request,email=email, password=password)
	# print(user)
	if user is not None:
		login(request, user, backend='account.backend.Backend')
		return redirect(to='home')

	messages.info(request, 'Username Or password is incorrect')
	return render(request, 'login.html')

	
def register(request):
	form = CreateUser(request.POST or None)
	template_name = 'register.html'

	if form.is_valid():
		form.save()
		return redirect(to='home')

	return render(request, template_name, {'form': form, 'errors': form.errors})
		
	# return HttpResponse("post")


	return render(request, template_name, {'form': form})



def logout_user(request):
	logout(request)
	return redirect(to='user:login')
	