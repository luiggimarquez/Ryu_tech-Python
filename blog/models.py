from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 200)
    imageMain = models.ImageField(upload_to='blogs',  null = True, blank = True)
    dateAdded = models.DateTimeField(auto_now_add = True)
    dateModified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f" {self.title} - {self.user}"