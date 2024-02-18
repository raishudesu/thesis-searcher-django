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
]
