from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from Application.forms import UserForm,TicketsNeeded
from django.contrib.auth.decorators import login_required
from .models import Event
from django.utils import timezone
from django.contrib import messages

# Create your views here.

# login and register

def loginUser(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           
            login(request, user)
            return redirect('home')
       
        else :     
            return render(request, 'loginUser.html')
        
     return render(request, 'loginUser.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')            
            return redirect('loginUser')
        else:
            form = UserForm()

    context={'form': UserForm}
    return render(request, 'register.html',context )

@login_required(login_url='/')
def home(request):
    username = request.user.username
    today = timezone.now().date()
    Events = Event.objects.filter(EventDate = today)
    return render(request, 'home.html',{'Events': Events, 'username': username})

@login_required(login_url='/')
def organiseevent(request):
    if request.method == 'POST':
        EventName = request.POST.get('EventName')
        EventVenue = request.POST.get('EventVenue')
        EventDescription = request.POST.get('EventDescription')
        EventDate = request.POST.get('EventDate')
        EventTime = request.POST.get('EventTime')
        EventAvailableTickets = request.POST.get('EventAvailableTickets')
        print(EventAvailableTickets)
        Events = Event(EventName=EventName, EventVenue=EventVenue, EventDescription=EventDescription, EventDate=EventDate, EventTime=EventTime, EventAvailableTickets= EventAvailableTickets)
        Events.save()
        return redirect('home')
    return render(request, 'organise.html')

@login_required(login_url='/')
def UpdatedEvent(request, Event_id):
    if request.method == 'POST':
        TicketsNeeded = int(request.POST.get('TicketsNeeded'))
        Events = Event.objects.get(pk = Event_id)
        if Events.EventAvailableTickets >= TicketsNeeded :
            Events.EventAvailableTickets -= TicketsNeeded
            Events.save()
            return redirect('home')
        else :
            return redirect('home')
    return redirect('home') 

@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    return redirect('loginUser')
