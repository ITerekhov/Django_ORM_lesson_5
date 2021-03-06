from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerFlatsInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('flat', 'owner',)


@admin.register(Flat)
class FlatAmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = (
        'town',
        'address',
        'price',
        'new_building',
        'construction_year',
        )
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerFlatsInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('user', 'flat',)
    list_display = ('user', 'flat', 'text',)
    raw_id_fields = ('flat', 'user',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'owners_phonenumber', 'owner_pure_phone',)
    list_display = ('full_name', 'owners_phonenumber', 'owner_pure_phone',)
    raw_id_fields = ('flats',)
