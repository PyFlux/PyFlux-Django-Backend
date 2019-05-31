# REST Api

visit: https://DonamsInnovations.gitlab.io/Vidhyadhan-Back-End

## migrate and populatedb

	./manage.py migrate
	./manage.py createadminuser
	./manage.py populatedb

## digitalocean setup

	$ apt-get update
	$ apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

Change dir: `$ cd /var/www/`
Clone the repo: `$ git clone https://gitlab.com/DonamsInnovations/Vidhyadhan-Back-End.git`
rename: `$ mv Vidhyadhan-Back-End backend`
Change dir: `$ cd backend`

Install Python 3.6::

	$ sudo add-apt-repository ppa:jonathonf/python-3.6
	$ sudo apt-get update
	$ sudo apt-get install python3.6

Create virtual and install django::

	$ apt install python3-pip
	$ pip3 install virtualenv
	$ virtualenv --python=/usr/bin/python3.6 venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt

Install PostgreSQL::

	$ apt-get install postgresql postgresql-contrib
	$ sudo -u postgres psql
	ALTER USER postgres WITH PASSWORD 'root';
	create database vidhyadhanbackend;
	\q

VirtualHost::

	$ vim /etc/apache2/sites-available/backend.conf 
	Listen 8000
	<VirtualHost *:8000>
	    WSGIDaemonProcess backendapp python-home=/var/www/backend/venv python-path=/var/www/backend
	    WSGIProcessGroup backendapp
	    WSGIPassAuthorization On
	    WSGIScriptAlias / /var/www/backend/backend/wsgi.py
	    ErrorLog /var/www/backend/error.log
	    CustomLog /var/www/backend/access.log combined
	</VirtualHost>

restart apache::

	$ a2ensite backend.conf
	$ service apache2 restart


to test celery::
 
    celery -A backend worker -l info -B
    celery -A backend worker -l info -B --concurrency=1

to see process `ps aux | grep celery`

to kill celery `pkill -9 -f 'celery'`


### Celery Installation

**Install Rabbitmq:**

	$ echo 'deb http://www.rabbitmq.com/debian/ testing main' |
	     sudo tee /etc/apt/sources.list.d/rabbitmq.list
	$ apt-get update
	$ apt-get install rabbitmq-server

To run on mac : 

    /usr/local/sbin/rabbitmq-server

**Daemonization here is a nice tutorial**

	$ apt-get install supervisor

Then, add `/etc/supervisor/conf.d/celery_proj_worker.conf` file:

	; celery -A backend worker -l info -B
	; Worker
	[program:projworker]
	command=/var/www/dev.vidhyadhan.in/backend/venv/bin/celery -A backend worker -l info
	directory=/var/www/dev.vidhyadhan.in/backend
	numprocs=1
	autostart=true
	autorestart=true
	startsecs=10
	stopwaitsecs = 600 
	killasgroup=true
	priority=998

Also add `/etc/supervisor/conf.d/celery_proj_beat.conf` file:

	; Beat
	[program:projbeat]
	command=/var/www/dev.vidhyadhan.in/backend/venv/bin/celery -A backend beat -l info
	directory=/var/www/dev.vidhyadhan.in/backend
	numprocs=1
	autostart=true
	autorestart=true
	startsecs=10
	priority=999

for Socket.IO Server add `/etc/supervisor/conf.d/socketio.conf` file:

	[program:socketio]
	command = /var/www/dev.vidhyadhan.in/backend/venv/bin/python /var/www/dev.vidhyadhan.in/backend/socketio_server.py
	

super visor logs can be found in:

	/var/log/supervisor/

update change for supervisor:

	$ supervisorctl reread
	$ supervisorctl update

Finally we can start the services :

	$ supervisorctl start projworker
	$ supervisorctl start projbeat

or even check the status/stop/restart:

	$ supervisorctl stop projworker
	$ supervisorctl restart projworker
	$ supervisorctl status projworker


### PDF Generation::

For `pdfkit` you need to Install `wkhtmltopdf`, [vpn setup](https://github.com/JazzCore/python-pdfkit/wiki/Using-wkhtmltopdf-without-X-server):

install ::

	sudo apt-get install wkhtmltopdf

if there is an xserver problem::

	wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
	tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz 
	cp wkhtmltox/bin/wk* /usr/local/bin/
	chmod +x /usr/local/bin/wkhtmltopdf

<!-- Installing Simple-Crypt:

     $ sudo apt update
     $ sudo apt-get install gcc-4.8
     $ sudo apt-get install g++
     $ sudo apt-get installsudo libffi-dev
     $ sudo apt-get install openssl -->

### Permission Check:

+ Need to block port `81` from outside users 
+ Added middleware, so that only authenticated users can access.