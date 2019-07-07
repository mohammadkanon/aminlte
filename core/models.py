from django.db import models

# Create your models here.
class HoverTable(models.Model):
	rendering_engine = models.CharField(max_length=50, null=True)
	browser = models.CharField(max_length=50, null=True)
	platform = models.CharField(max_length=100, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)


class Modal(models.Model):
	modal_email = models.EmailField(null=True)
	modal_password = models.CharField(max_length=50, null=True)
	modal_image = models.ImageField(upload_to='modal-image', null=True)
	State_Choices = [
		('Alabama', 'Alabama'),
		('Alaska', 'Alaska'),
		('California', 'California'),
		('Delawar', 'Delawar'),
		('Texas', 'Texas'),
		('New York', 'New York')
	]
	minimal = models.CharField(max_length=10, choices=State_Choices, default=None)
	multiple = models.CharField(max_length=10, choices=State_Choices, default=None)
	date = models.DateTimeField(null=True, blank=True)
	