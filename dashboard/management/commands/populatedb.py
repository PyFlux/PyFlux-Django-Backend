# create fake data
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from dashboard.serializers import create_aclpermissions_for_role

fake = Faker()

from systemconfig.models import Country, Nationality, State, CityTown, Religion, Languages, Relationship, Occupation, \
    Hobby, District, Caste
from dashboard.models import Widget, Roles, UserTypes, SystemSettings


DATA = {
    'user_types': {'Super Admin': 'SU', 'Admin': 'A','Anonymous': 'AN'},
    'system_settings': {
        'maintenance_mode': '0', 'frontend_url': '', 'backend_url': '', 'sendsms_verifiednumbers_only':'0',
        'sub_domain': '',
    },
    'roles': ['Administrator', 'Manager', 'Anonymous'],
    'religions': ['Christian', 'Hindu', 'Muslim', 'Other'],
    'languages': ['English', 'Malayalam', 'Tamil', 'Hindi', 'Other'],
    'relationships': ['Father', 'Mother', 'Brother', 'Sister', 'Uncle', 'Other'],
    'occupations': ['Business', 'Teacher', 'Software Engineer', 'Driver', 'Other'],
    'student_categories': ['ST', 'SC', 'OBC''Nair', 'Bhramin', 'Roman Catholic', 'Latin Catholic', 'Others', ],
    'castes': ['Roman Catholic', 'Latin Catholic', 'Others', ],
    'nationalities': ['Indian', 'American', 'Sri Lankan', 'Other'],
    'states': ['Kerala', 'Tamilnadu', 'Karnataka', 'Other'],
    'districts': ['Thrissur', 'Ernakulam'],
    'cities': ['Thrissur', 'Guruvayur', 'Kunnamkulam', 'Other'],
    'hobbies': ['Reading', 'Writing', 'Drawing', 'Listening Music'],
    'countries': ['India', 'America', 'Other'],
    'designations': ['Principal', 'Manager', 'Teacher', 'Driver', 'Other'],
    'widgets': {'profile':''},
}


