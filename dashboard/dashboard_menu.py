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
}
]
