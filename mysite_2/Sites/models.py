from django.db import models

# Create your models here.
class Sites(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	timestamp = models.DateTimeField()

	def __str__(self):
		return self.title