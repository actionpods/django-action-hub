from django.shortcuts import render, get_object_or_404

from ..models.campaign import Campaign

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse, reverse_lazy
#Permissions
from .decorators.permissions import is_creator_permission_required, public_or_creator_permission_required
from django.utils.decorators import method_decorator

from .base import BaseCreate

#Complex Lookups
from django.db.models import Q

class Index(ListView):
    template_name = 'actionpods/campaigns/index.html'
    context_object_name = 'campaigns'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Campaign.objects.filter(Q(admins=self.request.user) | Q(private=False)).order_by('-created')[:5]
        else:
            return Campaign.objects.filter(private=False).order_by('-created')[:5]

@method_decorator(public_or_creator_permission_required(Campaign), name='dispatch')
class Detail(DetailView):
    model = Campaign
    template_name = 'actionpods/campaigns/detail.html'

class Create(BaseCreate):
    model = Campaign
    fields = ['title', 'private',]

@method_decorator(is_creator_permission_required(Campaign), name='dispatch')
class Update(UpdateView):
    model = Campaign
    template_name = 'actionpods/generic/edit.html'
    fields = ['title', 'private',]

@method_decorator(is_creator_permission_required(Campaign), name='dispatch')
class Delete(DeleteView):
    model = Campaign
    template_name = 'actionpods/generic/delete.html'
    fields = ['title',]
    success_url = reverse_lazy('actionpods:campaign')


##blog

from hub.models.campaign import CampaignBlog

def blog_index(request, pk):
    return render(request, 'actionpods/campaign/blog/index.html',
        {
        'posts': CampaignBlog.objects.filter(campaign_id=pk).order_by('-posted', 'title')[:5],
        }
    )

#Returns the (hopefully) singular post for that blog
def view_post(request, slug):
    return render(request, 'blog/index.html',
        {
        'posts': Blog.objects.filter(slug=slug).order_by('-posted', 'title')[:5],
        'slug': slug,
        }
    )
