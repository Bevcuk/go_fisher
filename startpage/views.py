from django.shortcuts import render

# Create your views here.

def index(request):
	# context = { 'header': 'Hi from start page !' }
	# return render(request, 'startpage/index.html', context)
	return render(request, 'index.html')