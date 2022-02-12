from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ideas_store, subscribe
import random
import json
# Create your views here.


# idea1 = ideas_store()

# idea1.title = "Idea1"
# idea1.description = "something"

# idea1.name = "harshith"
# idea1.email = "harshith@gmail.com"
# idea1.handle = "harshithtunuguntla"


# idea2 = ideas_store()

# idea2.title = "Idea1"
# idea2.description = "something"

# idea2.name = "harshith"
# idea2.email = "harshith@gmail.com"
# idea2.handle = "harshithtunuguntla"

# ideas_list = [idea1,idea2]





def home_page_view(request):

    ideas_list = ideas_store.objects.filter(is_reviewd="True")
    return render(request,"idea_display.html",{"ideas":ideas_list})


def contribute_view(request):
    return render(request,"idea_contribution.html")

def add_idea_view(request):

    if request.method=="POST":

        print("inside post")
        idea_title = request.POST['idea_title']
        idea_description = request.POST['idea_description']

        person_name = request.POST['person_name']
        person_email = request.POST['person_email']
        person_handle = request.POST['person_handle']


        new_idea = ideas_store()
        new_idea.title = idea_title
        new_idea.description=idea_description
        new_idea.name=person_name
        new_idea.email=person_email
        new_idea.handle=person_handle

        new_idea.save()




    return redirect('/')

def api_view(request):
    return render(request,"ideaconapi.html")

    
def subscribe_view(request):

    return render(request,"subscribe.html")


def subscribtion_view(request):

    if request.method == "POST":
        person_name = request.POST['person_name']
        person_email = request.POST['person_email']

        new_subscription = subscribe()
        new_subscription.name = person_name
        new_subscription.email = person_email

        new_subscription.save()

    return redirect('/')


def api_idea_view(request):


    random_idx = random.randint(0, ideas_store.objects.count() - 1)
    random_obj = ideas_store.objects.all()[random_idx]


    response_data = {}
    response_data['idea_title'] = random_obj.title
    response_data['idea_description'] = random_obj.description
    response_data['contributed_by'] = random_obj.handle

    return HttpResponse(json.dumps(response_data), content_type="application/json")
