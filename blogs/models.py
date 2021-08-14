from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    title = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50,null=True)
    sub = models.CharField(max_length=50,null=True)
    message = models.TextField()

    def _str_(self):
      return self.title
        

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Comment(models.Model):
    title = models.CharField(max_length=225, null=True)
    email = models.EmailField(max_length=50,null=True)
    body = models.TextField()
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

  
class Images(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    def _str_(self):
      return self.image1
