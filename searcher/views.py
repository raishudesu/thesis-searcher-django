from django.shortcuts import render
from django.http import HttpResponse
from .models import Thesis

# Create your views here.


def index(request):
    theses = Thesis.objects.all()
    return render(request, "base.html", {"theses": theses})


# def thesis_list(request):
# return render(request, "searcher/theses.html", {"theses": theses})
