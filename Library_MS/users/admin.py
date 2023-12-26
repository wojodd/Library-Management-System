from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(CustomUsers)

admin.site.register(gender)

admin.site.register(Despositves)

admin.site.register(Semester)

admin.site.register(Cities)
admin.site.register(Role)