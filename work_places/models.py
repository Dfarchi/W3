from datetime import *

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



# Create your models here.


class Person(models.Model):
    DoesNotExist = None
    first_name = models.CharField(db_column='first name', max_length=256, null=False)
    last_name = models.CharField(db_column='last name', max_length=256, null=False)
    personal_email = models.CharField(db_column='Email', max_length=256, null=False)
    gender = models.CharField(db_column='gender ',
                              choices=[('Male', 'M'), ('Female', 'F'), ('Polygender', 'P'), ('Genderfluid', 'G'), ('Agender', 'A'), ('Bigender', 'B')]
                              , max_length=256, null=False)
    birth_date = models.DateField(db_column='birth_date',
                                  validators=[MinValueValidator(datetime(year=1900, month=1, day=1)),
                                              MaxValueValidator(datetime.now)])
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'persons'


class Employee(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    job_title = models.CharField(db_column='job title', max_length=256, null=False)
    is_current_job = models.CharField(db_column="is_current_job",max_length=256, null=False)
    company_email = models.CharField(db_column='Email', max_length=256, null=False)


    class Meta:
        db_table = 'employees'


class Company(models.Model):
    company_name = models.CharField(db_column='company_name', max_length=256, null=False)
    country = models.CharField(db_column='country', max_length=256, null=False)
    city = models.CharField(db_column='city ', max_length=256, null=False)
    address = models.CharField(db_column='address', max_length=256, null=False)
    phone_num = models.CharField(db_column='phone_num', max_length=256, null=False)
    persons = models.ManyToManyField(Person, through='Employee')

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        db_table = "companys"
