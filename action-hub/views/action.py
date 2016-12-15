from django.shortcuts import render, get_object_or_404

from ..models.pod import Action, Pod

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
#Permissions
from .decorators.permissions import is_creator_permission_required, public_or_creator_permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(public_or_creator_permission_required(Pod), name='dispatch')
class Detail(DetailView):
    model = Action
    template_name = 'actionpods/actions/detail.html'

@method_decorator(is_creator_permission_required(Pod), name='dispatch')
class Create(CreateView):
    model = Action
    template_name = 'actionpods/actions/create.html'
    fields = ['title', 'description', 'start_time', 'end_time']
    def get_success_url(self):
        return reverse('actionpods:pod:detail', args=(self.kwargs['pk'],))
    def form_valid(self, form):
        pod = get_object_or_404(Pod, pk = self.kwargs['pk'])
        form.instance.pod = pod
        form.instance.creator = self.request.user
        return super(Create, self).form_valid(form)

class Update(UpdateView):
    model = Action
    template_name = 'actionpods/generic/edit.html'
    fields = ['title']

class Delete(DeleteView):
    model = Action
    template_name = 'actionpods/generic/delete.html'
    success_url = reverse_lazy('actionpods:pod:detail')
