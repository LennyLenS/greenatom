from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255)
    j_b = models.FileField(upload_to="J_D")
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ' ' + self.surname

