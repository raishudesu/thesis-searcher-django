from django.urls import path
from . import views

app_name = "thesis"

urlpatterns = [
    path("", views.thesis_list, name="thesis_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>",
        views.thesis_detail,
        name="thesis_detail",
    ),
    path('<int:thesis_id>/comment/',
        views.thesis_comment, name='thesis_comment'),
    path("search", views.search_theses, name="search_theses")
]
