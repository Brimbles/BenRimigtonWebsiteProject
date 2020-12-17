# # blog/urls.py 
# from django.urls import path
# from .views import BlogHomePageView,BlogDetailView,BlogCreateView

# urlpatterns = [
#     path('blog/new/', BlogCreateView.as_view(), name='blog_new'), # new
#     path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'), 
#     path('', BlogHomePageView.as_view(), name='bloghome'), 
# ]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogpostList.as_view(), name='blog_home'),
    path('<slug:slug>/', views.BlogpostDetail.as_view(), name='blog_detail'),
]