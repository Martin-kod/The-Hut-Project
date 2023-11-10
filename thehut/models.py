from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=12)
    num_guests = models.IntegerField(choices=[(2, 2), (4, 4)])
    date = models.DateField()
    time = models.IntegerField(choices=[
        (1, '16:00'), (2, '18:00'), (3, '20:00')])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']
