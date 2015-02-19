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
	os.system('rm /etc/apache2/sites-available/%s' %domain)
	os.system('a2dissite %s 1>/dev/null' %domain)

def delete_zone(domain):
	os.system('rm /var/cache/bind/%s' %domain)

def delete_dns(domain):
	fread = open('/etc/bind/named.conf.local','r')
	lineas = fread.readlines()
	fread.close()
	fwrite = open('/etc/bind/named.conf.local','w')
	for linea in lineas:
		if linea == '# zona de %s\n' % domain:
			indice = lineas.index(linea)
	for i in lineas[indice:indice+5]:
		lineas.remove(i)
	for i in lineas:
		fwrite.write(i)
	fwrite.close()


def delete_ldap(name):
	os.system('ldapdelete -x -D "cn=admin,dc=example,dc=com" "uid=%s,ou=People,dc=example,dc=com" -w super'%name)
	os.system('ldapdelete -x -D "cn=admin,dc=example,dc=com" "cn=%s,ou=Group,dc=example,dc=com" -w super' %name)




