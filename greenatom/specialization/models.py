from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    knowledge = models.TextField()
    description = models.TextField()

