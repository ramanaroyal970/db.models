from django.db import models

# Create your models here.
class topic(models.Model):
    game=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.game

class webpage(models.Model):
    game=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self) -> str:
        return self.name
class access_records(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.author
