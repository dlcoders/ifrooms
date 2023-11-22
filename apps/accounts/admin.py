from django.contrib import admin
from apps.accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "registration",
        "name",
        "email",
        "is_coordinator",
        "is_teacher",
        "is_active",
    ]
    list_filter = [
        "is_superuser",
        "is_coordinator",
        "is_teacher",
        "is_active",
    ]

    search_fields = ["registration"]
    readonly_fields = ["date_joined", "last_updated"]

    fieldsets = (
        ("Usuário", {"fields": ("name", "email", "registration", "password")}),
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

    # Disable add new users through the Django Admin
    def has_add_permission(self, request):
        return False

