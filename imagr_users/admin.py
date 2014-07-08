from django.contrib import admin
from imagr_users.models import ImagrUser


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(ImagrUser, UserAdmin)