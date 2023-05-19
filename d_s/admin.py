from django.contrib import admin
from . models import User,Events,Notice

# Register your models here.

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Notice)
