# -*- coding: utf-8 -*-

import os

def delete_db(name):
	import MySQLdb
	db = MySQLdb.connect(host='localhost', user='root', passwd='super')
	cursor = db.cursor()
	cursor.execute('drop database %s' %name)
	cursor.execute('drop user %s' %name)
	db.commit()


def delete_directory(name,domain):
	os.system('rm -r /var/www/users/%s' %name)
	os.system('rm /etc/apache2/sites-avaliable/%s' %domain)
	os.system('a2dissite %s 1>/dev/null' %domain)

def delete_zone(domain):
	os.system('rm /var/cache/bind/%s' %domain)

def delete_ldap(name):
	ldapdelete -x -D "cn=admin,dc=example,dc=com" "uid=alenieto,ou=People,dc=example,dc=com" -W
	ldapdelete -x -D "cn=admin,dc=example,dc=com" "cn=alenieto,ou=Group,dc=example,dc=com" -W




