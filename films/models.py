from django.db import models


class Movie(models.Model):
    imdbId = models.IntegerField("imdbId")
    Title = models.CharField("Title", max_length=255)
    Poster = models.CharField("Poster", max_length=255)
    Rating = models.IntegerField("Rating")

    def __str__(self):
        return self.Poster

