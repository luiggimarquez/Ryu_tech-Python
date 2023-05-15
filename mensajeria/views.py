from django.shortcuts import render
from django.contrib.auth.models import User


def usersChat(request):

    users= User.objects.all()
    return render(request, 'mensajeria/index.html',{'usuarios':users})
