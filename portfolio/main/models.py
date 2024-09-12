from django.db import models

# Create your models here.

class Messages(models.Model):
	name = models.CharField(max_length=40, null=False, blank=False)
	email = models.EmailField(null=False, blank=False)
	message = models.TextField(null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message[:80]