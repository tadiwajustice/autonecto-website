from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    features = models.TextField(help_text="Enter one feature per line")

    def __str__(self):
        return self.title
