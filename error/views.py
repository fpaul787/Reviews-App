from django.shortcuts import render
from django.http import HttpResponse

# Settings must be marked to False
# for these pages to show up

def handler404(request, exception):
    # html = "<h1>Wrong Page Dawg</h1>"
    # return HttpResponse(html)
    return render(request, '404.html', status=404)

def handler500(request, exception):
    return render(request, '500.html', status=500)
