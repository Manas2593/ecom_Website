from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator


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




class userProfile(models.Model):
    user = models.OneToOneField(regUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True)
    country_name = CountryField()
    phone_number = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(99999999999)])
    residence_number = models.CharField(max_length=150, null=True, blank=True)
    residence_lane = models.CharField(max_length=255, null=True, blank=True)
    residence_city = models.CharField(max_length=255, null=True, blank=True)
    residence_State = models.CharField(max_length=30, null=True, blank=True)
    residence_locality = models.CharField(max_length=80, null=True, blank=True)




    def __str__(self) -> None:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return str(self.user)
