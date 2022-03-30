from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#handles varioius webpages

def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)     #User model object
    # return HttpResponse("<h>Hello World</h>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h>Contact Page</h>")
    return render(request, "contact.html", {})

def social_view(request, *args, **kwargs):
    # return HttpResponse("<h>Social Page</h>")
    return render(request, "social.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us...template context",
        "my_number": 1223,
        "my_list" : [123,456,7753]

    }
    # return HttpResponse("<h>Social Page</h>")
    return render(request, "about.html", my_context)

