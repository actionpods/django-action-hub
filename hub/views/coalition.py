from django.shortcuts import render, get_object_or_404

from ..models.coalition import Coalition, CoalitionBlog

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .base import BaseCreate

from django.urls import reverse, reverse_lazy

#Permissions
from .decorators.permissions import is_creator_permission_required, public_or_admin_permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

#Complex Lookups
from django.db.models import Q

class Index(ListView):
    template_name = 'actionpods/coalitions/index.html'
    context_object_name = 'coalitions'

    def get_queryset(self):
        return Coalition.objects.filter(Q(admins=self.request.user) | Q(private=False)).order_by('-created')[:5]

@method_decorator(public_or_admin_permission_required(Coalition), name='dispatch')
class Detail(DetailView):
    model = Coalition
    template_name = 'actionpods/coalitions/detail.html'


class Create(BaseCreate):
    model = Coalition
    template_name = 'actionpods/generic/create.html'
    fields = ['title', 'private',]
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(Create, self).form_valid(form)

@method_decorator(is_creator_permission_required(Coalition), name='dispatch')
class Update(UpdateView):
    model = Coalition
    template_name = 'actionpods/generic/edit.html'
    fields = ['title', 'private',]

@method_decorator(is_creator_permission_required(Coalition), name='dispatch')
class Delete(DeleteView):
    model = Coalition
    template_name = 'actionpods/generic/delete.html'
    success_url = reverse_lazy('actionpods:coalition')
