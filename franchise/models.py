from django.db import models


class Panchayat(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=256)
    panchayat = models.ForeignKey(to=Panchayat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.panchayat} Ward {self.name}"


class Franchise(models.Model):
    PENDING = 'pending'
    EXIST = 'exist'
    STATUS = (
        (PENDING, 'Pending'),
        (EXIST, 'Exist'),
    )
    name = models.CharField(max_length=256)
    block = models.ForeignKey(to=Ward, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=8)

    def __str__(self):
        return self.name
