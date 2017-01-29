from django.core.validators import RegexValidator
from django.db import models

class Legislator(models.Model):
    """
    A specific legislator
    """
    gender_options = (('F', "Female"),
                      ('N', "Nonbinary"),
                      ('M', "Male"))
    invalid_phone = "Phone number must be in the format +999999999. Up to 15 digits allowed."

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=invalid_phone)

    family_name = models.CharField(max_length=30)
    given_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=gender_options)
    pronouns = models.ForeignKey("Pronouns")
    party = models.CharField(max_length=3)
    body = models.ForeignKey("Body")
    phone_number = models.CharField(max_length=16, validators=[phone_regex], blank=True)

class Honorific(models.Model):
    """
    An honorific set used by Legislators in a Body
    """
    neutral = models.CharField(max_length=30)
    masculine = models.CharField(max_length=30)
    feminine = models.CharField(max_length=30)

class Pronouns(models.Model):
    """
    The set of pronouns used by a Legislator
    """
    sub = models.CharField(max_length=30)
    obj = models.CharField(max_length=30)
    own = models.CharField(max_length=30)
    ref = models.CharField(max_length=30)

class Party(models.Model):
    """
    A political party
    """
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=3)

class Body(models.Model):
    """
    A legislative body
    """
    name = models.TextField()
    location = models.TextField()
    honorific = models.ForeignKey("Honorific")
    controlling_party = models.ForeignKey("Party")

class Vote(models.Model):
    """
    A single Legislator"s vote on a Legislation
    """
    vote_options = (('Y', "Yea"),
                    ('N', "Nay"),
                    ('A', "Abstain"))

    legislator = models.ForeignKey("Legislator")
    vote = models.CharField(max_length=1, choices=vote_options)

class Legislation(models.Model):
    """
    A piece of Legislation sponsored by Legislators in a Body
    """
    name = models.TextField(blank=False)
    reference = models.URLField()
    sponsors = models.ManyToManyField("Legislator")
    body = models.ForeignKey("Body")
    votes = models.ManyToManyField("Vote")

    positively_related_legislation = models.ManyToManyField("self")
    netatively_relation_legislation = models.ManyToManyField("self")

class ExternalInformation(models.Model):
    """
    Data retrieved from an external API
    """
    reference = models.URLField()
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
