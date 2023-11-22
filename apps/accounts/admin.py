from django.contrib import admin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # model = models.Event
    list_display = [
        "email",
        "matricula",
    ]
    list_filter = ["email", "matricula"]
    search_fields = ["matricula"]
