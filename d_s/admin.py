from django.contrib import admin
from . models import User,Events,Notice,Visitor,Watchman,Chairman,Transaction

# Register your models here.

admin.site.register(User)
admin.site.register(Events)
admin.site.register(Notice)
admin.site.register(Visitor)
admin.site.register(Watchman)
admin.site.register(Chairman)
admin.site.register(Transaction)
