from django.shortcuts import render
from django.http import HttpResponse
from .models import Video, Place


def home(request):
	places = Place.objects.all()

	return render(request, 'website/home.html', {'places':places})