from django.contrib import admin
from .models import Ticket

# Register your models here.
admin.site.register(Ticket)

class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
