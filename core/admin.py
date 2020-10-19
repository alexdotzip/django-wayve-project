from django.contrib import admin

from .models import OrgId, Category, Journal

admin.site.register(OrgId)
admin.site.register(Category)
admin.site.register(Journal)
