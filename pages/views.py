from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'


# class PostsHomePageView(TemplateView):  # new
#     template_name = 'postshome.html'
