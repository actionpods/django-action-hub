from django.contrib import admin
from hub.models.pod import Pod, PodCategory, Action, Role
from hub.models.coalition import Coalition, CoalitionBlog
from hub.models.campaign import Campaign
from hub.models.relationships import Invitation, Blocking

from django import forms
from ckeditor.widgets import CKEditorWidget


### Pods Admin Models ###

class PodAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Pod
        fields = '__all__'

class PodAdmin(admin.ModelAdmin):
    exclude = ['creator', 'created']
    form = PodAdminForm
    list_display = ["id", "title", "creator", "created", "private"]
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()

class PodCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PodInline(admin.StackedInline):
    model = Pod

admin.site.register(Pod, PodAdmin)
admin.site.register(PodCategory, PodCategoryAdmin)

### Action Admin Models
class RoleInline(admin.StackedInline):
    model = Role

class ActionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Action
        fields = '__all__'

class ActionAdmin(admin.ModelAdmin):
    exclude = ['creator', 'created']
    form = ActionAdminForm
    inlines = [RoleInline,]
    prepopulated_fields = {'slug': ('title',), }
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()

class CoalitionAdminForm(forms.ModelForm):
    #description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Coalition
        fields = '__all__'

class CoalitionAdmin(admin.ModelAdmin):
    exclude = ['creator', 'created']
    form = CoalitionAdminForm
    list_display = ["id", "title", "creator", "created", "private"]
    prepopulated_fields = {
                           'slug': ('title',),
                           }
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
    exclude = ['creator', 'created']
    list_display = ["id", "title", "creator", "created", "private"]
    form = CampaignAdminForm
    prepopulated_fields = {
                           'slug': ('title',),
                           }
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()

admin.site.register(Role)
admin.site.register(Action, ActionAdmin)
admin.site.register(Coalition, CoalitionAdmin)
admin.site.register(CoalitionBlog)
admin.site.register(Campaign, CampaignAdmin)



class RelationshipAdmin(admin.ModelAdmin):
    list_display = ["id", "coalition", "pod", "added"]


class InvitationAdmin(admin.ModelAdmin):
    list_display = ["id", "coalition", "pod", "sent"]


class BlockingAdmin(admin.ModelAdmin):
    list_display = ["id", "coalition", "pod", "added"]

admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Blocking, BlockingAdmin)
