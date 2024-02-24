from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Thesis
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .forms import CommentForm, SearchForm
# Create your views here.


def landing_page(request):

    return render(request, "searcher/landing-page/landing_page.html")

def thesis_list(request):
    theses = Thesis.published.all()
    paginator = Paginator(theses, 3)
    page_number = request.GET.get("page", 1)
    theses = paginator.page(page_number)
    form = SearchForm()
    context = {"theses": theses, "form" : form}
    return render(request, "searcher/thesis/list.html", context)


def thesis_detail(request, year, month, day, post):
    thesis = get_object_or_404(
        Thesis,
        status=Thesis.Status.PUBLISHED,
        slug=post,
        published_date__year=year,
        published_date__month=month,
        published_date__day=day,
    )

    authors = thesis.authors.all()
    panelists = thesis.panelists.all()
    keywords = thesis.keywords.all()
    
    comments = thesis.comments.filter(active=True)
    form = CommentForm()
    context = {
        "thesis": thesis,
        "authors": authors,
        "panelists": panelists,
        "keywords": keywords,
        "form": form,
        "comments": comments
    }

    return render(request, "searcher/thesis/detail.html", context)

@require_POST
def thesis_comment(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id, status=Thesis.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.thesis = thesis
        comment.save()

    return render(request, "searcher/thesis/comment.html",
                        {'thesis':thesis,
                         'form': form, 
                         'comment': comment})

@require_POST
def search_theses(request):
    form = SearchForm(data=request.POST)
    theses = None

    if form.is_valid():
        keywords = form.data.get("abstract")
        theses = Thesis.objects.filter(abstract__contains=keywords)

    context = {
        "theses" : theses,
        "form": form
    }
    return render(request, "searcher/thesis/search.html", context)
