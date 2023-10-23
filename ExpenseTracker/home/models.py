from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative')
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField()
    expenses = models.FloatField(null=True)
    balance = models.FloatField(null=True)


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100, choices=TYPE)

    def __str__(self):
        return self.name
