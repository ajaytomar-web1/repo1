from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def dateTimeInfo(request):
    msg='<h1 style="color:red"> The current date and time is : Now the server time is '+'<hr>'+'</h1>'
    return HttpResponse(msg + str(datetime.datetime.now()));
