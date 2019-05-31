"""
* If you want to add a new menu then update 
    dashboard/sync_dashboard_menu.py --> NEW_MENU_ITEMS

now run::
    $ ./manage.py shell
    >>> from dashboard import sync_dashboard_menu
    >>> sync_dashboard_menu.sync()

Dont forget to add it to dashboard/dashboard_menu.py --> SIDE_BAR_MENUS
"""

from .models import AclPermissions,SubMenus,SubSubMenus,Roles


NEW_MENU_ITEMS =  [
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
}

]

def add_dashboard_menu(new_menu_item):
    """
    SYNC Database to update dashboard_menu change.
    """
    deleted_items = AclPermissions.objects.filter(menu_text=new_menu_item['menu_text']).delete()
    print ('Deleted: ',deleted_items)
    for role in Roles.objects.all():
        model_menu = AclPermissions.objects.create(
            role = role, link = '#',menu_text= new_menu_item['menu_text'],icon = new_menu_item['menu_icon'],
        )
        print()
        print(model_menu.menu_text,role)
        print('='*20)
        for submenu in new_menu_item['sub_menu']:
            model_submenu = SubMenus.objects.create(main_menu = model_menu,menu_text = submenu['menu_text'])
            print('  ', model_submenu.menu_text)
            for subsubmenu in submenu['sub_sub_menu']:
                model_subsubmenu = SubSubMenus.objects.create(
                    sub_menu = model_submenu,menu_text = subsubmenu['menu_text'],link = subsubmenu['link'],
                )
                print('    ', model_subsubmenu.menu_text)
# if __name__=='__main__':
def sync():
    for item in NEW_MENU_ITEMS:
        # if NEW_MENU_ITEMS:
        # deleted_items = AclPermissions.objects.filter(menu_text=item['menu_text']).delete()

        # print ('Deleted: ',deleted_items)

        add_dashboard_menu(item)
