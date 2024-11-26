from django.urls import path
from mynewssite import views

urlpatterns = [
    path('newssite/',views.newssitehome,name="home"),
    path('sports/',views.sports,name="sports"),
    path('politics/',views.politics,name="politics"),
    path('entertainment/',views.entertainment,name="entertainment"),
]