from django.contrib import admin
from .models import Project


#The below class defines some handy defaults within the admin pages
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on') #Adds extra columns to the list view
    list_filter = ("status",) #adds a filter to the right hand side
    search_fields = ['title', 'content'] #adds a search function
    prepopulated_fields = {'slug': ('title',)} #autopopulates the slug
  
admin.site.register(Project,ProjectAdmin)
