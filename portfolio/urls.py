# portfolio/urls.py 
from django.urls import path
from .views import ProjectListView, ProjectDetailView


from django.conf import settings#added 05/04/2021 to allow multiple images
from django.conf.urls.static import static #added 05/04/2021 to allow multiple images

urlpatterns = [
    
    path('', ProjectListView.as_view(), name='project_list'), 
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#added 05/04/2021 to allow multiple images

