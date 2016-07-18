from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from catalogue.models import BigCategory
from catalogue.models import Category
from product.models import Kind


class IndexView(ListView):
	context_object_name = 'home_list'
	template_name = 'index.html'
	queryset = BigCategory.objects.all()

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['category_list'] = Category.objects.all()
		context['kind_list'] = Kind.objects.all()
		return context