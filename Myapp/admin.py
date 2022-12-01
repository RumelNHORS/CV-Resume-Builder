from django.contrib import admin
from . models import ResumeProfile

#admin.site.register(ResumeProfile)


@admin.register(ResumeProfile)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address']