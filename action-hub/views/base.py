from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseCreate(LoginRequiredMixin, CreateView):
    template_name = 'actionpods/generic/create.html'
    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        form.instance.admins.add(self.request.user)
        return super(BaseCreate, self).form_valid(form)
