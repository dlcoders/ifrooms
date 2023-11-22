from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, registration, password=None, registration_type='student', **extra_fields):
        user = self.model(registration=registration, registration_type=registration_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, registration, password=None, registration_type='student', **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_coordinator", False)
        extra_fields.setdefault("is_teacher", False)
        return self._create_user(registration, password, registration_type, **extra_fields)

    def create_teacher(self, registration, password=None, registration_type='teacher', **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_coordinator", False)
        extra_fields.setdefault("is_teacher", True)
        return self._create_user(registration, password, registration_type, **extra_fields)

    def create_coordinator(self, registration, password=None, registration_type='coordinator', **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_coordinator", True)
        return self._create_user(registration, password, registration_type, **extra_fields)

    def create_superuser(self, registration, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_coordinator", False)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(registration, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    REGISTRATION_TYPE_CHOICES = [
        ('student', _('Aluno')),
        ('coordinator', _('Coordenador')),
        ('teacher', _('Professor')),
    ]

    registration = models.CharField(
        _("Matrícula"),
        max_length=12,
        unique=True,
        help_text="Ex: 123456",
    )

    name = models.CharField(_("Nome"), max_length=100)
    email = models.EmailField(_("E-mail"), unique=True)

    registration_type = models.CharField(
        _("Tipo"),
        max_length=20,
        choices=REGISTRATION_TYPE_CHOICES,
        default="student",
    )

    is_superuser = models.BooleanField(_("Superuser"), default=False)
    is_staff = models.BooleanField(_("Staff"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    is_coordinator = models.BooleanField(_("Coordinator"), default=False)
    is_teacher = models.BooleanField(_("Teacher"), default=False)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "registration"

    def __str__(self):
        return f"{self.name} ({self.registration})"
