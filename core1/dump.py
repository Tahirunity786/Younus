from django.db import models

# Create your models here.

class Packages_1_extra_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)

class Packages_1_exterior_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)


class Packages_1_interior_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)

class Packages_2_extra_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)
class Packages_2_exterior_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)


class Packages_2_interior_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)

class Packages_3_extra_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)
class Packages_3_exterior_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)


class Packages_3_interior_Data(models.Model):
    package_name = models.CharField(max_length=100, default="", db_index=True)
    price = models.IntegerField(default=0, db_index=True)
    package_description = models.TextField(default="", db_index=True)


class Packages1(models.Model):
    extra_package = models.ManyToManyField(Packages_1_extra_Data, related_name="level_one_extra_package" )
    exterior_package = models.ManyToManyField(Packages_1_exterior_Data, related_name="level_one_exterior_package" )
    interior_package = models.ManyToManyField(Packages_1_interior_Data, related_name="level_one_interior_package" )
    


class Packages2(models.Model):
    extra_package = models.ManyToManyField(Packages_2_extra_Data, related_name="level_two_extra_package" )
    exterior_package = models.ManyToManyField(Packages_2_exterior_Data, related_name="level_two_exterior_package" )
    interior_package = models.ManyToManyField(Packages_2_interior_Data, related_name="level_two_interior_package" )


class Packages3(models.Model):
    extra_package = models.ManyToManyField(Packages_3_extra_Data, related_name="level_three_extra_package" )
    exterior_package = models.ManyToManyField(Packages_3_exterior_Data, related_name="level_three_exterior_package" )
    interior_package = models.ManyToManyField(Packages_3_interior_Data, related_name="level_three_interior_package" )

class Levels(models.Model):
    level_one = models.ManyToManyField(Packages1, related_name="level_one" )
    level_two = models.ManyToManyField(Packages2, related_name="level_two")
    level_three = models.ManyToManyField(Packages3, related_name="level_three")


class Payments(models.Model):
    # Info
    first_name = models.CharField(max_length=100, default='', db_index=True)
    last_name = models.CharField(max_length=100, default='', db_index=True)
    # contact
    postal_code = models.CharField(max_length=30, default='', db_index=True)
    # Address
    street_no = models.CharField(max_length=200, default='', db_index=True)
    postal_code = models.CharField(max_length=50, default='', db_index=True)
    city = models.CharField(max_length=100, default='', db_index=True)
    state = models.CharField(max_length=100, default='', db_index=True)
    country = models.CharField(max_length=100, default='', db_index=True)