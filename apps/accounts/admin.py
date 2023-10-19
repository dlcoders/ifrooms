from django.contrib import admin
from .models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # model = models.Event
    list_display = [
        "email",
        "matricula",
    ]
    list_filter = ["email", "matricula"]
    search_fields = ["matricula"]
