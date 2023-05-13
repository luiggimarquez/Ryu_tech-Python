from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 200)
    Message = RichTextField(blank=False, null=False, default='')
    imageMain = models.ImageField(upload_to='blogs',  null = True, blank = True)
    dateAdded = models.DateTimeField(auto_now_add = True)
    dateModified = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f" {self.title} - {self.user}"
    
    class Meta:
        ordering = ['-dateModified']
 