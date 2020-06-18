from django.contrib import admin
from balance.models import Weight, Equipment, Charge


class ChargeAdmin(admin.ModelAdmin):
    model = Charge
    list_display = ('identification', 'equipment', 'created_by')
    search_fields = ('identification', 'equipment__description', 'equipment_identification')


admin.site.register(Charge, ChargeAdmin)
admin.site.register(Equipment)
admin.site.register(Weight)
