from django.contrib import admin
from maths.models import Math
# Register your models here.
class MathAdmin(admin.ModelAdmin):
    list_display = ["operations", "a", "b"]
    search_fields = ["operations"]
    list_filter = ["operations"]
admin.site.register(Math, MathAdmin)