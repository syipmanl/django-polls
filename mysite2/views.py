from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("<p>Hello world<p>")

def lets_start(request):
    return HttpResponse("here we are")

def current_datetime(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = "<html><body>It is now %s.</body></html>" % (now)
    return HttpResponse(html)

