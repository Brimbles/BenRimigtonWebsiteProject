from django.views.generic import TemplateView
from django.views import generic
from blog.models import Blogpost

# class HomePageView(TemplateView):
#     template_name = 'home.html'

#Added in this view so that the top n blog posts can be made available to the home page
class HomePageView(generic.ListView):
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')[:4]
    template_name = 'home.html'

class AboutPageView(TemplateView):  # new
    template_name = 'about.html'

# class PostsHomePageView(TemplateView):  # new
#     template_name = 'postshome.html'
