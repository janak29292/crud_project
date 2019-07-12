from django.db import models
from django.contrib.auth.models import AbstractUser

PROFILE_CHOICES=[
    ('journalist', 'Journalist'),
    ('pr', 'PR Pro')
]
# Create your models here.
class User(AbstractUser):
	role = models.CharField(max_length = 16, choices=PROFILE_CHOICES, null=True)


class Pr(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Jr(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class School(models.Model):
	name = models.CharField(max_length = 64)
	principal = models.CharField(max_length = 64)
	location = models.TextField()
	pr = models.ForeignKey(Pr,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.name
