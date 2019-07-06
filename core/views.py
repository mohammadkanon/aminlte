from django.shortcuts import render
from core.models import HoverTable

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