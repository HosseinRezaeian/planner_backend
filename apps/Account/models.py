from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, Permission, Group



class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name="account_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="account_user_permissions",
        blank=True
    )
    first_name = models.CharField(max_length=120,null=True)
    last_name = models.CharField(max_length=120,null=True)
    phone_number = models.CharField(max_length=11,null=True)

