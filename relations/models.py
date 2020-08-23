from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=50,
    )
    gender = models.CharField(
        max_length=1,
    )
    dob = models.DateField()
    blood_type = models.CharField(
        max_length=3,
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    objects = models.Manager()

    def __str__(self):
        return self.name
