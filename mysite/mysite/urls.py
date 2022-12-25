from django.contrib import admin
from django.urls import include, path
#the include fucntion allows referencing other
# URLConfs like the one inside the polls app
# projects are made up of different apps
# every app is a portion of the project that you are building out
# i think its kinda like components in react
# whenever Django encounters an include(), it chops off whatever part of the URL matched up to that point and sned the remaining string to the included URLconf for furuther processing
# this allows you to be more versatile with the url
# since polls are in their own URLconf (polls/urls.py)
# they can be placed under "/polls/" or under "/fun_polls" or under "/content/polls/" or any other path root and the app will still work I think this will be helpful for the post app I will ahve to make for the ratemytoilet application
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
