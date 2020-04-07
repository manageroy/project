from django.contrib import admin

# Register your models here.
from . import models


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Stu_msg, UserProfileAdmin)
admin.site.register(models.Student, UserProfileAdmin)
admin.site.register(models.Administrator, UserProfileAdmin)
admin.site.register(models.Class, UserProfileAdmin)
admin.site.register(models.Change_class, UserProfileAdmin)
admin.site.register(models.School_expression, UserProfileAdmin)
admin.site.register(models.Points, UserProfileAdmin)
admin.site.register(models.Suggestions, UserProfileAdmin)
admin.site.register(models.Leave_school, UserProfileAdmin)
