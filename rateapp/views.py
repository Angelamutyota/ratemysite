from django.http.response import Http404
from rest_framework import serializers
from rateapp.forms import ProjectForm, CreateUserForm, ProfileForm
from django.shortcuts import render, redirect
from django.http  import HttpResponse
from.models import Profile, Project
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProfileSerializer, ProjectSerializer
from rateapp import serializer

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage') 
        name = form.cleaned_data.get("username")
        messages.success(request, 'Account was created for' , name)
    context = {'form':form, 'profile':profile}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect Username or Password')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='login')
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

@login_required(login_url='login')
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = ProfileForm(instance=request.user.profile)
    profiles = Profile.objects.filter(user=user)
    projects = Project.objects.filter(user = user)
    context = {
        'projects': projects,
        'profiles': profiles,
        'prof_form': prof_form,
    }
    return render(request, 'profile.html', context)

def search(request):
    if 'projectname' in request.GET and request.GET ['projectname']:
        search_title = request.GET.get('projectname')
        searched_project = Project.search_project(search_title)

        message = f"{search_title}"

        return render(request, 'search.html', {"message": message, "projects": searched_project })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def  new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')
    else:
        form = ProjectForm()
    return render(request,'newproject.html',{"form":form})

def project(request, id):
    try:
        project = Project.objects.get(id =id)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, "project.html", {"project":project})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get (self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)