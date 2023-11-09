from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    num_guests = models.IntegerField(choices=[(2, 2), (4, 4)])
    date = models.DateField()
    time = models.IntegerField(choices=[
        (1, '16:00'), (2, '18:00'), (3, '20:00')])

    class Meta:
        ordering = ['date']
