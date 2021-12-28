#IMPORTS
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Models

#Post class for database
class Post(models.Model):
    Title= models.CharField(max_length=100)
    Content= models.TextField()
    Date_Posted= models.DateTimeField(default=timezone.now) #We can edit the time
    Author= models.ForeignKey(User,on_delete=models.CASCADE) #if user deleted then delete post

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) #full path as string

