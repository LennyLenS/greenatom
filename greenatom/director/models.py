from django.db import models

from employee.models import Employee


class Director(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255)
    id_emp = models.ManyToManyField(Employee)
    depat_name = models.CharField(max_length=511)
    center_name = models.CharField(max_length=511)
    group_name = models.CharField(max_length=511)
    pos_name = models.CharField(max_length=511)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.login
