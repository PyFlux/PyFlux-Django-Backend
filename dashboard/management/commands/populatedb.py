# create fake data
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from dashboard.serializers import create_aclpermissions_for_role

fake = Faker()

from systemconfig.models import Country, Nationality, State, CityTown, Religion, Languages, Relationship, Occupation, \
    Hobby, District, Caste
from students.models import StudentCategory, Student
from academics.models import AcademicYear, Courses, Batches, Section, Classes, Subject, Exam
from exammanagement.models import QuestionCategory, Questions, QuestionOptions
from dashboard.models import Widget, Roles, UserTypes, SystemSettings
from hr.models import Designation

DATA = {
    'user_types': {'Super Admin': 'SU', 'Admin': 'A', 'Principal': 'PR', 'Manager': 'MN', 'Student': 'S', 'Parent': 'P',
                   'Employee': 'E', 'Teacher': 'T', 'Anonymous': 'AN'},
    'system_settings': {
        'maintenance_mode': '0', 'frontend_url': '', 'backend_url': '', 'sendsms_verifiednumbers_only':'0',
        'sub_domain': '',
    },
    'roles': ['Principal', 'Vice Principal', 'Administrator', 'Manager', 'Employee', 'Teacher', 'Student', 'Parent',
              'Librarian', 'Anonymous'],
    'religions': ['Christian', 'Hindu', 'Muslim', 'Other'],
    'languages': ['English', 'Malayalam', 'Tamil', 'Hindi', 'Other'],
    'relationships': ['Father', 'Mother', 'Brother', 'Sister', 'Uncle', 'Other'],
    'occupations': ['Business', 'Teacher', 'Software Engineer', 'Driver', 'Other'],
    'academic_years': ['2017-2018', '2018-2019', '2019-2020'],
    'student_categories': ['ST', 'SC', 'OBC''Nair', 'Bhramin', 'Roman Catholic', 'Latin Catholic', 'Others', ],
    'castes': ['ST', 'SC', 'OBC''Nair', 'Bhramin', 'Roman Catholic', 'Latin Catholic', 'Others', ],
    'nationalities': ['Indian', 'American', 'Sri Lankan', 'Other'],
    'states': ['Kerala', 'Tamilnadu', 'Karnataka', 'Other'],
    'districts': ['Thrissur', 'Ernakulam'],
    'cities': ['Thrissur', 'Guruvayur', 'Kunnamkulam', 'Other'],
    'hobbies': ['Reading', 'Writing', 'Drawing', 'Listening Music'],
    'countries': ['India', 'America', 'Other'],
    'designations': ['Principal', 'Manager', 'Teacher', 'Driver', 'Other'],
    'widgets': {'profile':'', 'fees':'S,P,T', 'events':'', 'noticeboard':'', 'holidays':'', 
                'student_progress_report':'S,P', 'student_fee_report':'S,P,T', 'teacher_exam_report':'T', 
                'student_attendance_report':'S,P,T', 'common_attendance_report':'','assignment':'S,P,T', 
                'leave_applications':'', 'timetable':'', 'teacher_timetable':'T'},

    'subjects': ['Malayalam Paper 1', 'Malayalam Paper 2', 'English', 'Hindi', 'Physics', 'Mathematics', 'Chemistry',
                 'Biology', 'Science', 'Social Sciences', 'Information Technology (IT)', 'Sanskrti'],
    # 'courses': ['Electronics', 'ComputerScience', 'Mechanical'],
    # 'batches': ['2017', '2018', '2019'],
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

        # ++++++++++++++++++++++++ Adding Student Category ++++++++++++++++++++++++
        # student_category = StudentCategory.objects.create(student_category_name=DATA['student_categories'][i], status=1)       
        for student_category in DATA['student_categories']:
            data_exist = StudentCategory.objects.filter(student_category_name__exact=student_category).all()
            if not data_exist:
                print("Added: " + student_category)
                StudentCategory.objects.create(student_category_name=student_category, status=1)
            else:
                if data_exist[0].student_category_name == student_category:
                    print("Skipping: " + student_category)
                else:
                    print("Added: " + student_category)
                    StudentCategory.objects.create(student_category_name=student_category, status=1)
        # ++++++++++++++++++++++++ End of Adding Student Category +++++++++++++++++

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

        # ++++++++++++++++++++++++ Adding Subjects ++++++++++++++++++++++++
        # citytown = CityTown.objects.create(city_name=DATA['cities'][i], city_state=state, city_country=country,status=1)
        for subject in DATA['subjects']:
            data_exist = Subject.objects.filter(subject_name__exact=subject).all()
            if not data_exist:
                print("Added: " + subject)
                Subject.objects.create(subject_name=subject, status=1)
            else:
                if data_exist[0].subject_name == subject:
                    print("Skipping: " + subject)
                else:
                    print("Added: " + subject)
                    Subject.objects.create(subject_name=subject, status=1)
        # ++++++++++++++++++++++++ End of Adding Subjects +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Academic Year ++++++++++++++++++++++++
        #     academic_year = AcademicYear.objects.create(academic_name=DATA['academic_years'][i], status=1,start_date=fake.date_this_month(), end_date=fake.date_this_month())
        for academic_year in DATA['academic_years']:
            data_exist = AcademicYear.objects.filter(academic_name__exact=academic_year).all()
            if not data_exist:
                print("Added: " + academic_year)
                AcademicYear.objects.create(academic_name=academic_year, status=1)
            else:
                if data_exist[0].academic_name == academic_year:
                    print("Skipping: " + academic_year)
                else:
                    print("Added: " + academic_year)
                    AcademicYear.objects.create(academic_name=academic_year, status=1)
        # ++++++++++++++++++++++++ End of Adding Academic Year +++++++++++++++++

        # ++++++++++++++++++++++++ Adding Employee Designations ++++++++++++++++++++++++
        for designation in DATA['designations']:
            data_exist = Designation.objects.filter(emp_designation_name__exact=designation).all()
            if not data_exist:
                print("Added: " + designation)
                Designation.objects.create(emp_designation_name=designation, status=1)
            else:
                if data_exist[0].emp_designation_name == designation:
                    print("Skipping: " + designation)
                else:
                    print("Added: " + designation)
                    Designation.objects.create(emp_designation_name=designation, status=1)
        # ++++++++++++++++++++++++ End of Adding Employee Designations +++++++++++++++++

        # Employee Category
        # unskilled, clerical, trades, or professional

        # Employee Designation
        # teacher, etc

        # for i in range(3):
        #
        #     academic_year = AcademicYear.objects.create(academic_name=DATA['academic_years'][i], status=1,
        #                                                 start_date=fake.date_this_month(),
        #                                                 end_date=fake.date_this_month())
        #     course = Courses.objects.create(course_name=DATA['courses'][i], status=1,
        #                                     course_code=DATA['courses'][i], course_alias=DATA['courses'][i])
        #     batch = Batches.objects.create(batch_name=DATA['batches'][i] + 'Batch', academic_name=academic_year,
        #                                    status=1,
        #                                    course_name=course, start_date=fake.date_this_month(),
        #                                    end_date=fake.date_this_month())

        #     for j in ['A', 'B', 'C']:
        #         Classes.objects.create(class_name='%d' % (i + 5), class_division=j)
        #
        # cat = QuestionCategory.objects.create(name='Energy Sources',
        #                                       description='Advantages and Disadvantages of energy sources', status=1)
        # questions = [
        #     'An advantage of using solar power is',
        #     'An advantage of using hydroelectric power is',
        #     'Most utility companies in the U.S. dont use hydroelectric power because',
        #     'Which energy source would be best for a city that has limited space and want to be effecient?',
        #     'What is a major disadvantage of nuclear power?',
        #     'If a community were choosing between solar and wind, what advantage would make wind the best choice?',
        #     'An advantage of burning coal for energy is',
        #     'An advantage of using natural gas as a form of energy is',
        #     'What do geothermal and solar energy have in common?',
        # ]
        # opts = [
        #     ['no greenhouse gases', 'lots of pollution', 'it is available even on cloudy days'],
        #     ['reservoirs can be used for irrigation of crops', 'sometimes surrounding area get flooded',
        #      'the normal flow of the water is diverted'],
        #     ['the plants are expensive to build and use expensive machinery',
        #      'reservoirs can be used to irrigate crops and they dont want to help farmers',
        #      'the cause a lot of greenhouse gass'],
        #     [r'solar-costly to build and 6%-30% efficient', r'Wind-turbines need lots of free space 40%-60% efficient',
        #      'Natural gas-can be used in small areas 50%-60% efficient'],
        #     ['it produces small amounts of power', 'the by-product(waste) is nuclear radiation',
        #      'power plants are inexpensive to build'],
        #     ['locations for turbines are limited because the wind can be blocked',
        #      'solar needs a back up system for cloudy days, some days there is no wind to move the turbines blades',
        #      'wind energy is less expensive and it is limitless'],
        #     ['it is an inexpensive source of energy', 'it does not pollute the air', 'it is a renewable energy source'],
        #     ['it is more expensive compared to other fossil fuels',
        #      'It produces low emissions(pollution) compared to other fossil fuels',
        #      'there is a more limited supply compared to other fossil fuels'],
        #     ['they both use sunlight to generate energy', 'both are non-renewable energy sources',
        #      'neither produce greenhouse gass'],
        # ]
        #
        # ans = [1, 1, 1, 3, 2, 3, 1, 2, 3]
        #
        # for i, q in enumerate(questions):
        #     quest = Questions.objects.create(questioncategory=cat, title=q, desc=q, status=1)
        #     t = 'text'
        #     QuestionOptions.objects.create(question=quest,
        #                                    opt_1=opts[i][0], opt_1_type=t, opt_2=opts[i][1], opt_2_type=t,
        #                                    opt_3=opts[i][2], opt_3_type=t,
        #                                    answer=ans[i], difficulty='Easy')
