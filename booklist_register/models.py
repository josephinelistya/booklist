from django.db import models

# Create your models here.
class Booktype(models.Model):
    booktype = models.CharField(max_length=50)

    def __str__(self):
        return self.booktype

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publishdate = models.DateField()
    pages = models.IntegerField()
    booktype = models.ForeignKey(Booktype,on_delete=models.CASCADE)

