from django.contrib import admin
from .models import *


class PostAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Post._meta.fields]



    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)


class UsersAdmin (admin.ModelAdmin):

    list_display = [field.name for field in Users._meta.fields]



    class Meta:
        model = Users

admin.site.register(Users, UsersAdmin)


