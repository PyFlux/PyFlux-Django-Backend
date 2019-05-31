SIDE_BAR_MENUS = [
{   
    "menu_text": "Control Panel",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{   
        "menu_text": "User Management",
        "sub_sub_menu": [
            {"link": "/dashboard/users", "menu_text": "Users"},
            {"link": "/dashboard/roles","menu_text": "Roles" }
        ]
    },
    {   
        "menu_text": "Assign User Roles",
        "sub_sub_menu": [
            {"link": "/dashboard/userroles", "menu_text": "User Roles"} 
        ]
    },
    { 
        "menu_text": "Menu Management",
        "sub_sub_menu": [
            {"link": "/dashboard/menumanagement", "menu_text": "Sync Menu"} 
        ]
    }]
},
{
    "menu_text": "Students",
    "menu_icon": "fa fa-users",
    "sub_menu": [{
        "menu_text": "Students Management",
        "sub_sub_menu": [   
            {"link": "/students/student", "menu_text": "Students List"},
            {"link": "/students/studentcategory", "menu_text": "Students Category"},
            {"link": "/students/importstudents", "menu_text": "Import/Export Students"},
            {"link": "/students/studentidcard", "menu_text": "Student ID Card Generation"},
            {"link": "/students/studentmigration", "menu_text": "Student Migration"},
        ]
    }]
},
{
    "menu_text": "Admissions",
    "menu_icon": "fa fa-file-text-o",
    "sub_menu": [{
        "menu_text": "Admission Management ",
        "sub_sub_menu": [
            {"link": "/admissions/admission", "menu_text": "Admissions"}
        ]
    }]
},     
{
    "menu_text": "Communications",
    "menu_icon": "fa fa-comments",
    "sub_menu": [{
        "menu_text": "Messages",
        "sub_sub_menu": [
            {"link": "/communications/chat", "menu_text": "Chat"},
            {"link": "/communications/messages", "menu_text": "My Messages"}, 
            {"link": "/communications/composemessage", "menu_text": "Compose Message"}, 
            {"link": "/communications/messagegroup", "menu_text": "Groups"},
            {"link": "/communications/announcements", "menu_text": "Announcements"},
        ]
    }]
},
{
    "menu_text": "Events",
    "menu_icon": "fa fa-calendar",
    "sub_menu": [{
        "menu_text": "Event Management ",
        "sub_sub_menu": [
            {"link": "/events/eventtype", "menu_text": "Event Category"},
            {"link": "/events/event", "menu_text": "Events List"},
            {"link": "/events/noticeboard", "menu_text": "NoticeBoard"},
            {"link": "/events/quotes", "menu_text": "Daily Quotes"}
        ]
    },
    {
        "menu_text": "Gallery",
        "sub_sub_menu": [
            {"link": "/events/gallerycategory", "menu_text": "Category"},
            {"link": "/events/galleryimageupload", "menu_text": "Image Upload"}
        ]
    }]

},
{
    "menu_text": "Academics",
    "menu_icon": "fa fa-compass",
    "acl_key": "dashboard.academics",
    "main_menu_key": "control.academics",
    "level": "0",
    "sub_menu": [{
        "link": "#",
        "menu_text": "Course Management ",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.coursemanagement",
        "sub_menu_key": "control.academics",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/academics/academicyear",
                "menu_text": "Academic Year",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.academicyear",
                "sub_sub_menu_key": "control.academics",
                "level": "2",
                "app_name": "academics",
                "model_name": "AcademicYear"},
                {

                    "link": "/academics/classes",
                    "menu_text": "Class",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.classes",
                    "sub_sub_menu_key": "control.academics",
                    "level": "2",
                    "app_name": "academics",
                    "model_name": "classes"},

               

                {

                    "link": "/academics/assignclasswiseteacher",
                    "menu_text": "Assign Teacher-Classes",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.assignclasswiseteacher",
                    "sub_sub_menu_key": "control.academics",
                    "level": "2",
                    "app_name": "academics",
                    "model_name": "assignclasswiseteacher"},
                {

                    "link": "/academics/assignsubjectwiseteacher",
                    "menu_text": "Assign Teacher-Subjects",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.assignsubjectwiseteacher",
                    "sub_sub_menu_key": "control.academics",
                    "level": "2",
                    "app_name": "academics",
                    "model_name": "assignsubjectwiseteacher"},
                {

                    "link": "/academics/assignclasssubject",
                    "menu_text": "Assign Subject-Class",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.assignclasssubject",
                    "sub_sub_menu_key": "control.academics",
                    "level": "2",
                    "app_name": "academics",
                    "model_name": "AssignClassSubject"},
                {

                    "link": "/academics/subject",
                    "menu_text": "Subjects",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.subjects",
                    "sub_sub_menu_key": "control.academics",
                    "level": "2",
                    "app_name": "academics",
                    "model_name": "Subjects"
            }]

    }, {
        "link": "#",
        "menu_text": "Grading System",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.academics",
        "sub_menu_key": "control.systemconfig",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/academics/gradingsystem",
                "menu_text": "Grading System",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.academics",
                "sub_sub_menu_key": "control.academics",
                "level": "2",
                "app_name": "academics",
                "model_name": "GradingSystem"}]

    },{
        "link": "#",
        "menu_text": "Assignments",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.academics",
        "sub_menu_key": "control.systemconfig",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/academics/assignment",
                "menu_text": "Assign Assignments",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.academics",
                "sub_sub_menu_key": "control.academics",
                "level": "2",
                "app_name": "academics",
                "model_name": "Assignment"}]

    },{
        "link": "#",
        "menu_text": "Attendance System",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.organization",
        "sub_menu_key": "control.systemconfig",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/academics/attendenceconfig",
                "menu_text": "Attendance Settings",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.organization",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "Organization"}, {

                "link": "/academics/attendence",
                "menu_text": "Attendance",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.organization",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "Organization"}, {

                    "link": "/academics/classworkingdays",
                    "menu_text": "Classworkingdays",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.classworkingdays",
                    "sub_sub_menu_key": "control.academics",
                    "level": "2",
                    "app_name": "academics",
                    "model_name": "classworkingdays"}]

    },
    {
        "link": "#",
        "menu_text": "Exam Management",
        "menu_icon": "fa fa-bar-chart",
        "acl_key": "dashboard.organization",
        "sub_menu_key": "control.systemconfig",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/academics/examcategory",
                "menu_text": "Exam Category",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.organization",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "Examcategory"}, {

                "link": "/academics/exam",
                "menu_text": "Exam",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.organization",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "Exam"}, {

                "link": "/academics/markentry",
                "menu_text": "Mark Entry",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.organization",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "MarkEntry"},
            {

                "link": "/academics/examshedule",
                "menu_text": "Exam Shedule",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.organization",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "ExamShedule"}]

    }]
},

