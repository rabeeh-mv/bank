from django.shortcuts import render ,redirect
from .forms import signUpform,LoginForm
from django.contrib.auth import authenticate, login as authlogin 
# Create your views here.
from django.contrib.auth.decorators import login_required
from banking.models import BankAccount, Transaction

# @login_required
def home(request):
    return render(request, 'homepage.html', )
def bnak_account(request):
    # Get the user's bank account
    # user_account = BankAccount.objects.get(owner=request.user)
    return render(request, 'index.html', )
    

def register(request):
    msg = None
    if request.method == 'POST':
        form=signUpform(request.POST)
        if form.is_valid():
            user= form.save()
            msg= 'user created'
            return redirect('login')
        else:
            msg = 'user not created'
    else:
        form = signUpform()        
    return render(request, 'register.html',{'form':form, 'msg':msg})

def login(request):
    form = LoginForm(request.POST or None)
    msg= None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username= username, password=password)
            if user is not None and user.is_admin:
                authlogin(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_student:
                authlogin(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                authlogin(request, user)
                return redirect('techer')
            else:
                msg= 'invalid credentials'
        else:
            msg= 'error validate form'
    return render(request, 'login.html',{'form':form, 'msg':msg})
    
    
def adminpage(request):
    return render(request, 'admin.html')

def techer(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')