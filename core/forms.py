from django import forms
from core.models import Modal

class ModalForm(forms.Form):
	class Meta:
		model = Modal
		fields = ['modal_email', 'modal_password', 'modal_image', 'minimal', 'multiple', 'date']