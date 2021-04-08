from django.contrib import admin
from .models import Project
#, ProjectImage


# #Added this 05/04/2021 so that multiple images can be added to a project
# class ProjectImageAdmin(admin.StackedInline):
#     model = ProjectImage

@admin.register(Project)
#The below class defines some handy defaults within the admin pages
class ProjectAdmin(admin.ModelAdmin):
    # inlines = [ProjectImageAdmin] #Added this 05/04/2021 so that multiple images can be added to a project
    list_display = ('title', 'slug', 'status','created_on') #Adds extra columns to the list view
    list_filter = ("status",) #adds a filter to the right hand side
    search_fields = ['title', 'content'] #adds a search function
    prepopulated_fields = {'slug': ('title',)} #autopopulates the slug

# admin.site.register(Project,ProjectAdmin)
    class Meta:
       model = Project


# # admin.site.register(ProjectImage)

# @admin.register(ProjectImage)
# class ProjectImageAdmin(admin.ModelAdmin):
#     pass



# from django.contrib import admin
 
# from .models import Project, ProjectImage
 
# class ProjectImageAdmin(admin.StackedInline):
#     model = ProjectImage
 
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     inlines = [ProjectImageAdmin]
 
#     class Meta:
#        model = Project
 
# @admin.register(ProjectImage)
# class ProjectImageAdmin(admin.ModelAdmin):
#     pass