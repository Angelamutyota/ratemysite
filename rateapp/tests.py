from django.test import TestCase
from .models import Profile, Project
# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.james= Profile(user= 'James', profile_pic ='hgvg.jpeg', bio ='i am james', contact = '0715168777')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))

     # Testing Save Method
    def test_save_method(self):
        self.james.save_profile()
        editors = Profile.objects.all()
        self.assertTrue(len(editors) > 0)

class ProjectTestClass(TestCase):

    def setUp(self):
        self.instagram= Project(user = 'James', title='instagram', project_image ='fwffw.jpeg', description= 'this is a clone of instagram', link = 'instagram.com', technologies_used= 'django')
        self.instagram.save_project()

       

    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
