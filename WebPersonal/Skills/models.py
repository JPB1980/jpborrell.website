from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skills"
        verbose_name_plural = "Skills"
        ordering = ["created"]

    def __str__(self):
        return self.title
