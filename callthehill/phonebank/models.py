from django.db import models


class Call(models.Model):
    call_outcomes = (('C', "Contacted"),
                     ('V', "Left Voicemail"),
                     ('U', "Unsuccessful"))

    activist = models.ForeignKey("activist.Activist")
    issue = models.ForeignKey("issues.Issue")
    legislator = models.ForeignKey("legislation.Legislator")
    outcome = models.CharField(max_length=1, choices=call_outcomes)
