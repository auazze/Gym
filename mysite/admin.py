from django.contrib import admin

from .models import Client, Registration
from .models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone')


admin.site.register(Client)
admin.site.register(Registration)
