from django.shortcuts import render
from . import read 
# Create your views here.
def loadserial(request):
    data=[]
    read.load(data)
    print(data)
    my_dict={'insert_me':data}
    return render(request,'serialLoad/loadPage.html',context=my_dict)
