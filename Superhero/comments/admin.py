from django.contrib import admin

# Register your models here.
from .models import comBatman
from .models import comSuperman
from .models import comWonderWoman

admin.site.register(comBatman)
admin.site.register(comSuperman)
admin.site.register(comWonderWoman)