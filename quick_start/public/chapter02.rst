=====================
Chapter 2: Deployment
=====================

Digital Ocean Deployment
========================

Install Apache
--------------
::

	apt-get update
	apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
	cd /var/www/
	git clone https://gitlab.com/DonamsInnovations/Vidhyadhan-Back-End
	cd Vidhyadhan-Back-End

Create virtual environment
--------------------------
Create virtual environment and install requirements::
	
	pip3 install virtualenv
	virtualenv env
	source ./env/bin/activate
	pip install -r requirements.txt

Migrate and sync db
-------------------
::

	mkdir media
	chmod 777 media
	./manage.py makemigrations
	./manage.py migrate
	cd media/
	chmod 777 db.sqlite3
	./manage.py collectstatic

Edit apache config
------------------
::

	vi /etc/apache2/sites-available/vidhyadhan_api.conf
	<VirtualHost *:80>
	    ServerName api.helpservice.xyz
	    WSGIDaemonProcess vidhyadhanapi python-home=/var/www/Vidhyadhan-Back-End/env python-path=/var/www/Vidhyadhan-Back-End
	    WSGIProcessGroup vidhyadhanapi
	    WSGIScriptAlias / /var/www/Vidhyadhan-Back-End/backend/wsgi.py
	    ErrorLog /var/www/Vidhyadhan-Back-End/error.log
	    CustomLog /var/www/Vidhyadhan-Back-End/access.log combined
	</VirtualHost>

restart apache
--------------
::

	a2ensite vidhyadhan_api.conf
	service apache2 reload

lets encrypt for HTTPS
======================

comment the `WSGIDaemonProcess` line
------------------------------------

https://github.com/certbot/certbot/issues/1820

I had to comment the `WSGIDaemonProcess` line out before running letsencrypt. 

in **/etc/apache2/sites-available/Vidhyadhan-Back-End.conf**::

    <VirtualHost *:80>
        ServerName api.helpservice.xyz
        # WSGIDaemonProcess vidhyadhanapi python-home=/var/www/Vidhyadhan-Back-End/env python-path=/var/www/Vidhyadhan-Back-End
        ...

install the certificate
-----------------------

https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04::

    add-apt-repository ppa:certbot/certbot
    apt-get update
    apt-get install python-certbot-apache
    certbot --apache -d api.helpservice.xyz

uncommented `WSGIDaemonProcess`
-------------------------------
in **/etc/apache2/sites-available/Vidhyadhan-Back-End.conf**::

    <VirtualHost *:80>
        ServerName api.helpservice.xyz
        WSGIDaemonProcess vidhyadhanapi python-home=/var/www/Vidhyadhan-Back-End/env python-path=/var/www/Vidhyadhan-Back-End
        ...

restart apache
--------------
::

	service apache2 reload

Serve Static Files
==================

create a directory 'api' in `/var/www/static/`.

if you don't set up the static files
------------------------------------

create config file -> `/etc/apache2/sites-enabled/static.conf`::

    <VirtualHost *:80>
        ServerName static.helpservice.xyz
        DocumentRoot /var/www/static
    </VirtualHost>

run collectstatic
-----------------

::

	./manage.py collectstatic

add header in requests
======================

if you try to pass a valid Header and you get **Authentication credentials were not provided** error::

	curl -H "Authorization: Token 69b...07" http://xxx/orders/


https://stackoverflow.com/questions/26906630

you have to add **WSGIPassAuthorization On** in your **/etc/apache2/apache2.conf**. Otherwise authorization header will be stripped out by mod_wsgi.