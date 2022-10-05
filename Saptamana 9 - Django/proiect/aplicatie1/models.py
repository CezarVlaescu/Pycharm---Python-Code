from django.db import models


class Location(models.Model):

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.country} -> {self.city}"


class Pontaj(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user} {self.start_date}"

