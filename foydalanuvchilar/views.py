from django.shortcuts import render
from django.http import HttpResponse
from .models import Users


def user_view(request , id):
    user_view = Users.username.get(id = id)

    context = {
    'user_view' : user_view
    }

    return render(request,template_name='users.html', context=context)