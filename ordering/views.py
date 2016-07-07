from django.shortcuts import render

def ordering(request):
	# context = { 'header': 'Hi from start page !' }
	# return render(request, 'startpage/index.html', context)
	return render(request, 'ordering/ordering.html')
