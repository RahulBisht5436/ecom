from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.product)
admin.site.register(models.order)
admin.site.site_header="rahul dashboard"