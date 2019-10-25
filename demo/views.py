from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View
from .models import Notification

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class Notifications(LoginRequiredMixin, View):

	login_url = 'hi'

	def get(self,request):
		
		notification = Notification.objects.filter(user=request.user)
		return render(request,'home.html',{'notification':notification})

def user_login(request):
	if request.method == "GET":
		return render(request,'login.html')

	if request.method == "POST":
		name = request.POST.get('name')
		password = request.POST.get('password')
		user = authenticate(username=name, password=password)
		if user is not None:
			login(request,user)
			print("OKay")
			return redirect('home')

def logout_view(request):

	logout(request)
	return redirect('hi')