from django.db import models

# Create your models here.
class Colors(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name

class Person(models.Model):
    colors = models.ForeignKey(Colors, on_delete=models.CASCADE, related_name='color', null=True)
    name =models.CharField(max_length=100)
    age = models.IntegerField()

class PersonDetail(models.Model):
    city = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)