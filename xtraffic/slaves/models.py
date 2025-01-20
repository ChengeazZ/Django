from django.db import models


class Slave(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    durability = models.PositiveIntegerField(null=True,blank=True)
    race = models.CharField(max_length=100,null=True,blank=True)
    photo = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
     

    def __str__(self):
        return self.name