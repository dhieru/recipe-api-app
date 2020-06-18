from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionMixin


class UserManager(BaseUserManager):

    def create_user(self,email,password=None, **extra_fields):
        
# Create your models here.
