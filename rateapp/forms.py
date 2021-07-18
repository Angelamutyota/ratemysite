from django import forms
from .models import Project,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','project_image','description','link']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','contact']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
