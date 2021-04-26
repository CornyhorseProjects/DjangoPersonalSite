from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    body = models.TextField(null=True)
    image = models.FilePathField(path="/img")
    detail_image = models.FilePathField(path="/img", null=True)
