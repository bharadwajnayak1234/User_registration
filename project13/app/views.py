from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login


# Create your views here.
def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO': EUFO, 'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            message =f"Hello{UFDO.cleaned_data.get('first_name')} your registration is successful Thank your for Register our app \n \n Thanks Regards"
            email=UFDO.cleaned_data.get('email')
            send_mail(
                'registration successful',
                message,
                'bharadwaj.nayak2019@gift.edu.in',
                [email],
                fail_silently=False
            )
            return HttpResponse("registraion Done")
        return HttpResponse("Invalid data")
    return render (request ,"register.html",d)


def user_login(request):
    if request.method == "POST":
        username =request.POST.get("un")
        pw =request.POST.get("pw")
        user = authenticate(username=username ,password =pw)
        if user is not None:
            login(request,user)
            request.session['username'] =username
            return render(request ,"home.html",{'user':user})
        else:    
            return HttpResponse('Invalid Data')      
    return render(request,"user_login.html")


def user_profile(request):
    try:
        un =request.session['username']
        uo = User.objects.get(username=un)
        d={'uo':uo}
        request.session.modified =True
        return render (request,"user_profile.html",d)
    except:
        return render(request,'user_login.html')

        



def home(request):
    request.session.modified =True
    return render(request,"home.html")

