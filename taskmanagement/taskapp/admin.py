from django.contrib import admin
from .models import Team, Task
from django.contrib.auth.models import User

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin


'''class AccountInLine(admin.StackedInline):
    model = CustomUser
    can_delete = False

# Register your models here.
class CustomUserAdmin(UserAdmin):
    inlines = (AccountInLine, )'''






# Register your models here.
admin.site.register(Team)

#admin.site.register(User)
admin.site.register(Task)
