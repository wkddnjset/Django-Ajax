from django.contrib import admin
from .models import Lone, Payback
# Register your models here.

class LoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'attention', 'price')

class PaybackAdmin(admin.ModelAdmin):
    list_display = ('id', 'lone_id', 'payback')

admin.site.register(Lone, LoneAdmin)
admin.site.register(Payback, PaybackAdmin)