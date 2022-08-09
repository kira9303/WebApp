from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.shortcuts import  render, redirect
from .forms import NewUserForm, TeamForm, TaskForm
from .models import Team, User, Task
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				#return redirect(render_homepage)
				return redirect(render_homepage)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(login_request)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form": form})

@login_required(login_url="login")
def render_homepage(request):
	if request.method == "POST" or request.method == "GET":
		team = Team.objects.all()
		content = {"content": team}

		return render(request = request, template_name="homepage.html", context=content)

'''def register_team(request):
	if request.method == "POST":
		form = NewTeamForm(request.POST)
		if form.is_valid():
			team = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(login_request)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form": form})'''

@login_required(login_url="login")
def register_team(request):
	context = {}
	if(request.method == "POST"):
		if request.user.is_authenticated:
			print("user logged in")
		else:
			print("user not logged in")

	# create object of form
		form = TeamForm(request.POST)

	# check if form data is valid
		if form.is_valid():
		# save the form data to model
			form.save()

		context['form'] = form
	context['form'] = TeamForm()
	return render(request, "teamdet.html", context)


@login_required(login_url="login")
def register_task(request):
	context = {}
	if(request.method == "POST"):
		if request.user.is_authenticated:
			print("user logged in")
		else:
			print("user not logged in")

	# create object of form
		form = TaskForm(request.POST)

	# check if form data is valid
		if form.is_valid():
		# save the form data to model
			form.save()

		context['form'] = form
	context['form'] = TaskForm()
	return render(request, "task.html", context)








