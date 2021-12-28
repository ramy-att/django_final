#imports
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #create form
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from .forms import UserRegistForm, UpdateUserForm,ProfileUpdateForm

# Create your views here.
#request creates an HttpRequest object containing info abt the request

def register(request):
    if request.method == 'POST':
        form= UserRegistForm(request.POST) #Create form using POST
        if form.is_valid(): #checks if valid, built in, check password, username exists, etc..
            form.save() #hashes password, saves user (becomes visible in admin page)
            username=form.cleaned_data.get('username')
            messages.success(request,"Account created for {}".format(username)+ "You can now log in!") #Success message
            return redirect('login')
    else: #if not valid
        form= UserRegistForm()
    return render(request,'users/register.html',{'form':form})

@login_required # decorator to require login
def profile(request):
    if request.method == 'POST': #check if POST route
        u_form= UpdateUserForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() #save info
            p_form.save() #save info
            messages.success(request,"Account updated!") #Success message
            return redirect('profile') #send GET request

    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    #check validity of BOTH forms:

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)
