from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUsers
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'Father_name', 'gender_id', 'feculty_id', 'semester_id', 'contant_no', 'Registration_no',
                    'original_Address','current_Address', 'role_id',  'signature'
                )
            }
        )
    )


admin.site.register(CustomUsers, CustomUserAdmin)

admin.site.register(gender)

admin.site.register(Despositves)

admin.site.register(Semester)

admin.site.register(Cities)
admin.site.register(Role)