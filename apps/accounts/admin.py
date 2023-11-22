from django.contrib import admin
from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "registration",
        "is_superuser",
        "is_staff",
        "is_coordinator",
        "is_teacher",
        "is_active",
        "date_joined",
        "last_updated",
    ]

    list_filter = [
        "registration",
        "is_superuser",
        "is_staff",
        "is_coordinator",
        "is_teacher",
        "is_active",
    ]

    search_fields = ["registration"]

    fieldsets = (
        ("Usuário", {"fields": ("registration", "password")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_coordinator",
                    "is_teacher",
                    "is_active",
                )
            },
        ),
        ("Histórico de Acesso", {"fields": ("date_joined", "last_updated")}),
    )

    ordering = ["registration"]

    def has_add_permission(self, request):
        # Disable the ability to add new users through the Django Admin
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ["date_joined", "last_updated"]
        else:  # adding a new object
            return []
