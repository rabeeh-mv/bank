from django import forms
from .models import BankAccount

class AddMoneyForm(forms.Form):
    amount = forms.DecimalField(label='Amount', min_value=0)

class DebitMoneyForm(forms.Form):
    amount = forms.DecimalField(label='Amount', min_value=0)
