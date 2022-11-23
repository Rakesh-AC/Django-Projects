from django.db import models
from django.contrib.auth.models import  AbstractUser

from . manager import UserManager
# Create your models here.


class User(AbstractUser):
    # we dont want to use username for log in so make it none
    username = None

    email = models.EmailField(unique=True)

    #Set all fields required
    mobile = models.CharField(max_length=14)
    is_varified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)

    #set user manage object
    bojects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


