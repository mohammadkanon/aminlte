from django.shortcuts import render, redirect
from core.models import HoverTable
from core.forms import ModalForm

# Create your views here.
def dashboard(request):
	return render(request, 'core/calender.html')

def hovertable(request):
	hover_table = HoverTable.objects.all()
	feature_table = HoverTable.objects.all()

	context = {
		'hover_table': hover_table,
		'feature_table': feature_table
	}

	return render(request, 'core/hover-table.html', context)


def pain(request):
	if request.method == 'POST':
		# form = ModalForm(request.POST, request.FILES)
		form = ModalForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
		else:
			errors = []
			for field in form:
				for error in field.errors:
	 				errors.append(field.label+" "+error)

			for error in form.non_field_errors():
	 			errors.append(field.label+" "+error)

			print(errors)

	else:
		form = ModalForm()

	context = {
		'form': form
	}

	return render(request, 'core/modal.html', context)
