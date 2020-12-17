# portfolio/urls.py 
from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    
    path('', ProjectListView.as_view(), name='project_list'), 
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
]

