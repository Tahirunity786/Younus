from django.db import models


class Package(models.Model):
    LEVEL_CHOICES = [
        ('level_one', 'Level One'),
        ('level_two', 'Level Two'),
        ('level_three', 'Level Three'),
    ]
    PACKAGE_TYPE = [
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
        ('extra', 'Extra'),
    ]

    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)
    level = models.CharField(
        max_length=20, choices=LEVEL_CHOICES, db_index=True, default="")
    types = models.CharField(
        max_length=20, choices=PACKAGE_TYPE, db_index=True, default="")


class Levels(models.Model):
    engine_min = models.IntegerField(default=0)
    engine_max = models.IntegerField(default=0)
    packages = models.ManyToManyField(Package)

    @staticmethod
    def get_level(engine):
        try:
            return Levels.objects.get(engine_min__lte=engine, engine_max__gte=engine)
        except Levels.DoesNotExist:
            return None
