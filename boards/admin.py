from django.contrib import admin
from .models import Board, Topic, Contact
from django.contrib.auth.models import Group


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'query', 'created_on')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('starter', 'subject', 'board', 'views')


admin.site.unregister(Group)
admin.site.register(Board)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Contact, ContactAdmin)
