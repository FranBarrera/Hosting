# -*- coding: utf-8 -*-

import os

def create_directory(name,domain):
	if os.path.isdir('/var/www/users/%s' %name) != True and os.path.isdir('/etc/apache2/sites-availables/%s' %domain) != True:
		os.system('mkdir /var/www/%s' %name)
		os.system('mkdir /etc/apache2/sites-availables/%s' %domain)
	else:
		print 'Name or Domain already exists.'
