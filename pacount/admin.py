from django.contrib import admin
from pacount.models import Field, Hole

# Register your models here.


class HoleAdmin(admin.options.TabularInline):
    model = Hole


class FieldAdmin(admin.ModelAdmin):
    inlines = [HoleAdmin, ]


admin.site.register(Field, FieldAdmin)