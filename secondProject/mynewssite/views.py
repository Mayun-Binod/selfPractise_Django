from django.shortcuts import render

# Create your views here.
def newssitehome(request):
    return render(request,'mynewssite/newssite.html')

def politics(request):
    return render(request,'mynewssite/politics.html')

def sports(request):
    return render(request,'mynewssite/sports.html')

def entertainment(request):
    return render(request,'mynewssite/entertainment.html')