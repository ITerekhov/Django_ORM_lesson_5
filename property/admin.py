from django.contrib import admin

from .models import Flat, Complaint


class FlatAmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ['created_at']
    list_display = ('town', 'address', 'price', 'new_building', 'construction_year',)
    list_editable = ('new_building',)
    list_filter = ('new_building',)

class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('user_name', 'flat',)
    list_display = ('user_name', 'flat', 'text',)
    raw_id_fields = ('flat', 'user_name',)

    
admin.site.register(Flat, FlatAmin)
admin.site.register(Complaint, ComplaintAdmin)