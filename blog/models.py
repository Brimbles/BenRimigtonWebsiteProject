from django.db import models
from django.urls import reverse #
from django.contrib.auth.models import User

# Create a tuple to store the status, this will be used when rendering so that only those in published status will be visible
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        'auth.User', #For the author field we’re using a ForeignKey which allows for a many-to-one relationship. 
        #This means that a given user can be the author of many different blog posts butnottheotherwayaround.
        #Thereferenceistothebuilt-inUsermodelthatDjango provides for authentication. 
        on_delete=models.CASCADE, #For all many-to-one relationships such as a ForeignKey we must also specify an on_delete option.
    )
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title