from django.shortcuts import render, get_object_or_404

from ..models.pod import Pod

def index(request):
    return render(request, 'actionpods/personal/dashboard.html',
        {
        "pods":Pod.objects.filter(members__in=[request.user.id]),
        }
    )
