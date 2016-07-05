from django.shortcuts import render

# Create your views here.

def ordering(request):
	# context = { 'header': 'Hi from start page !' }
	# return render(request, 'startpage/index.html', context)
	return render(request, 'ordering/ordering.html')