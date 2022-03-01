from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'book'

    def __str__(self):
        return f"{self.name}"
