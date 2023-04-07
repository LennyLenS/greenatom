from django.db import models

from position.models import Position
from specialization.models import Specialization


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255)
    j_b = models.FileField(upload_to="J_D")
    job = models.TextField(max_length=511)
    position = models.ManyToManyField(Position)
    specialization = models.ManyToManyField(Specialization)
    depat_name = models.CharField(max_length=511)
    center_name = models.CharField(max_length=511)
    group_name = models.CharField(max_length=511)

    def __str__(self):
        return self.name + ' ' + self.surname

