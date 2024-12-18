from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record

# Create your views here.

# homepage

def home(request):

    return render(request, 'crmApp/index.html')

# register user

def register(request):
     form = CreateUserForm()

     if request.method == 'POST':
          
          form = CreateUserForm(request.POST)

          if form.is_valid():
                
                form.save()

                return redirect('login')

     context = {'form':form}

     return render(request, 'crmApp/register.html', context=context)

# login a user

def login(request):
     form = LoginForm()

     if request.method == 'POST':
          
          form = LoginForm(request, data=request.POST)

          if form.is_valid():
               
               username = request.POST.get('username')
               password = request.POST.get('password')

               user = authenticate(request, username=username, password=password)

               if user is not None:
                    
                    auth.login(request, user)

                    return redirect('dashboard')

     context = {'form':form}

     return render(request, 'crmApp/login.html', context=context)




# Dashboard
@login_required(login_url='login')
def dashboard(request):

     my_records = Record.objects.all()

     context = {'records':my_records}

     return render(request, 'crmApp/dashboard.html', context=context)


# create a record
@login_required(login_url=login)
def create_record(request):
      form = CreateRecordForm()

      if request.method == "POST":
           
           form = CreateRecordForm(request.POST)

           if form.is_valid():
                
                form.save()

                return redirect('dashboard')

      context = {'form':form}

      return render(request, 'crmApp/create.html', context=context)



#  update a record
@login_required(login_url=login)
def update_record(request, pk):
     record = Record.objects.get(id=pk)

     form = UpdateRecordForm(instance=record)

     if request.method == "POST":

          form = UpdateRecordForm(request.POST, instance=record)

          if form.is_valid():

               form.save()

               return redirect('dashboard')
          
     context = {'form':form}
     return render(request, 'crmApp/update.html', context=context)



#  view a record
@login_required(login_url=login)
def view_record(request, pk):
      record = Record.objects.get(id=pk)

      context = {'record':record}


      return render(request, 'crmApp/view.html', context=context)


#  delete a record
@login_required(login_url=login)
def delete_record(request, pk):
      record = Record.objects.get(id=pk)

      record.delete()


      return render(request, 'crmApp/dashboard.html')


# logout a user

def logout(request):

     auth.logout(request)

     return redirect('login')