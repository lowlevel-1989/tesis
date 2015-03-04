ssh usuario@formatcomtesis.com.ve

if not exist ~/src
	mkdir ~/src

cd ~/src
wget http://bitbucket.org/ianb/virtualenv/get/tip.gz
tar -xvzf tip.gz
rm tip.gz
mv ianb-virtualenv-1f9dfb2437f1/ virtualenv
python virtualenv/virtualenv.py --distribute ~/django/modules
echo 'source ~/django/modules/bin/activate' >> ~/.bash_profile
exit

scp -r ~/Proyectos/tesis/biblioteca usuario@formatcomtesis.com.ve:/home/usuario/django/
ssh usuario@formatcomtesis.com.ve
cd ~/django/biblioteca
pip install -r requirements/production.txt 

biblioteca/settings.py
	line 19: DEBUG = True
	change
	line 19: DEBUG = False

./manage.py collectstatic

touch ~/www/cgi-bin/tesis.py

	#!/home/usuario/django/modules/bin/python
	import os, sys

	sys.path.insert(0, '/home/usuario/django/modules')
	sys.path.insert(0, '/home/usuario/django/biblioteca')

	os.environ['DJANGO_SETTINGS_MODULE'] = "biblioteca.settings"
	from django.core.servers.fastcgi import runfastcgi
	runfastcgi(method="threaded", deamonize="false")


htaccess
	For Django to respond to URL requests, those urls need to be fed into the tesis.py script.
	For testing I routed everything from /api to the cgi script by adding the following lines 
	to my top-level htaccess file:

		RewriteEngine on
		RewriteRule ^cgi-bin/ - [L]
		RewriteRule ^api/(.*)$ /cgi-bin/tesis.py/$1 [QSA,L]

		Options -Indexes