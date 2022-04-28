from atexit import register
from django.contrib import admin
from .models import Chat_Groups,profile_details,Chat
# Register your models here.
admin.site.register(Chat_Groups)
admin.site.register(profile_details)
admin.site.register(Chat)
