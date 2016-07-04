from django.db import models


Ratings=( (1,1) , (2,2) , (3,3) , (4,4) , (5,5) )

# Create your models here.
class Tracks(models.Model):
	Track_name=models.CharField(max_length=100)
	Genre_id=models.IntegerField()
	Track_title=models.CharField(max_length=100)
	Rating=models.IntegerField(choices=Ratings,default=1)
	Track=models.FileField(upload_to='tracks')
	 
	def __unicode__(self):
		return self.Track_name

class Genre_id(models.Model):
	Genre_name=models.CharField(max_length=100)
	Genre_id=models.IntegerField()

	def __unicode__(self):
		return self.Genre_name

class Id_genre(models.Model):
	Genre_name=models.CharField(max_length=100)
	Genre_id=models.IntegerField()

