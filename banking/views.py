from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .models import BankAccount, AdminProfile, StudentProfile, Transaction
from .forms import AddMoneyForm, DebitMoneyForm

@login_required
def bank_account_details(request):
    if request.user.is_superuser:
        try:
            admin_profile = AdminProfile.objects.get(user=request.user)
            bank_account = BankAccount.objects.get(owner=request.user)
            return render(request, 'banking/admin_bank_account_details.html', {'admin_profile': admin_profile, 'bank_account': bank_account})
        except AdminProfile.DoesNotExist or BankAccount.DoesNotExist:
            # Handle the case where AdminProfile or BankAccount does not exist for the user
            return HttpResponseBadRequest("Admin profile or Bank account not found")
    else:
        try:
            student_profile = StudentProfile.objects.get(user=request.user)
            bank_account = BankAccount.objects.get(owner=request.user)
            return render(request, 'banking/student_bank_account_details.html', {'student_profile': student_profile, 'bank_account': bank_account})
        except StudentProfile.DoesNotExist or BankAccount.DoesNotExist:
            # Handle the case where StudentProfile or BankAccount does not exist for the user
            return HttpResponseBadRequest("Student profile or Bank account not found")

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            transaction_type = form.cleaned_data['transaction_type']
            account = BankAccount.objects.get(owner=request.user)

            # Create a new transaction record
            Transaction.objects.create(account=account, amount=amount, transaction_type=transaction_type)

            return redirect('transaction_history')
    else:
        form = AddMoneyForm()
    return render(request, 'transaction_form.html', {'form': form})

@login_required
def view_transactions(request):
    if request.user.is_superuser:
        return HttpResponseBadRequest("Unauthorized access")  # Only students can view transactions
    
    try:
        student_profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        # Handle the case where StudentProfile does not exist for the user
        return HttpResponseBadRequest("Student profile not found")

    transactions = Transaction.objects.filter(account__owner=request.user)
    
    # Get the user's bank account object
    user_account = BankAccount.objects.get(owner=request.user)

    # Get the total balance from the user's bank account
    total_balance = user_account.balance

    return render(request, 'transactions.html', {'transactions': transactions, 'total_balance': total_balance, 'user_account': user_account})
