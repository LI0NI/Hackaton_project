from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string


from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string


class MyUserManager(BaseUserManager):
    def _create(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('User must have username')
        if not email:
            raise ValueError('User must have email')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        return self._create(username, email, password, **extra_fields)

    def create_superuser(self,username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create(username, email, password, **extra_fields)


class MyUser(AbstractBaseUser):
    username = models.CharField('Username', max_length=50, primary_key=True)
    email= models.EmailField('Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username

    def has_module_perms(self, app_lable):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def create_activation_code(self):
        code = get_random_string(length=8)
        if MyUser.objects.filter(activation_code=code).exists():
            self.create_activation_code()
        self.activation_code = code
        self.save()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'





# class MyUserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, username, email, password, **extra_fields):
#         user = self.model(username=username, email=self. normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.create_activation_code()
#         user.save(using=self._db)
#         return user
    
#     def create_user(self,username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_active', False)
#         return self._create_user(username, email, password, **extra_fields)

#     def create_superuser(self,username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Super must is_staff=True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Super must is_staff=True')
#         return self._create_user(username, email, password, **extra_fields)


# class MyUser(AbstractUser):
#     username = models.CharField(max_length=50, primary_key=True)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=50, blank=True)

#     objects = MyUserManager()
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self) -> str:
#         return self.username

#     def has_module_perms(self, app_lable):
#         return self.is_staff

#     def has_perm(self, obj=None):
#         return self.is_staff

#     def create_activation_code(self):
#         code = get_random_string(length=8)
#         if MyUser.objects.filter(activation_code=code).exists():
#             self.create_activation_code()
#         self.activation_code = code
#         self.save()
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'User'

