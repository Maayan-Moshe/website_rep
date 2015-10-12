from django.db import models

# Create your models here.

class web_page_content_location(models.Model):
	path = models.CharField(max_length=300)
	name = models.CharField(max_length=200)
	
	def __str__(self):              # __unicode__ on Python 2
         return self.name