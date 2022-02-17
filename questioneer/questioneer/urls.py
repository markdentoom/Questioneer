from django.contrib import admin
from django.urls import include, path
from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomUserForm

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=CustomUserForm, success_url="/"),
        name="django_registration_register",
    ),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("api/v1/", include("questions.api.urls")),
]
