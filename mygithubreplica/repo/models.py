from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)

class Commit(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(File)
