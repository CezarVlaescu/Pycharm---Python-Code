from django.db import models

class AdminArticle(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.title

STAT = (
    (0, 'Draft'),
    (1, 'Publish'),
)
class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=80, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STAT, default=0)
    image = models.ImageField(upload_to='update/')

    def __str__(self):
        return {self.title}



