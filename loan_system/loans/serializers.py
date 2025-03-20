from rest_framework import serializers
from .models import Customer, Loan, Transaction

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(many=True, read_only=True, source='loan_set')  # Add this line 👈

    class Meta:
        model = Customer
        fields = ['id', 'name', 'loans']  # Include loans
