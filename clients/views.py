from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def show(request):
    ls = [5, 2, 4, 4]
    lsort = [51, 2, 41, 4]
    lsort.sort()
    return HttpResponse("Hello Django World! {}; Length= {}; Sort= {} ".format(ls, len(ls), lsort))

def client_list(request):
    clients = Client.objects.all()    
    context = {'clients': clients}    
    return render(request, 'clients/client.html', locals())
