from django.db import models

# Create your models here.

class WildBlog(models.Model):
    path = models.CharField(max_length=300)
    name = models.CharField(max_length=200, primary_key = True)
    
    def __str__(self):
        return self.name

class WebPageContentLocation(models.Model):
    wild_blog = models.ForeignKey(WildBlog)
    path = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
	
    def __str__(self):              # __unicode__ on Python 2
        return self.name
