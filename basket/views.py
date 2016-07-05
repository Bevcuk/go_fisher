from django.shortcuts import render

# Create your views here.

def basket(request):
	# context = { 'header': 'Hi from start page !' }
	# return render(request, 'startpage/index.html', context)
	return render(request, 'basket/basket.html')