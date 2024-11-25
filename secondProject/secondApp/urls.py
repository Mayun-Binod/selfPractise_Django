from django.urls import path
from secondApp import views
urlpatterns = [
    path('second/',views.secondindex),

]