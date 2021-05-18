from django.http import HttpResponse

def homepage(request):
    html='hello'
    return HttpResponse(html)