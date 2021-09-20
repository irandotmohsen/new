from django.db import models

class Expense(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.text

class Income(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.text