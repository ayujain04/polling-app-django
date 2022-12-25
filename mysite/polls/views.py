from django.http import HttpResponse 

#making the first view
def index(request): 
    return HttpResponse("Hello, world. You're at the polls index.")

