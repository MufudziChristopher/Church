from django.shortcuts import render

# Create your views here.
def teach(request):

    return render (request, 'teach.html', {})

def scroll(request):

    return render (request, 'scroll.html', {})