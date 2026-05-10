from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
