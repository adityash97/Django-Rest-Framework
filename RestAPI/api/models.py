from django.db import models

# Create your models here.
class Artcile(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    date = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.title