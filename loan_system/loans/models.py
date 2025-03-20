# loans/models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    principal_amount = models.FloatField()
    loan_period = models.IntegerField()  # years
    rate_of_interest = models.FloatField()
    total_interest = models.FloatField()
    total_amount = models.FloatField()
    monthly_emi = models.FloatField()
    amount_paid = models.FloatField(default=0)
    emis_paid = models.IntegerField(default=0)
    loan_start_date = models.DateField(auto_now_add=True)

class Transaction(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='transactions')
    TRANSACTION_CHOICES = (('EMI', 'EMI'), ('LUMP_SUM', 'LUMP_SUM'))
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)
