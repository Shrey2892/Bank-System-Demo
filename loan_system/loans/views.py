from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Loan, Transaction
from .serializers import LoanSerializer, TransactionSerializer,CustomerSerializer
from .utils import calculate_loan
from rest_framework import status

# ========== HTML TEMPLATE VIEWS ==========

def lend_page(request):
    return render(request, 'loans/lend.html')

def payment_page(request):
    return render(request, 'loans/payment.html')

def overview_page(request):
    return render(request, 'loans/overview.html')

def ledger_page(request):
    return render(request, 'loans/ledger.html')

def main(request):
    return render(request,'loans/base.html')

# ========== API VIEWS ==========


# API View to create customer (POST)

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# HTML View to show form
def customer_form(request):
    return render(request, 'loans/customer_form.html')

@api_view(['GET'])
def all_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)




@csrf_exempt
@api_view(['POST'])
def lend(request):
    customer_id = request.data['customer_id']
    principal = float(request.data['loan_amount'])
    period = int(request.data['loan_period'])
    rate = float(request.data['rate_of_interest'])
    interest, total_amount, monthly_emi = calculate_loan(principal, period, rate)
    customer = Customer.objects.get(id=customer_id)
    loan = Loan.objects.create(
        customer=customer,
        principal_amount=principal,
        loan_period=period,
        rate_of_interest=rate,
        total_interest=interest,
        total_amount=total_amount,
        monthly_emi=monthly_emi
    )
    serializer = LoanSerializer(loan)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def payment(request):
    loan_id = request.data['loan_id']
    payment_type = request.data['payment_type']
    loan = Loan.objects.get(id=loan_id)
    if payment_type == 'EMI':
        amount = loan.monthly_emi
        loan.amount_paid += amount
        loan.emis_paid += 1
    else:
        amount = float(request.data['amount'])
        loan.amount_paid += amount
    loan.save()
    Transaction.objects.create(loan=loan, transaction_type=payment_type, amount=amount)
    return Response({'message': 'Payment successful'})

@api_view(['GET'])
def ledger(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    transactions = Transaction.objects.filter(loan=loan)
    serializer = TransactionSerializer(transactions, many=True)
    balance = loan.total_amount - loan.amount_paid
    return Response({
        'transactions': serializer.data,
        'principal_amount': loan.principal_amount,
        'total_amount': loan.total_amount,
        'amount_paid': loan.amount_paid,
        'balance': balance,
        'monthly_emi': loan.monthly_emi,
        'emis_left': (loan.loan_period * 12) - loan.emis_paid
    })

@api_view(['GET'])
def overview(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    loans = Loan.objects.filter(customer=customer)
    loans_list = []
    for loan in loans:
        loans_list.append({
            'loan_id': loan.id,
            'principal_amount': loan.principal_amount,
            'total_amount': loan.total_amount,
            'monthly_emi': loan.monthly_emi,
            'total_interest': loan.total_interest,
            'amount_paid': loan.amount_paid,
            'emis_left': (loan.loan_period * 12) - loan.emis_paid
        })
    return Response({
        'customer_id': customer.id,
        'customer_name': customer.name,
        'loans': loans_list
    })
