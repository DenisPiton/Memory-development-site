from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    test_passed = models.IntegerField(default=0)
    words_test_passed = models.IntegerField(default=0)
    results = models.JSONField(default={'slova':[],'primer':[]})
    best_time = models.IntegerField(default=1000)

