from django.shortcuts import render
from .models import ShortenedURL
from .forms import CreateShortenedURL
from datetime import datetime
import random
import string
import requests
import os

def home(request):

    global domainPath 
    domainPath = request.build_absolute_uri()    
    return render(request, "home.html")


def redirect(request, url):

    current_obj = ShortenedURL.objects.filter(shortenedURL = url)
    if len(current_obj) == 0:
        return render(request, "not_found.html")

    context = {"obj": current_obj[0]}

    return render(request, 'redirect.html', context)


def create_short_URL(request):

    if request.method == "POST":

        form = CreateShortenedURL(request.POST)

        if form.is_valid():
            
            originalWebsite = form.cleaned_data["originalURL"]         
            allowedChars = list(string.ascii_letters)
            allowedChars.append("_") 
            shortURL = ""

            for i in range(10):
                shortURL += random.choice(allowedChars)

            while len(ShortenedURL.objects.filter(shortenedURL = shortURL)) > 0:

                for i in range(10):
                    shortURL += random.choice(allowedChars)

            date = datetime.now()

            if domainPath[len(domainPath) - 1] is not "/":
                short = domainPath + "/" + shortURL
                
            else:
                short = domainPath + shortURL

            urlModel = ShortenedURL(originalURL = originalWebsite, shortenedURL = shortURL, shortened = short, dateOfCreation = date)
            urlModel.save()

            return render(request, 'short_url_result.html', {'shortenedURL': short})
        
        else:
            return render(request, 'not_found.html')
    
    else:

        form = CreateShortenedURL()
        context = {'form': form}

        return render(request, 'create_short_URL.html', context)