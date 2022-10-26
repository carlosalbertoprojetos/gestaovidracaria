from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
#from import_export.admin import ImportExportMixin
#from import_export import resources

from .models import Fisico, Fiscal


class FisicoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fisico, FisicoAdmin)

class FiscalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fiscal, FiscalAdmin)
