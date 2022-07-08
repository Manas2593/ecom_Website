from django.db import models


# Custom User Model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


# user model manager
class regUserManager(BaseUserManager):
    def create_user(self, email, password=None,is_active=True, is_staff=False, is_superuser=False):
        if not email:
            return ValueError('Users must have an email address for making an Tailwind Account')
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.active = is_active
        user.superuser = is_superuser
        user.staff = is_staff
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email = email,
            password=password,
            is_staff = True
        )
        return user


    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = email,
            password=password,
            is_staff = True,
            is_superuser=True
        )
        return user


    








# USer model
class regUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser

    objects=regUserManager()


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    