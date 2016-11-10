from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    if 'activity' not in request.session:
            request.session['activity'] = ""
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "ninjagold/index.html")

def gold(request, location):
    if (location == "farm"):
        gold = random.randint(10, 20)
        request.session['gold'] += gold
        activity = "Earned " + str(gold) + " gold from the farm! " + str(datetime.datetime.now()) + "\n"
        request.session['activity'] += activity
    if (location == "cave"):
        gold = random.randint(5,10)
        request.session['gold'] += gold
        activity = "Earned " + str(gold) + " gold from the cave! " + str(datetime.datetime.now()) + "\n"
        request.session['activity'] += activity
    if (location == "house"):
        gold = random.randint(2,5)
        request.session['gold'] += gold
        activity = "Earned " + str(gold) + " gold from the house! " + str(datetime.datetime.now()) + "\n"
        request.session['activity'] += activity
    if (location == "casino"):
        gold = random.randint(-50,50)
        request.session['gold'] += gold
        if gold > 0:
            activity = "Earned " + str(gold) + " gold from the casino! " + str(datetime.datetime.now()) + "\n"
            request.session['activity'] += activity
        else:
            activity = "Lost " + str(gold) + " gold from the casino! " + str(datetime.datetime.now()) + "\n"
            request.session['activity'] += activity
    return redirect("/")
