from django.db import models


class Countries(models.Model):
    country_id = models.TextField(primary_key=True)
    country_name = models.TextField()
    region = models.ForeignKey('Regions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.TextField()
    location = models.ForeignKey('Locations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departments'


class Dependents(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    relationship = models.TextField()
    employee = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dependents'


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField()
    email = models.TextField()
    phone_number = models.TextField(blank=True, null=True)
    hire_date = models.TextField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.TextField()  # This field type is a guess.
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employees'


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.TextField()
    min_salary = models.TextField()  # This field type is a guess.
    max_salary = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jobs'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    city = models.TextField()
    state_province = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locations'


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'regions'
