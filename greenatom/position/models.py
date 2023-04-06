from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    job_experience = models.CharField(max_length=255)

