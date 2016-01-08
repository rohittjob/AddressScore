from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=200)

    def __unicode__(self):
        return self.country



class State(models.Model):
    state = models.CharField(max_length=200)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.state


class City(models.Model):
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    zip_start = models.IntegerField()
    zip_end = models.IntegerField()

    def __unicode__(self):
        return self.city


class Pincode(models.Model):
    pincode = models.IntegerField(primary_key=True)
    score = models.FloatField(default=0.0)
    encountered_entries = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.pincode)