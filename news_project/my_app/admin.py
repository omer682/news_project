from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session
from .forms import SignUpForm
from .models import CustomUser, Post
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = SignUpForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
        'User role',
        {
            'fields':(
            'personal_id',
            'age',
            'city',
            'user_type'
            )
        }
        )
    )
   


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Session)
admin.site.register(Post)
