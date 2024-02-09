from django.shortcuts import render
from django.http import HttpResponse
from .models import Thesis

# Create your views here.


def index(request):
    theses = Thesis.objects.all()
    return render(request, "base.html", {"theses": theses})


def thesis_detail(request, id):
    thesis = Thesis.objects.get(pk=id)
    authors = thesis.authors.all()
    panelists = thesis.panelists.all()
    keywords = thesis.keywords.all()

    context = {
        "thesis": thesis,
        "authors": authors,
        "panelists": panelists,
        "keywords": keywords,
    }

    return render(request, "detail.html", context)
