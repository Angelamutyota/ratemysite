from django.db.models import fields
from rest_framework import serializers
from .models import Project, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile_pic', 'bio', 'contact']
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('user', 'title', 'project_image', 'description','link', 'technologies_used')
