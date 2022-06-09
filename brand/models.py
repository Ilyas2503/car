from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    value = models.FloatFBield()
    color = models.CharField(max_length=25)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title
