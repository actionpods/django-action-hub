from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

def index(request):
    return render(request, 'actionpods/users/index.html',
        {
        "users":User.objects.all(),
        }
    )

def detail(request, user):
    return render(request, 'actionpods/users/detail.html',
        {
        "user":get_object_or_404(User, id=user),
        }
    )
