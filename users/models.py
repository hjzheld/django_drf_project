from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, fullname, nickname, date_of_birth, password=None):
        if not username:
            raise ValueError('Users must have an email username')
        if not email:
            raise ValueError('Users must have an email address')
        if not fullname:
            raise ValueError('Users must have an email fullname')
        if not nickname:
            raise ValueError('Users must have an email nickname')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            fullname = fullname,
            nickname = nickname,
            date_of_birth = date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, fullname, nickname, date_of_birth, password=None):
        user = self.create_user(
            email,
            username,
            fullname,
            nickname,
            date_of_birth,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100, default=False)
    fullname = models.CharField(max_length=100, default=False)
    nickname = models.CharField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['username', 'email', 'fullname']


    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin