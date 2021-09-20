from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    emp_id = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name