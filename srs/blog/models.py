from django.db import models

# Create your models here.
# each class -- a table in db
# each var in class -- column in that table

class Post(models.Model):
	title = models.CharField(max_length = 240) 
	body = models.TextField()

	def __str__(self):
		return self.title
