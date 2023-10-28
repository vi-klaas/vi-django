from django.contrib import admin

from .models import UserProfile, Department


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = [
        "user",
        "position",
        "get_departments",
        "id",
    ]

    def get_departments(self, obj):
        return "\n".join([d.name for d in obj.departments.all()])


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = [
        "name",
        "short_name",
        "id",
    ]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
