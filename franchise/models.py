from django.db import models


class Panchayat(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=256)
    panchayat = models.ForeignKey(to=Panchayat, on_delete=models.CASCADE)
    PENDING = 'pending'
    EXIST = 'exist'
    DOES_NOT_EXIST = 'does_not_exist'
    STATUS = (
        (PENDING, 'Pending'),
        (EXIST, 'Exist'),
        (DOES_NOT_EXIST, 'Does not Exist'),
    )
    franchise_status = models.CharField(choices=STATUS, max_length=16)

    def __str__(self):
        return f"{self.panchayat} Ward {self.name}"

