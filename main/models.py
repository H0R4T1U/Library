from django.db import models

# Create your models here.
class Carte(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    extra = models.CharField(max_length=50,null=True)

    def __str__(this):
        return f"{this.author}:{this.name},{this.location},{this.extra}"