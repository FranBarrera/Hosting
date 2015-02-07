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

def generate_passwd():
	from random import choice
	passwd = ''
	length = 15
	values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	passwd = passwd.join([choice(values) for i in range(length)])
	return passwd

def create_db(name):
	import MySQLdb
	passwd = generate_passwd()
	db = MySQLdb.connect(host='localhost', user='root', passwd='super')
	cursor = db.cursor()
	cursor.execute('create database %s' %name)
	cursor.execute("grant all privileges on %s.* to " %name+"%s" %name+" identified by "+"'%s'" %passwd)
	db.commit()
	return 'password = %s' %passwd

def group_ldap(name):
	import ldap
	from ldap import modlist
 
	l = ldap.initialize("ldap://localhost.example.com:389/")
	l.simple_bind_s("cn=admin,dc=example,dc=com","asdasd")
	dn="cn="+name+",ou=Group,dc=example,dc=com" 

	attrs = {}
	attrs['objectclass'] = ['top','posixGroup']
	attrs['cn'] = name
	attrs['gidNumber'] = '2000'

	ldif = modlist.addModlist(attrs)
	l.add_s(dn,ldif)
	l.unbind_s()


def user_ldap(name,passwd):
	import ldap
	from ldap import modlist
	from passlib.hash import pbkdf2_sha256
 
	passwd_encrypt = pbkdf2_sha256.encrypt(passwd, rounds=200000, salt_size=16)
	# Open connection
	l = ldap.initialize("ldap://localhost.example.com:389/")

	# login with user admin
	l.simple_bind_s("cn=admin,dc=example,dc=com","asdasd")

	# new entry
	dn="cn="+name+",ou=People,dc=example,dc=com" 

	# add attributes
	attrs = {}
	attrs['objectclass'] = ['top','posixAccount','account']
	attrs['cn'] = name
	attrs['uid'] = name
	attrs['uidNumber'] = '2000'
	attrs['gidNumber'] = '2000'
	attrs['homeDirectory'] = '/var/www/users/'+name
	attrs['userPassword'] = passwd_encrypt
	attrs['loginShell'] = '/bin/bash'

	# Convert dict to ldif
	ldif = modlist.addModlist(attrs)

	# add entry
	l.add_s(dn,ldif)

	# disconnect server
	l.unbind_s()
