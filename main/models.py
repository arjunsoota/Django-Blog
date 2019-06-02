from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(null =True)
    CreatedAt = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ManyToManyField('Author')
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

