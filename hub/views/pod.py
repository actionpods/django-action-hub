from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
#Models
from ..models.pod import Pod

#Generic Views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .base import BaseCreate

#Permissions
from .decorators.permissions import is_creator_permission_required, public_or_creator_permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

#Complex Lookups
from django.db.models import Q

class Index(ListView):
    template_name = 'actionpods/pods/index.html'
    context_object_name = 'pods'
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Pod.objects.filter(Q(admins=self.request.user) | Q(private=False)).order_by('-created')[:5]
        else:
            return Pod.objects.filter(private=False).order_by('-created')[:5]

@method_decorator(public_or_creator_permission_required(Pod), name='dispatch')
class Detail(DetailView):
    model = Pod
    template_name = 'actionpods/pods/detail.html'

class Create(BaseCreate):
    model = Pod
    template_name = 'actionpods/generic/create.html'
    fields = ['focus', 'team_size', 'private',]

    def form_valid(self, form):
        form.instance.leader = self.request.user
        form.instance.creator = self.request.user
        form.save()
        form.instance.admins.add(self.request.user)
        form.instance.members.add(self.request.user)
        return super(Create, self).form_valid(form)

@method_decorator(is_creator_permission_required(Pod), name='dispatch')
class Update(UpdateView):
    model = Pod
    template_name = 'actionpods/generic/edit.html'
    fields = ['focus', 'team_size', 'private',]
    #permission_required = 'actionpods.change_pod'

@method_decorator(is_creator_permission_required(Pod), name='dispatch')
class Delete(DeleteView):
    model = Pod
    template_name = 'actionpods/generic/delete.html'
    success_url = reverse_lazy('actionpods:pod:index')