{
    "menu_text": "Exam Management",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{
        "menu_text": "Questions",
        "sub_sub_menu": [
            {"link": "/exammanagement/questions", "menu_text": "Questions"},
            {"link": "/exammanagement/questioncategory", "menu_text": "Question Category"}]
    }, {
        "menu_text": "Online Exams",
        "sub_sub_menu": [
            {"link": "/exammanagement/onlineexam", "menu_text": "Online Exam"},
            {"link": "/exammanagement/studentexams", "menu_text": "Student Exams"},
            {"link": "/exammanagement/studentexams/upcoming_exams", "menu_text": "Upcoming Exams"}]
    }]
},

{
    "menu_text": "System Config",
    "menu_icon": "fa fa-cogs",
    "acl_key": "dashboard.systemconfig",
    "main_menu_key": "control.systemconfig",
    "level": "0",
    "sub_menu": [{
        "link": "#",
        "menu_text": "Configuration",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.configuration",
        "sub_menu_key": "control.systemconfig",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/systemconfig/country",
                "menu_text": "Country",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.country",
                "sub_sub_menu_key": "control.systemconfig",
                "level": "2",
                "app_name": "systemconfig",
                "model_name": "Country"},
                {

                    "link": "/systemconfig/state",
                    "menu_text": "State",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.state",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "State"},

                {

                    "link": "/systemconfig/district",
                    "menu_text": "District",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.district",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "District"},

                {

                    "link": "/systemconfig/citytown",
                    "menu_text": "City/Town",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.citytown",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "CityTown"},

                {

                    "link": "/systemconfig/languages",
                    "menu_text": "Language",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.languages",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Language"},

                {

                    "link": "/systemconfig/nationality",
                    "menu_text": "Nationality",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.nationality",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Nationality"},
                {

                    "link": "/systemconfig/religion",
                    "menu_text": "Religion",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.religion",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Religion"},
                {

                    "link": "/systemconfig/caste",
                    "menu_text": "Caste",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.caste",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Caste"},

                {

                    "link": "/systemconfig/relationship",
                    "menu_text": "Relationship",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.relationship",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Relationship"},
                {

                    "link": "/systemconfig/occupation",
                    "menu_text": "Occupation",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.occupation",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Occupation"},
                {

                    "link": "/systemconfig/hobbies",
                    "menu_text": "Hobbies",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.hobby",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Hobby"}]

    },
        {
            "link": "#",
            "menu_text": "Organization",
            "menu_icon": "fa fa-tasks",
            "acl_key": "dashboard.organization",
            "sub_menu_key": "control.systemconfig",
            "level": "1",
            "sub_sub_menu":
                [{

                    "link": "/systemconfig/organization",
                    "menu_text": "Organization",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.organization",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Organization"}]

        },
        {
            "link": "#",
            "menu_text": "Sms/Email",
            "menu_icon": "fa fa-tasks",
            "acl_key": "dashboard.sms/email",
            "sub_menu_key": "control.systemconfig",
            "level": "1",
            "sub_sub_menu":
                [{

                    "link": "/systemconfig/smsconfig",
                    "menu_text": "Sms Config",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.smsconfig",
                    "sub_sub_menu_key": "control.systemconfig",
                    "level": "2",
                    "app_name": "systemconfig",
                    "model_name": "Smsconfig"},

                    {

                        "link": "/systemconfig/smscredentials",
                        "menu_text": "Sms Credentials",
                        "menu_icon": "fa fa-tasks",
                        "acl_key": "dashboard.admin.smscredentials",
                        "sub_sub_menu_key": "control.systemconfig",
                        "level": "2",
                        "app_name": "systemconfig",
                        "model_name": "SmsCredentials"},

                    {

                        "link": "/systemconfig/emailconfig",
                        "menu_text": "Email Config",
                        "menu_icon": "fa fa-tasks",
                        "acl_key": "dashboard.admin.emailconfig",
                        "sub_sub_menu_key": "control.systemconfig",
                        "level": "2",
                        "app_name": "systemconfig",
                        "model_name": "Emailconfig"},

                    {

                        "link": "/systemconfig/emailcredentials",
                        "menu_text": "Email Credentials",
                        "menu_icon": "fa fa-tasks",
                        "acl_key": "dashboard.admin.emailcredentials",
                        "sub_sub_menu_key": "control.systemconfig",
                        "level": "2",
                        "app_name": "systemconfig",
                        "model_name": "EmailCredentials"}]

        }]
},
{
    "menu_text": "Library",
    "menu_icon": "fa fa-book",
    "acl_key": "dashboard.library",
    "sub_menu": [{
        "menu_text": "Manage Library",
        "menu_icon": "fa fa-tasks",
        "sub_sub_menu":
            [{

                "link": "/library/bookcategory",
                "menu_text": "Book Category",
                "menu_icon": "fa fa-tasks"}, {

                "link": "/library/books",
                "menu_text": "Books",
                "menu_icon": "fa fa-tasks"}, {

                "link": "/library/bookvendor",
                "menu_text": "Book Vendors",
                "menu_icon": "fa fa-tasks"}, {

                "link": "/library/cupboard",
                "menu_text": "Cupboard",
                "menu_icon": "fa fa-tasks"},
             
            {

                "link": "/library/bookstatus",
                "menu_text": "Book Status",
                "menu_icon": "fa fa-tasks"}, {

                "link": "/library/fine",
                "menu_text": "Fines",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.fine",
                "sub_sub_menu_key": "control.library",
                "level": "2",
                "app_name": "library",
                "model_name": "Fine"}, {

                "link": "/library/issuebook",
                "menu_text": "Issue Book",
                "menu_icon": "fa fa-tasks"},
                {

                    "link": "/library/returnrenewbook",
                    "menu_text": "Return/Renew Book",
                    "menu_icon": "fa fa-tasks"}]

    }]
},
{
    "menu_text": "Administration",
    "menu_icon": "fa fa-thumb-tack",
    "acl_key": "dashboard.administration",
    "sub_menu": [{
        "menu_text": "Transport",
        "menu_icon": "fa fa-tasks",
        "sub_sub_menu":
            [{

                "link": "/administration/busallocation",
                "menu_text": "Bus Allocation",
                "menu_icon": "fa fa-tasks"}, {

                "link": "/administration/driverdetails",
                "menu_text": "Driver Details",
                "menu_icon": "fa fa-tasks"}, {

               

                "link": "/administration/manageroute",
                "menu_text": "Route",
                "menu_icon": "fa fa-tasks"}, {

                "link": "/administration/vehicledetails",
                "menu_text": "Vehicle Details",
                "menu_icon": "fa fa-tasks"}]

    }]
},
{
    "menu_text": "Fees",
    "menu_icon": "fa fa-money",
    "sub_menu": [{
        "menu_text": "Manage Fee",
        "sub_sub_menu": [
            {"link": "/fees/bank", "menu_text": "Bank"},
            {"link": "/fees/feecategorydetails", "menu_text": "Fee Details"},
            {"link": "/fees/feecollectcategory", "menu_text": "Fee Category"},
            {"link": "/fees/feepaymenttransaction", "menu_text": "Fee Transaction"}]
    }]
},
{
    "menu_text": "Extra Curricular",
    "menu_icon": "fa fa-coffee",
    "acl_key": "dashboard.extracurricularactivities",
    "main_menu_key": "control.extracurricularactivities",
    "level": "0",
    "sub_menu": [{
        "link": "#",
        "menu_text": "Activity Management",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.extracurricularactivitiesmanagement",
        "sub_menu_key": "control.extracurricularactivities",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/extracurricularactivities/category",
                "menu_text": "Category",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.extracurricularactivities",
                "sub_sub_menu_key": "control.extracurricularactivities",
                "level": "2",
                "app_name": "extracurricularactivities",
                "model_name": "Category"},

                {

                    "link": "/extracurricularactivities/activities",
                    "menu_text": "Activity",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.extracurricularactivities",
                    "sub_sub_menu_key": "control.extracurricularactivities",
                    "level": "2",
                    "app_name": "extracurricularactivities",
                    "model_name": "Activities"},
                {

                    "link": "/extracurricularactivities/studentactivity",
                    "menu_text": "StudentActivity",
                    "menu_icon": "fa fa-tasks",
                    "acl_key": "dashboard.admin.extracurricularactivities",
                    "sub_sub_menu_key": "control.extracurricularactivities",
                    "level": "2",
                    "app_name": "extracurricularactivities",
                    "model_name": "StudentActivity"}]

    }]
},
{
    "menu_text": "Human Resource",
    "menu_icon": "fa fa-book",
    "acl_key": "dashboard.humanresource",
    "sub_menu": [{
        "menu_text": "Human Resource",
        "menu_icon": "fa fa-tasks",
        "sub_sub_menu":
            [{

                "link": "/hr/designation",
                "menu_text": "Designation",
                "menu_icon": "fa fa-tasks"},
            {
                "link": "/hr/exportemployees",
                "menu_text": "Export Employee"},

                {

                "link": "/hr/employee",
                "menu_text": "Employee",
                "menu_icon": "fa fa-tasks"}]

    }, {
        "menu_text": "Employee Config",
        "menu_icon": "fa fa-tasks",
        "sub_sub_menu":
            [

                {

                "link": "/hr/holiday",
                "menu_text": "Holiday",
                "menu_icon": "fa fa-tasks"}]

    }, {
        "menu_text": "Leave Management",
        "menu_icon": "fa fa-tasks",
        "sub_sub_menu":
            [
            
                {

                "link": "/hr/leavetype",
                "menu_text": "Leave Type",
                "menu_icon": "fa fa-tasks"},

            

                {

                "link": "/hr/leavereporting",
                "menu_text": "Leave Reporting",
                "menu_icon": "fa fa-tasks"},

                {

                "link": "/hr/leaveapplications",
                "menu_text": "Leave Applications",
                "menu_icon": "fa fa-tasks"}]

    },{
        "menu_text": "Teacher Management",
        "menu_icon": "fa fa-tasks",
        "sub_sub_menu":
            [
           

                {

                "link": "/hr/teachermanagement",
                "menu_text": "Teacher",
                "menu_icon": "fa fa-tasks"}]

    }]
}, {
    "menu_text": "Parents",
    "menu_icon": "fa fa-male",
    "acl_key": "dashboard.parents",
    "main_menu_key": "control.parents",
    "level": "0",
    "sub_menu": [{
        "link": "#",
        "menu_text": "Manage Parents ",
        "menu_icon": "fa fa-tasks",
        "acl_key": "dashboard.parentmanagement",
        "sub_menu_key": "control.parents",
        "level": "1",
        "sub_sub_menu":
            [{

                "link": "/parent/parents",
                "menu_text": "Parents",
                "menu_icon": "fa fa-tasks",
                "acl_key": "dashboard.admin.parents",
                "sub_sub_menu_key": "control.parents",
                "level": "2",
                "app_name": "parents",
                "model_name": "ParentManagement"}]

    }]
},
{
    "menu_text": "Time Table",
    "menu_icon": "fa fa-calendar-o",
    "sub_menu": [{
        "menu_text": "Timetable Management",
        "sub_sub_menu": [
            {"link": "/timetable/timetables", "menu_text": "Time Tables"}]
    }]
},
{
    "menu_text": "Tasks",
    "menu_icon": "fa fa-calendar-o",
    "sub_menu": [{
        "menu_text": "Task Management",
        "sub_sub_menu": [
            {"link": "/utils/taskmanagement", "menu_text": "Task Management"}]
    }]
},
{
    "menu_text": "Feedback",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{
        "menu_text": "Feedback Management",
        "sub_sub_menu": [
            {"link": "/utils/feedbackmanagement", "menu_text": "Feedbacks"}]
    }]
},
{
    "menu_text": "Template",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{
        "menu_text": "Template",
        "sub_sub_menu": [
            {"link": "/utils/templates", "menu_text": "Templates"},
            {"link": "/utils/category", "menu_text": "Category"},
            {"link": "/utils/subcategory", "menu_text": "Sub Category"}
        ]
    }]
},
{
    "menu_text": "Document Uploader",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{
        "menu_text": "Documents",
        "sub_sub_menu": [
            {"link": "/documentuploader/chapter", "menu_text": "Chapter"},
            {"link": "/documentuploader/module", "menu_text": "Module"}
        ]
    }]
            
},

{
    "menu_text": "Hostel",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{
        "menu_text": "Hostel Management",
        "sub_sub_menu": [
            # {"link": "/hostel/hostelcategory", "menu_text": "category"},
            {"link": "/hostel/hostels", "menu_text": "Hostels"},
            {"link": "/hostel/room", "menu_text": "Room"},
            {"link": "/hostel/studentallocation", "menu_text": "Student Allocation"}
        ]
    }]
},
{
    "menu_text": "Inventory",
    "menu_icon": "fa fa-tasks",
    "sub_menu": [{
        "menu_text": "Inventory Management",
        "sub_sub_menu": [
            # {"link": "/hostel/hostelcategory", "menu_text": "category"},
            {"link": "/inventory/productcategory", "menu_text": "Product Category"},
            {"link": "/inventory/producttype", "menu_text": "Product Type"},
            {"link": "/inventory/brand", "menu_text": "Product Brand"},
            {"link": "/inventory/department", "menu_text": "Department"},
            {"link": "/inventory/product", "menu_text": "Product"},
            {"link": "/inventory/supplier", "menu_text": "Supplier"},
            {"link": "/inventory/stockmovement", "menu_text": "Stock Movement"}
        ]
    }]               
    
}
]
