from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class user(AbstractUser):
    is_admin=models.BooleanField('is_admin', default=False)
    is_student=models.BooleanField('is_student', default=False)
    is_teacher=models.BooleanField('is_teacher', default=False)