from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics")
    bio = models.TextField()
    phone_no = models.IntegerField()
    
    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_pics")
    dateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title
    
    def get_success(self):
        return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)
    dateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " Comment: " + self.content
    

