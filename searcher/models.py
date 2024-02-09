from django.db import models

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


class Thesis(models.Model):
    class Status(models.TextChoices):
        REJECTED = "RJ", "Rejected"
        PUBLISHED = "PB", "Published"
        UNDER_REVIEW = "UR", "Under Review"

    title = models.CharField(max_length=250)

    authors = models.ManyToManyField(Author)

    panelists = models.ManyToManyField(Panelist)

    keywords = models.ManyToManyField(Keyword)

    abstract = models.TextField()

    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.UNDER_REVIEW
    )

    defense_date = models.DateTimeField()

    published_date = models.DateTimeField()

    paper_link = models.CharField(max_length=250)

    institution = models.CharField(max_length=250)

    department = models.CharField(max_length=250)

    adviser = models.CharField(max_length=250)

    def __str__(self):
        return self.title
