from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return (self.first_name)

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artiste_Id = models.IntegerField()

    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    song = models.ForeignKey()
    content = models.TextField()
    song_Id = models.IntegerField()
    
    def __str__(self):
        return(self.song)