class Command(BaseCommand):
    help = 'Populate data'

    def handle(self, *args, **options):

        # Roles should be created from the system in the below order.
        # 'Roles - Primary Key value - These are static in a system
        # 'Principal - 3', 'Vice Principal - 4', 'Administrator - 5', 'Manager - 6', 'Employee - 7' , 'Teacher - 8', 'Student - 9', 'Parent - 10'
        # 'Librarian - 11', 'Anonymous - 12'
        # ++++++++++++++++++++++++ Adding Roles ++++++++++++++++++++++++
        for role in DATA['roles']:
            role_type = DATA['user_types'].get(role,'')
            data_exist = Roles.objects.filter(name__exact=role)
            if data_exist:
                if data_exist[0].name == role:
                    if data_exist[0].role_type == role_type:
                        print("Skipping: " + role)
                    else:
                        print("Updated: " + role)
                        data_exist.update(role_type=role_type)
                    continue

            # role_type = DATA['user_types'].get(role,'')
            
            role_created = Roles.objects.create(name=role, role_type=role_type, status=1)
            print("Added: " + role)
            create_aclpermissions_for_role(role_created)
            
        # ++++++++++++++++++++++++ End of Adding Roles +++++++++++++++++

        # ++++++++++++++++++++++++ Adding User Types ++++++++++++++++++++++++
        for key, val in DATA['user_types'].items():
            data_exist = UserTypes.objects.filter(user_type__exact=val).all()
            if not data_exist:
                print("Added: " + key)
                UserTypes.objects.create(name=key, user_type=val, status=1)
            else:
                if data_exist[0].user_type == val:
                    print("Skipping: " + val)
                else:
                    print("Added: " + key)
                    UserTypes.objects.create(name=key, user_type=val, status=1)
        # ++++++++++++++++++++++++ End of Adding User Types +++++++++++++++++

        #  ++++++++++++++++++++++++ Adding System Settings ++++++++++++++++++++++++
        for key, val in DATA['system_settings'].items():
            data_exist = SystemSettings.objects.filter(key__exact=key).all()
            if not data_exist:
                print("Added: " + key)
                SystemSettings.objects.create(key=key, value=val, status=1)
            else:
                if data_exist[0].key == key:
                    print("Skipping: " + key)
                else:
                    print("Added: " + key)
                    SystemSettings.objects.create(key=key, value=val, status=1)
        # ++++++++++++++++++++++++ End of Adding System Settings +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Religions ++++++++++++++++++++++++
        # religion = Religion.objects.create(religion_name=DATA['religions'][i], status=1)
        for religion in DATA['religions']:
            data_exist = Religion.objects.filter(religion_name__exact=religion).all()
            if not data_exist:
                print("Added: " + religion)
                Religion.objects.create(religion_name=religion, status=1)
            else:
                if data_exist[0].religion_name == religion:
                    print("Skipping: " + religion)
                else:
                    print("Added: " + religion)
                    Religion.objects.create(religion_name=religion, status=1)
        # ++++++++++++++++++++++++ End of Adding Religions +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Castes ++++++++++++++++++++++++
        for caste in DATA['castes']:
            data_exist = Caste.objects.filter(name__exact=caste).all()
            if not data_exist:
                print("Added: " + caste)
                Caste.objects.create(name=caste, status=1)
            else:
                if data_exist[0].name == caste:
                    print("Skipping: " + caste)
                else:
                    print("Added: " + caste)
                    Caste.objects.create(name=caste, status=1)
        # ++++++++++++++++++++++++ End of Adding Castes +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Languages ++++++++++++++++++++++++
        # language = Languages.objects.create(language_name=DATA['languages'][i], status=1)
        for language in DATA['languages']:
            data_exist = Languages.objects.filter(language_name__exact=language).all()
            if not data_exist:
                print("Added: " + language)
                Languages.objects.create(language_name=language, status=1)
            else:
                if data_exist[0].language_name == language:
                    print("Skipping: " + language)
                else:
                    print("Added: " + language)
                    Languages.objects.create(language_name=language, status=1)
        # ++++++++++++++++++++++++ End of Adding Religions +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Hobbies ++++++++++++++++++++++++
        for hobby in DATA['hobbies']:
            data_exist = Hobby.objects.filter(name__exact=hobby).all()
            if not data_exist:
                print("Added: " + hobby)
                Hobby.objects.create(name=hobby, status=1)
            else:
                if data_exist[0].name == hobby:
                    print("Skipping: " + hobby)
                else:
                    print("Added: " + hobby)
                    Hobby.objects.create(name=hobby, status=1)
        # ++++++++++++++++++++++++ End of Adding Hobbies +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Countries ++++++++++++++++++++++++
        # country = Country.objects.create(country_name='India', status=1)
        for country in DATA['countries']:
            data_exist = Country.objects.filter(country_name__exact=country).all()
            if not data_exist:
                print("Added: " + country)
                Country.objects.create(country_name=country, status=1)
            else:
                if data_exist[0].country_name == country:
                    print("Skipping: " + country)
                else:
                    print("Added: " + country)
                    Country.objects.create(country_name=country, status=1)
        # ++++++++++++++++++++++++ End of Adding Countries +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Relationships ++++++++++++++++++++++++
        # relationship = Relationship.objects.create(name=DATA['relationships'][i], status=1)
        for relationship in DATA['relationships']:
            data_exist = Relationship.objects.filter(name__exact=relationship).all()
            if not data_exist:
                print("Added: " + relationship)
                Relationship.objects.create(name=relationship, status=1)
            else:
                if data_exist[0].name == relationship:
                    print("Skipping: " + relationship)
                else:
                    print("Added: " + relationship)
                    Relationship.objects.create(name=relationship, status=1)
        # ++++++++++++++++++++++++ End of Adding Countries +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Occupation ++++++++++++++++++++++++
        # occupation = Occupation.objects.create(name=DATA['occupations'][i], status=1)
        for occupation in DATA['occupations']:
            data_exist = Occupation.objects.filter(name__exact=occupation).all()
            if not data_exist:
                print("Added: " + occupation)
                Occupation.objects.create(name=occupation, status=1)
            else:
                if data_exist[0].name == occupation:
                    print("Skipping: " + occupation)
                else:
                    print("Added: " + occupation)
                    Occupation.objects.create(name=occupation, status=1)
        # ++++++++++++++++++++++++ End of Adding Occupation +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Nationality ++++++++++++++++++++++++
        # nationality = Nationality.objects.create(nationality_name=DATA['nationalities'][i])
        for nationality in DATA['nationalities']:
            data_exist = Nationality.objects.filter(nationality_name__exact=nationality).all()
            if not data_exist:
                print("Added: " + nationality)
                Nationality.objects.create(nationality_name=nationality, status=1)
            else:
                if data_exist[0].nationality_name == nationality:
                    print("Skipping: " + nationality)
                else:
                    print("Added: " + nationality)
                    Nationality.objects.create(nationality_name=nationality, status=1)
        # ++++++++++++++++++++++++ End of Adding Nationality +++++++++++++++++

        # ++++++++++++++++++++++++ Adding States ++++++++++++++++++++++++
        # state = State.objects.create(state_name=DATA['states'][i], state_country=country, status=1)
        for state in DATA['states']:
            data_exist = State.objects.filter(state_name__exact=state).all()
            if not data_exist:
                print("Added: " + state)
                State.objects.create(state_name=state, status=1)
            else:
                if data_exist[0].state_name == state:
                    print("Skipping: " + state)
                else:
                    print("Added: " + state)
                    State.objects.create(state_name=state, status=1)
        # ++++++++++++++++++++++++ End of Adding States +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Widgets ++++++++++++++++++++++++
        # Widget.objects.create(name=item.capitalize(), code=item)
        for widget, roletypes in DATA['widgets'].items():
            # for widget in DATA['widgets']:

            data_exist = Widget.objects.filter(code__exact=widget)
            name = widget.replace('_',' ').title()
            if data_exist:
                if data_exist[0].code == widget:
                    print("Skipping: " + name)
                    continue

            Widget.objects.create(name=name, code=widget, roletypes = roletypes, status=1)
            print("Added: " + name)
                    
        # ++++++++++++++++++++++++ End of Adding Widgets +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Districts ++++++++++++++++++++++++
        for district in DATA['districts']:
            data_exist = District.objects.filter(name__exact=district).all()
            if not data_exist:
                print("Added: " + district)
                District.objects.create(name=district, status=1)
            else:
                if data_exist[0].name == district:
                    print("Skipping: " + district)
                else:
                    print("Added: " + district)
                    District.objects.create(name=district, status=1)
        # ++++++++++++++++++++++++ End of Adding District +++++++++++++++++

        # ++++++++++++++++++++++++ Adding City ++++++++++++++++++++++++
        # citytown = CityTown.objects.create(city_name=DATA['cities'][i], city_state=state, city_country=country,status=1)
        for city in DATA['cities']:
            data_exist = CityTown.objects.filter(city_name__exact=city).all()
            if not data_exist:
                print("Added: " + city)
                CityTown.objects.create(city_name=city, status=1)
            else:
                if data_exist[0].city_name == city:
                    print("Skipping: " + city)
                else:
                    print("Added: " + city)
                    CityTown.objects.create(city_name=city, status=1)
        # ++++++++++++++++++++++++ End of Adding City +++++++++++++++++
