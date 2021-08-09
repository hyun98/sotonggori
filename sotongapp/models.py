from django.db import models
from django.utils import timezone



class Organ(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Information(models.Model):
    temp = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.DateField(auto_now="true")
    time = models.TimeField(auto_now="true")
    organ_name = models.ForeignKey(Organ, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.time)

  