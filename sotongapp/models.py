from django.db import models


class Organ(models.Model):
    name = models.CharField(max_length=30)
    url_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Information(models.Model):
    temp = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.DateField()
    time = models.TimeField()
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE, related_name='organ')

    def __str__(self):
        return str(self.time)