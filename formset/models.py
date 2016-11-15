from django.db import models


class Setup(models.Model):
    description = models.CharField(max_length=100)


class Specification(models.Model):
    setup = models.ForeignKey(Setup, related_name="target_specs")
    result = models.FloatField(default=0.)

