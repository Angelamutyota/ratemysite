from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   path('register/', views.registerPage, name= 'register'),
   path('login/', views.loginPage, name= 'loginpage'),
   path('logout/',views.logoutpage,name='logout'),

    path('',views.index, name = 'index'),
    path('profile/', views.profile, name= 'profile'),
    path('search/', views.search, name='search_results'),
    path('uploadproject/',views.new_project,name='new_project'),
    path('project/<int:id>/',views.project,name='project'),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)