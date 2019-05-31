from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
    	# https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
        import dashboard.signals 
