from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=140)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        ordering = ('-created_at', )
