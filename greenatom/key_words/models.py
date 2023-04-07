from django.db import models


class Key_words(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


