import uuid
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

class Activist(models.Model):
    """
    An Activist is a user on Call the Hill
    """
    invalid_zip = "The ZIP code you entered is invalid"

    zip_validator = RegexValidator(regex=r'^\d{5}(?:[-\s]\d{4})?$', message=invalid_zip)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    interests = models.ManyToManyField('issues.Tag', blank=True)
    name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, validators=[zip_validator])
    photo = models.ImageField(default="default_user.jpg")
