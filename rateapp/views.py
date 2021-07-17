from rateapp.forms import ProjectForm
from django.shortcuts import render, redirect
from django.http  import HttpResponse
from.models import Profile, Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user)
    projects = Profile.objects.filter(user=user)
    return render(request, 'profile.html',{'user':user, 'profile': profile, 'projects':projects})

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