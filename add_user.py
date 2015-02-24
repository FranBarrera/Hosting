# -*- coding: utf-8 -*-

from add_functions import *
import sys, os

name=(sys.argv[1])
domain=(sys.argv[2])

if os.path.isdir('/var/www/users/%s' %name) != True and os.path.isfile('/etc/apache2/sites-availables/%s' %domain) != True:

	create_directory(name,domain)
	create_mysql
	create_db(name)
	user_ldap(name)
	create_zone(domain)
	create_dns(domain)

	os.system('service apache2 restart 1>/dev/null 2>/dev/null')
	os.system('service bind9 restart 1>/dev/null 2>/dev/null')
else:
	print 'Name or Domain already exists.'