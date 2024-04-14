from django.db import models
from account.models import user  # Import your custom user model

class AdminProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Admin Profile"

class StudentProfile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Student Profile"

class BankAccount(models.Model):
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.account_number

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update bank account balance based on transaction type
        if self.transaction_type == 'credit':
            self.account.balance += self.amount
        elif self.transaction_type == 'debit':
            self.account.balance -= self.amount
        self.account.save()
