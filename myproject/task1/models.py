from django.db import models

# Create your models here.
class Bayer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=3, max_digits=3)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_length=100, decimal_places=3, max_digits=3)
    size = models.DecimalField(max_length=100, decimal_places=3, max_digits=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Bayer, related_name='game_buyer')