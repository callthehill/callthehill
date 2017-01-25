from django.db import models

class Issue(models.Model):
    """
    An Issue about which you call a Legislator
    Tied to one, and only one, primary Legislation
    Legislations associated with the primary Legislation are used to determine calls
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    legislation = models.ForeignKey("legislation.Legislation")
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    """
    A Tag which can be added to an Issue
    """
    tag = models.CharField(max_length=10)
    description = models.CharField(max_length=140)
