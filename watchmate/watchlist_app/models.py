from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    path = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    ''' We are using related name here so that we get our stramplatform data in drf(ManyToOne relationship) '''
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist") #ManyToOne Relationship
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=500,null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)  #everytime we update , it will get updated.
    
    
    def __str__(self):
        return (str(self.rating)+ ' | '+ self.watchlist.title)
     
    
    
    

    