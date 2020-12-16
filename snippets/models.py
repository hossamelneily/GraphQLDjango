from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', related_name='by_snippet', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]


class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name
