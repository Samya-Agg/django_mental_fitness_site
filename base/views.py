from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .models import profile



# Create your views here.
def index(request):
    return render(request,"home.html")

def loginPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
          messages.error(request,"Invalid username")
          return redirect('/user/login/')
    
        user=authenticate(username=username,password=password)

        if user is None:
          messages.error(request,"Invalid password")
          return redirect('/user/login/')
        else:
          login(request,user)
          return redirect('/user/chat/')
    
    return render(request,'login.html')
   

def reg(request):

    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.error(request,"username taken")
            return redirect('/user/register/')

        user=User.objects.create(
         first_name=first_name,
         last_name=last_name,
         username=username
        )
        user.set_password(password)
        user.save()

        messages.info(request,"Account created")

    return render(request,'register.html')

def logoutpage(request):
    logout(request)
    return redirect('loginPage')

def chatting(request):
    users = User.objects.exclude(username=request.user.username)
    sender=request.user
    recipient = None
    chats = []

    if request.method == "POST":
        recipient_username = request.POST.get('recipient')
        recipient = get_object_or_404(User, username=recipient_username)
        chat.objects.create(
            user=request.user,
            recipient=recipient,
            message=request.POST.get('body')
        )
        return redirect('chatting')  # Replace with the appropriate URL name

    if 'recipient' in request.GET:
        recipient_username = request.GET.get('recipient')
        recipient = get_object_or_404(User, username=recipient_username)

    if recipient:
        chats = chat.objects.filter(
            Q(sender=request.user, recipient=recipient) |
            Q(sender=recipient, recipient=request.user)
        )
    #all_chats = chat.objects.all().order_by('time')
    total=chat.objects.all()
    context = {
        "messages": chats,
        "users": users,
        "recipient": recipient,
        "total":total,
    }
    return render(request, "chat.html", context)
   #chats=chat.objects.filter(user=request.user)
   #recipient=request.POST.get('recipient')
   ##chats = chat.objects.filter(
        #models.Q(user=request.user, recipient=recipient) |
        #models.Q(user=recipient, recipient=request.user)
    #).order_by('time')

   #if request.method=="POST":
    #  msg=chat.objects.create(
     #    user=request.user,
      #   message=request.POST.get('body'),
       #  recipient=recipient
      #)
      #msg.save()
      #return redirect('/user/chat')
   #context={"messages":chats}
   #return render(request,"chat.html",context)


def account(request):
   if request.method=="POST":
        description=request.POST.get('description')
        age=request.POST.get('age')
        playlist=request.POST.get('playlist')
        contact=request.POST.get('contact')

        prof=profile.objects.create(
           user=request.user,
           description=description,
           age=age,
           playlist=playlist,
           contact=contact,
        )
        prof.save()

   return render(request,'profile.html')