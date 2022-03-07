from django.db import models

# Create your models here.
class Bitcoin(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Ethereum(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Tether(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Helium(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Doge(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Litecoin(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Polkadot(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class Cardano(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']

class ShibaInu(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.BigIntegerField()

    # FixMe: For later? Keeps the db in descending order
    # class Meta:
    #     ordering = ['-updated', '-created']