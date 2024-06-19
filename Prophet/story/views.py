from django.shortcuts import render

# Create your views here.
def story(request):

    return render (request, 'story.html', {})