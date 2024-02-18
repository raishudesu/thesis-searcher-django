from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Panelist(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Adviser(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Thesis(models.Model):
    class Status(models.TextChoices):
        REJECTED = "RJ", "Rejected"
        PUBLISHED = "PB", "Published"
        UNDER_REVIEW = "UR", "Under Review"

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250, unique_for_date="published_date")

    authors = models.ManyToManyField(Author)

    panelists = models.ManyToManyField(Panelist)

    keywords = models.ManyToManyField(Keyword)

    abstract = models.TextField()

    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.UNDER_REVIEW
    )

    published_date = models.DateTimeField(default=timezone.now)

    defense_date = models.DateTimeField()

    paper_link = models.CharField(max_length=250)

    institution = models.CharField(max_length=250)

    department = models.CharField(max_length=250)

    adviser = models.ForeignKey(Adviser, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["-published_date"]
        indexes = [models.Index(fields=["-published_date"])]

    def get_absolute_url(self):
        return reverse(
            "thesis:thesis_detail",
            args=[
                self.published_date.year,
                self.published_date.month,
                self.published_date.day,
                self.slug
            ],
        )

    def __str__(self):
        return self.title
