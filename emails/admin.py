from django.contrib import admin
from .models import *


class EmailSetingFactAdmin (admin.ModelAdmin):

    list_filter = ['email']
    search_fields = ['name', 'email']


    class Meta:
        model = EmailSetingFact

admin.site.register(EmailSetingFact, EmailSetingFactAdmin)