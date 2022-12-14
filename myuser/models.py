from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# otp = s.random(length=5)

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("You have to import username")

        user = self.model(
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self,  username, first_name="", last_name="", password=None):
        user = self.create_user(
            username = username,
            # first_name = first_name,
            # last_name = last_name,
        )

        user.level_1 = True
        user.level_2 = True
        user.level_3 = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):
    
    # username = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)



    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_level_2 = models.BooleanField(_("مدیر عامل"), default=False)
    is_level_1 = models.BooleanField(_("مدیر"), default=False)
    is_level_3 = models.BooleanField(_("کارمند"), default=False)
    




    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


    def __str__(self):
        return self.username