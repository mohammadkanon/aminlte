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


def modal(request):
	if request.method == 'POST':
		form = ModalForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ModalForm()
	context = {
		'form': form
	}
	return render(request, 'core/modal.html', context)