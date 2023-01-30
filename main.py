from typing import Tuple, List, Any

import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'worksplaces.settings'
django.setup()

from work_places.models import *


def get_person_name_by_id(person_id: int) -> str:
    try:
        person = Person.objects.get(id=person_id)
        return person.first_name + ' ' + person.last_name
    except Person.DoesNotExist:
        return "Person with id {} not found".format(person_id)


# print(get_person_name_by_id(1))


def get_people_by_age(age: int) -> list[Person]:
    """
    Given age in years, return list of persons of this age
    :param age:
    :return:
    """
    person = Person.objects.filter(birth_date__year=datetime.now().year - age)
    return person

# print(get_people_by_age(39))

def get_people_cnt_by_gender(gender: str) -> list[Person]:
    """
    Given the gender, return list of people of this gender
    :param gender:
    :return:
    """
    person = Person.objects.filter(gender=gender)
    return person

# print(get_people_cnt_by_gender("Male"))
# print(get_people_cnt_by_gender("Female"))


def get_companies_by_country(country: str) -> tuple[str, list[Any]]:
    """
    Given country name, return list of companies' names in this country
    :param country:
    :return:
    """
    company = Company.objects.filter(country=country)
    return f"{'companys in ' + country + ' are'}", [c.company_name for c in company]

# print(get_companies_by_country("China"))


def get_company_employees(company_id: int, current_only: str) -> tuple[str, list[Any]]:
    """
    Given company id, return list of persons whi work(ed) for this company
    :param company_id:
    :param current_only: if True, return only people who are currently work in the company
    :return:
    """
    company = Company.objects.get(id=company_id)
    employees = Employee.objects.filter(company=company_id, is_current_job=current_only)
    return f"{'employees in ' + str(company) + ' are'}", [get_person_name_by_id(e.id) for e in employees]


# print(get_company_employees(2, "true"))
# print(get_company_employees(1, True))
def get_person_jobs(person_id: int) -> str:
    """
    Given person_id, return list of dictionaries that map from company name to job title
    :param person_id:
    :return:
    """
    jobs = Employee.objects.filter(person_id=person_id)

    return f"{get_person_name_by_id(person_id)} 'has worked at:' {[{j.company.company_name:j.job_title} for j in jobs]}"
#print(get_person_jobs(5))




# with open("companies.csv", 'r', encoding= "utf-8") as file:
#     reader = csv.DictReader(file, delimiter=',')
#     header = next(reader)
#     for row in reader:
#         Company.objects.create(company_name=row["company_name"],
#                                country=row["country"],
#                                city=row["city"],
#                                address=row["address"],
#                                phone_num=row["phone_num"]).save()

# with open("persons.csv", 'r', encoding= "utf-8") as file:
#     reader = csv.DictReader(file, delimiter=',')
#     header = next(reader)
#     for row in reader:
#         Person.objects.create(first_name=row["first_name"],
#                                last_name=row["last_name"],
#                                personal_email=row["personal_email"],
#                                gender=row["gender"],
#                                birth_date=row["birth_date"]).save()
#
# with open("employees.csv", 'r', encoding= "utf-8") as file:
#     reader = csv.DictReader(file, delimiter=',')
#     header = next(reader)
#     for row in reader:
#         Employee.objects.create(person_id=row["person_id"],
#                                company_id=row["company_id"],
#                                job_title=row["job_title"],
#                                is_current_job=row["is_current_job"],
#                                company_email=row["company_email"]).save()
