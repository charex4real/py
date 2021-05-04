from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'CoreyMs',
        'title': ' Blog Post 1',
        'content': ' First Ever Pass Message',
        'date_posted': 'August 27, 2018'
    },
     {
        'author': 'Jane Doe',
        'title': ' Blog Post 2',
        'content': ' Second Ever Pass Message',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
   #return HttpResponse('<h1>Blog Home </h1>') 
   context = {
       'posts' : Post.objects.all(),
       'title' : 'Home Page'
   }
   return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog Home </h1>') 
    return render(request, 'blog/about.html')

# Create your views here.
