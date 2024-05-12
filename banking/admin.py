from django.contrib import admin
from .models import BankAccount, AdminProfile, StudentProfile,Transaction,TotalMoney

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'owner', 'balance')

admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(AdminProfile)
admin.site.register(StudentProfile)
admin.site.register(Transaction)
admin.site.register(TotalMoney)
