from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .models import ParticipantProfile, OrganizerProfile
from .forms import ParticipantProfileEditForm, OrganizerProfileEditForm


# class ProfileChangeList(ChangeList):
#
#     def __init__(self, *args, **kwargs):
#         super(ProfileChangeList, self).__init__(*args, **kwargs)
#
#         # these need to be defined here, and not in MovieAdmin
#         self.list_display = ['user', 'date_of_birth', 'photo', 'categories']
#         self.raw_id_fields = ['user']
#         self.list_editable = ['categories']


class MembershipInline(admin.TabularInline):
    model = ParticipantProfile.categories.through


@admin.register(ParticipantProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
    inlines = [MembershipInline]

    def show_categories(self, obj):
        return "\n".join([a.title for a in obj.categories.all()])

    # def get_changelist(self, request, **kwargs):
    #     return ProfileChangeList

    # def get_changelist_form(self, request, **kwargs):
    #     return ProfileChangeList


@admin.register(OrganizerProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'organization']
    raw_id_fields = ['user']

    # def get_changelist(self, request, **kwargs):
    #     return ProfileChangeList

    # def get_changelist_form(self, request, **kwargs):
    #     return ProfileChangeList