from django.shortcuts import render
from .forms import CreateUserForm, LoginForm

# Create your views here.

def home(request):

    return render(request, 'crmApp/index.html')

def register(request):
     form = CreateUserForm()

     if request.method == 'POST':
          
          form = CreateUserForm()

          if form.is_valid():
                
                form.save()

     context = {'form':form}

     return render(request, 'crmApp/register.html', context)