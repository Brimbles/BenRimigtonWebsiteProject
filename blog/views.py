# blog/views.py 
# from django.views.generic import ListView, DetailView 
# from django.views.generic.edit import CreateView 
from django.views import generic
from .models import Blogpost


class BlogpostList(generic.ListView):
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')
    template_name = 'bloghome.html'


class BlogpostDetail(generic.DetailView):
    model = Blogpost
    template_name = 'blog_detail.html'

class LastNBlogList(generic.ListView):
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')[:4]
    template_name = 'home.html'