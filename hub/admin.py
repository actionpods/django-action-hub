from django.contrib import admin
from hub.models.pod import Pod, Focus, Action
from hub.models.campaign import Campaign, CampaignBlog
from hub.models.relationships import Invitation, Blocking

from django import forms
from tinymce.widgets import TinyMCE

### Pods Admin Models ###

class PodAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), error_messages={'required': 'n'})
    class Meta:
        model = Pod
        fields = '__all__'

class PodAdmin(admin.ModelAdmin):
    exclude = ['creator', 'created']
    form = PodAdminForm
    list_display = ["id", "creator", "created", "focus", "private"]
    list_display_links = ('id', 'creator')
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()

class FocusAdmin(admin.ModelAdmin):
    exclude = ['slug']

class PodInline(admin.StackedInline):
    model = Pod

admin.site.register(Pod, PodAdmin)
admin.site.register(Focus, FocusAdmin)

### Action Admin Models

class ActionAdminForm(forms.ModelForm):
    description = forms.CharField()
    class Meta:
        model = Action
        fields = '__all__'

class ActionAdmin(admin.ModelAdmin):
    exclude = ['creator', 'created', 'slug']
    form = ActionAdminForm
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()

class CampaignAdminForm(forms.ModelForm):
    #description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Campaign
        fields = '__all__'

class CampaignAdmin(admin.ModelAdmin):
    exclude = ['creator', 'created', 'slug']
    list_display = ["id", "title", "creator", "created", "private"]
    list_display_links = ('id','title', 'creator')
    form = CampaignAdminForm
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()

admin.site.register(Action, ActionAdmin)
admin.site.register(Campaign, CampaignAdmin)

class CampaignBlogAdminForm(forms.ModelForm):
    #Set the editor to a WYSIWYG or Markdown
    #NOTE: Be sure to edit the template to reflect a change.
    body = forms.CharField(widget=TinyMCE())
    class Meta:
        model = CampaignBlog
        fields = '__all__'

class CampaignBlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    form = CampaignBlogAdminForm
    prepopulated_fields = {
                           'slug': ('title',),
                           }

admin.site.register(CampaignBlog, CampaignBlogAdmin)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ["id", "campaign", "pod", "added"]


class InvitationAdmin(admin.ModelAdmin):
    list_display = ["id", "campaign", "pod", "sent"]


class BlockingAdmin(admin.ModelAdmin):
    list_display = ["id", "campaign", "pod", "added"]

admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Blocking, BlockingAdmin)
