from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    date=datetime.datetime.now()
    msg="Hello,Guest !!!"
    h=int(date.strftime("%H"))
    if h>12:
        msg+="Good Morning."
    elif h<16:
        msg+="Good Afternoon."
    elif h<20:
        msg+="Good Evening."
    else:
        msg="Hello Guest,Good Night."

    context={"insert_date":date,"insert_msg":msg}
    return render(request,'firstApp/html/index.html',context=context)

   
