from django.urls import path
from . import views

urlpatterns = [
    path('bank-account-details/', views.bank_account_details, name='bank_account_details'),
     path('add-transactions/', views.add_transaction, name='view_transactions'),
     path('transactions/', views.view_transactions, name='view_transactions'),
]
