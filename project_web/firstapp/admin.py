from django.contrib import admin

# Register your models here.
from firstapp.models import article,User,push,party
# Register your models here.

admin.site.register(article)
admin.site.register(User)
admin.site.register(push)
admin.site.register(party)