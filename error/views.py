from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def default(request, exception):
    html = "<h1>Wrong Page Dawg</h1>"
    # return HttpResponse(html)
    return render(request, '404.html', status=404)
