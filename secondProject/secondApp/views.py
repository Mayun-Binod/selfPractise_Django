from django.shortcuts import render

# Create your views here.
def secondindex(request):
    my_dict={"name":"Binod","age":23}
    return render(request,'secondApp/html/index.html',context=my_dict)
