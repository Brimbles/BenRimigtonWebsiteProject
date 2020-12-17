# pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),  # new
    # path('postshome/', PostsHomePageView.as_view(), name='posts'),  # new
    path('', HomePageView.as_view(), name='home'),
    path('home/', HomePageView.as_view(), name='home'),
]
