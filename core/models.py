from django.db import models

# Create your models here.
class HoverTable(models.Model):
	rendering_engine = models.CharField(max_length=50, null=True)
	browser = models.CharField(max_length=50, null=True)
	platform = models.CharField(max_length=100, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)