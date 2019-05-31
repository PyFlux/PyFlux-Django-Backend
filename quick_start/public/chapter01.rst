=====================================
Chapter 1: Angular/DRF Authentication
=====================================

RestFramework Authentication
============================

Token authentication
--------------------

To use the `TokenAuthentication` scheme you'll need to include `rest_framework.authtoken` in your `INSTALLED_APPS` setting::

	INSTALLED_APPS = [
	    ...
	    'rest_framework.authtoken'
	]


The default authentication schemes may be set globally, using the `DEFAULT_AUTHENTICATION_CLASSES` setting. For example::

	REST_FRAMEWORK = {
	  'DEFAULT_AUTHENTICATION_CLASSES': (
	    'rest_framework.authentication.BasicAuthentication',
	    'rest_framework.authentication.SessionAuthentication',
	    'rest_framework.authentication.TokenAuthentication',
	  )
	}

When using `TokenAuthentication`, you may want to provide a mechanism for clients to obtain a token given the username and password. REST framework provides a built-in view to provide this behavior. To use it, add the `obtain_auth_token` view to your URLconf::

	from rest_framework.authtoken import views
	urlpatterns += [
	    url(r'^api-token-auth/',
	    	views.obtain_auth_token)
	]


The curl command line tool may be useful for testing token authenticated APIs. For example::

	$ curl -X POST http://xxx/api-token-auth/ -d "username=abc&password=mypass"
	{"token":"69b...07","user_id":1,"email":""}

	$ curl -X GET http://xxx/academicyear/ -H 'Authorization: Token 69b...07'