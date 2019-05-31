====================================
Chapter 4: Deleting a User (student)
====================================

Dashboard Userroles
-------------------

::

	DELETE FROM "dashboard_userroles"
	WHERE (("user_id" = '33'));

Parents Info Student
--------------------

::

	DELETE FROM "parents_info_student"
	WHERE (("users_id" = '33'));

Students Master
---------------

::

	DELETE FROM "students_master"
	WHERE (("stu_user_id" = '33'));

Students Migration
------------------

::

	DELETE FROM "students_migration"
	WHERE (("student_id" = '33'));

Students Info
-------------

::

	DELETE FROM "students_info"
	WHERE (("user_id" = '33'));

Dashboard UserProfile
----------------------

::

	DELETE FROM "dashboard_user_profile"
	WHERE (("user_id" = '33'));

Dashboard Users
---------------

::

	DELETE FROM "dashboard_users"
	WHERE (("id" = '33'));


Single query
============

::

	DELETE FROM "dashboard_userroles"
	WHERE (("user_id" = '33'));
	DELETE FROM "parents_info_student"
	WHERE (("users_id" = '33'));
	DELETE FROM "students_master"
	WHERE (("stu_user_id" = '33'));
	DELETE FROM "students_migration"
	WHERE (("student_id" = '33'));
	DELETE FROM "students_info"
	WHERE (("user_id" = '33'));
	DELETE FROM "dashboard_user_profile"
	WHERE (("user_id" = '33'));
	DELETE FROM "dashboard_users"
	WHERE (("id" = '33'));