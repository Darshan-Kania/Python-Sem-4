from django.db import models

# Create your models here.


class BlogModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title