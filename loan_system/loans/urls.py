from django.urls import path
from .views import lend, payment, ledger, overview
from .views import lend_page, payment_page, overview_page, ledger_page,customer_form,create_customer,main,all_customers

urlpatterns = [
    # API endpoints
    
    path('create-customer/',create_customer),
    path('lend/', lend),
    path('payment/', payment),
    path('ledger/<int:loan_id>/', ledger),
    path('overview/<int:customer_id>/', overview),
    path('customers/',all_customers),

    # HTML pages
    path('',main),
    path('create-customer-form/',customer_form),
    path('lend-page/', lend_page, name='lend-page'),
    path('payment-page/', payment_page, name='payment-page'),
    path('overview-page/', overview_page, name='overview-page'),
    path('ledger-page/', ledger_page, name='ledger-page'),
]
