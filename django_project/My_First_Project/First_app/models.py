from django.db import models


# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instruement = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
   # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_starts = models.IntegerField()