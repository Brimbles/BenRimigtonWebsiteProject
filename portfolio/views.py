from django.views.generic import ListView, DetailView 
# from django.views.generic.edit import CreateView 
# from django.shortcuts import render
from .models import Project

# def PortfolioHomePageView(request):
#     projects = Project.objects.all()
#     context = {
#         'projects' :projects
#     }
#     return render(request, 'portfoliohome.html', context)
#     # context_object_name = 'portfoliohome'


class ProjectListView(ListView):
    model = Project
    template_name = 'portfoliohome.html'
    context_object_name = 'project_list'

class ProjectDetailView(DetailView):
    model = Project 
    template_name = 'project_detail.html'
    context_object_name = 'project_detail'

# class ProjectCreateView(CreateView): 
#     model = Project
#     template_name = 'project_new.html'
#     fields = ['title', 'description', 'technology']
