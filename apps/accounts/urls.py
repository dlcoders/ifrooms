from django.urls import path

from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
    path("user-create/", views.CreateUserView.as_view(), name="user-create"),
    path("users/", views.ListUserView.as_view(), name="user-list"),
    path("users-update/<int:id>/", views.UpdateUserView.as_view(), name="user-update"),
    path("users-delete/<int:id>/", views.DeleteUserView.as_view(), name="user-delete"),
]
