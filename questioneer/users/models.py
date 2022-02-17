from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Use default AbstractUser, but inherit it so we can change it as we see fit later
    pass
