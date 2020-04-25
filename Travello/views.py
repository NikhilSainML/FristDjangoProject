from django.shortcuts import render
from .models import Destination
# Creatws here.
def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html',{'dests':dests})
