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

 	f_uidnumber = open('f_uidnumber', 'r')
 	uidnumber = f_uidnumber.readline()
 	f_uidnumber.close()

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
	attrs['uidNumber'] = uidnumber
	attrs['gidNumber'] = uidnumber
	attrs['homeDirectory'] = '/var/www/users/'+name
	attrs['userPassword'] = passwd_encrypt
	attrs['loginShell'] = '/bin/bash'

	# Convert dict to ldif
	ldif = modlist.addModlist(attrs)

	# add entry
	l.add_s(dn,ldif)

	# disconnect server
	l.unbind_s()

 	f_uidnumber = open('f_uidnumber', 'w')
 	uidnumber=int(uidnumber)+1
 	f_uidnumber.write(str(uidnumber))

 	f_uidnumber.close()


def create_zone(domain):
	from jinja2 import Environment, FileSystemLoader
	fdns = open('/etc/bind/named.conf.local','a')
	env = Environment(loader=FileSystemLoader('/etc/bind/'))
	template = env.get_template('bind_template.tpl')
	out = template.render(domain=domain)
	fdns.write(out)
	fdns.close()

def create_dns(domain):
	from jinja2 import Environment, FileSystemLoader
	os.system('touch /var/cache/bind/%s' %domain)
	fdns = open('/var/cache/bind/%s' %domain,'w')
	env = Environment(loader=FileSystemLoader('/etc/bind/'))
	template = env.get_template('dns_template.tpl')
	out = template.render(domain=domain)
	fdns.write(out)
	fdns.close()