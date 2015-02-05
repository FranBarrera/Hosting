# -*- coding: utf-8 -*-

import os

def create_directory(name,domain):
	from jinja2 import Environment, FileSystemLoader
	if os.path.isdir('/var/www/users/%s' %name) != True and os.path.isfile('/etc/apache2/sites-availables/%s' %domain) != True:
		os.system('mkdir /var/www/%s' %name)
		os.system('touch /etc/apache2/sites-availables/%s' %domain)
		fdomain = open('/etc/apache2/sites-availables/%s' %domain)
		env = Environment(loader=FileSystemLoader('/etc/apache2/sites-availables'))
		template = env.get_template('template.tpl')
		out = template.render(name=name,domain=domain)
		fdomain.write(out)
		fdomain.close()
	else:
		print 'Name or Domain already exists.'

def generate_passwd
	from random import choice
	passwd = ''
	length = 15
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	passwd = p.join([choice(valores) for i in range(longitud)])
	return passwd