from django.db import models

# Create your models here.


class Employees(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f"ID: {self.pk} | Username: {self.username} | Name: {self.first_name}"