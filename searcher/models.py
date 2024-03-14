from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
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

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Thesis.Status.PUBLISHED)



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

    objects = models.Manager()
    published = PublishedManager()

    tags = TaggableManager()

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

class Comment(models.Model):
    thesis = models.ForeignKey(Thesis, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email=models.EmailField()
    body= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.thesis}'