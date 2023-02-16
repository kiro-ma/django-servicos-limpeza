from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class modelTESTE(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Usuario(AbstractUser):
    tipo_user = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username