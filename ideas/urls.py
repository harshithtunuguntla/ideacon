
from os import name
from django.urls import path

from . import views


urlpatterns = [
    path('',views.home_page_view,name="home_page"),
    path('contribute',views.contribute_view,name="contribute"),
    path('add/',views.add_idea_view,name="add idea"),
    path('ideaconapi/',views.api_view,name="api"),
    path('subscribe/',views.subscribe_view,name="subscribe"),
    path('subscription/',views.subscribtion_view,name="subscribtion"),
    path('ideaconapi/idea',views.api_idea_view,name="idea"),






    ]