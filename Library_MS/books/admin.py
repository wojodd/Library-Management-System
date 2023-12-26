from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Author)

admin.site.register(Publisher)

admin.site.register(Book)

admin.site.register(Ebook)

admin.site.register(Faculty)

admin.site.register(Category)

admin.site.register(New)

admin.site.register(Library)

admin.site.register(Section)

admin.site.register(Copy)

admin.site.register(Langauge)