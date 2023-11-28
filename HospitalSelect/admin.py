from django.contrib import admin
from .models import County, Constituency, Specialization, Hospital

# Register your models here.
# admin.py
admin.site.register(County)
admin.site.register(Constituency)
admin.site.register(Specialization)
admin.site.register(Hospital)
