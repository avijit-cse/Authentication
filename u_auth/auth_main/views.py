from auth_main.models import userInfo
from django.shortcuts import render
from django.http import HttpResponse
from auth_main.forms import userfrom,userInfofrom



from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django .urls import reverse
from django.contrib.auth.models import User



def index(request):
    dict={}

    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_basic_info=User.objects.get(pk=user_id)
        user_moreinfo= userInfo.objects.get(user__pk=user_id)
        dict={'user_basic_info':user_basic_info,'user_moreinfo':user_moreinfo}
    
    return render(request,'index.html',context=dict)

def registartion(request):
    registered=False
    if request.method=='POST':
        user_form=userfrom(data=request.POST)
        user_info= userInfofrom(data=request.POST)

        if user_form.is_valid() and user_info.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            userInfo=user_info.save(commit=False)
            userInfo.user=user
            if 'profile_pic' in request.FILES:
                userInfo.profile_pic=request.FILES['profile_pic']

            userInfo.save()
            registered=True

        
      
    else:
        user_form=userfrom()
        user_info= userInfofrom()
    diction={'user_form':user_form,'user_info':user_info,'register':registered}

    
    return render(request,'registratiom.html',context=diction)


def Login_page(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username)
        print(password)
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('auth_main:index'))
            else:
                return HttpResponse("this  acccount are not active")

        else:
            return HttpResponse("login detais is worng")            

    diction={'name': 'Login Page'}
    return render (request,'Login.html',context=diction)


'''def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        print(username)
        print(password)'''

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_main:index'))

