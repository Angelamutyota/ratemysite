from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name = 'index'),
    path('profile/', views.profile, name= 'profile'),
    path(r'^search/', views.search, name='search_results'),
   path('uploadproject/',views.new_project,name='new_project')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)