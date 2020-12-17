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




# class BlogHomePageView(ListView):
#     model = Blogpost
#     template_name = 'bloghome.html'
#     context_object_name = 'all_blogs_list'

# class BlogDetailView(DetailView):
#     model = Blogpost 
#     template_name = 'blog_detail.html'
#     context_object_name = 'post_detail_view'

# class BlogCreateView(CreateView): 
#     model = Blogpost
#     template_name = 'blog_post_new.html'
#     fields = ['title', 'author', 'body']
