from django.db import models

class jobs(models.Model):
	img=models.ImageField(upload_to='images/')
	summary=models.CharField(max_length=200)
