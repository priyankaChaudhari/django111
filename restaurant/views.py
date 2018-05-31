from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    html_ = """<!DOCTYPE html>
    <html lang=en>
    <head></head>
    <body>
    <h1>Hello World!!!!!</h1>
    </body>
    <html>
    
    """
    #    return HttpResponse(html_)
    return render(request, "base.html", {})
