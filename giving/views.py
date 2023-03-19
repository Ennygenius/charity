from django.shortcuts import render

# Create your views here.
from .models import *




# Create your views here.

def index(request):
    context = {}
    return render (request, "giving/index.html", context)

def about(request):
    context = {}
    return render (request, "giving/about.html", context)


def appreciation(request):
    context = {}
    return render (request, "giving/appreciation.html", context)


def blog(request):
    context = {}
    return render (request, "giving/blog.html", context)

def contact(request):
    context = {}
    return render (request, "giving/contact.html", context)

def donate(request):
    context = {}
    return render (request, "giving/donate.html", context)

def support(request):
    context = {}
    return render (request, "giving/support.html", context)

def gallery(request):
    context = {}
    return render (request, "giving/gallery.html", context)

def fundraiser(request):
    context = {}
    return render (request, "giving/fundraiser.html", context)

def terms(request):
    context = {}
    return render (request, "giving/terms.html", context)