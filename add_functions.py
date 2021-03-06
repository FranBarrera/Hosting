# -*- coding: utf-8 -*-

import os

def create_directory(name,domain):
	from jinja2 import Environment, FileSystemLoader
	os.system('mkdir /var/www/users/%s' %name)
	os.system('touch /etc/apache2/sites-available/%s' %domain)
	os.system('touch /var/www/users/%s/index.html' %name)
	os.system('touch /etc/apache2/sites-available/mysql_%s' %domain)
	fdomain = open('/etc/apache2/sites-available/%s' %domain ,'w')
	findex = open('/var/www/users/%s/index.html' %name ,'w')
	env = Environment(loader=FileSystemLoader('templates'))
	template = env.get_template('apache.tpl')
	out = template.render(name=name,domain=domain)
	fdomain.write(out)
	fdomain.close()
	template = env.get_template('index.tpl')
	out = template.render(domain=domain)
	findex.write(out)
	findex.close()
	os.system('a2ensite %s 1>/dev/null' %domain)

def create_mysql(domain):
	from jinja2 import Environment, FileSystemLoader
	fmysql = open('/etc/apache2/sites-available/mysql_%s' %domain,'w')
	env = Environment(loader=FileSystemLoader('templates'))
	template = env.get_template('mysql_template.tpl')
	out = template.render(domain=domain)
	fmysql.write(out)
	fmysql.close()
	os.system('a2ensite mysql_%s 1>/dev/null' %domain)


def generate_passwd():
	from random import choice
	passwd = ''
	length = 15
	values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	passwd = passwd.join([choice(values) for i in range(length)])
	return passwd



def encrypt(password):
	import hashlib
	from base64 import encodestring as encode
	from base64 import decodestring as decode

	salt = os.urandom(4)
	h = hashlib.sha1(password)
	h.update(salt)
	return "{SSHA}" + encode(h.digest() + salt)


def create_db(name):
	import MySQLdb
	passwd = generate_passwd()
	db = MySQLdb.connect(host='localhost', user='root', passwd='asdasd')
	cursor = db.cursor()
	cursor.execute('create database %s' %name)
	cursor.execute("grant all privileges on %s.* to " %name+"my%s" %name+" identified by "+"'%s'" %passwd)
	db.commit()
	print 'password mysql = %s' %passwd


def user_ldap(name):
	import ldap
	import ldap.modlist as modlist

	uidnumber = generate_uid()
	passwd = generate_passwd()


	l = ldap.initialize("ldap://hosting.example.com:389/")
	l.simple_bind_s("cn=admin,dc=example,dc=com","asdasd")
	dn="cn="+name+",ou=Group,dc=example,dc=com" 

	attrs = {}
	attrs['objectclass'] = ['top','posixGroup']
	attrs['cn'] = name
	attrs['gidNumber'] = uidnumber

	ldif = modlist.addModlist(attrs)
	l.add_s(dn,ldif)
	l.unbind_s()


	passwd_encrypt = encrypt(passwd)

	l = ldap.initialize("ldap://hosting.example.com:389/")
	l.simple_bind_s("cn=admin,dc=example,dc=com","asdasd")
	dn="uid="+name+",ou=People,dc=example,dc=com" 

	attrs = {}
	attrs['objectclass'] = ['top','posixAccount','account']
	attrs['cn'] = name
	attrs['uid'] = name
	attrs['uidNumber'] = uidnumber
	attrs['gidNumber'] = uidnumber
	attrs['homeDirectory'] = '/var/www/users/'+name
	attrs['userPassword'] = passwd_encrypt
	attrs['loginShell'] = '/bin/bash'

	ldif = modlist.addModlist(attrs)
	l.add_s(dn,ldif)
	l.unbind_s()
	os.system('chown -R %s:%s /var/www/users/%s' % (uidnumber,uidnumber,name))
	print 'password ftp = %s' %passwd


def create_zone(domain):
	from jinja2 import Environment, FileSystemLoader
	fdns = open('/etc/bind/named.conf.local','a')
	env = Environment(loader=FileSystemLoader('templates'))
	template = env.get_template('bind_template.tpl')
	out = template.render(domain=domain)
	fdns.write(out)
	fdns.close()

def create_dns(domain):
	from jinja2 import Environment, FileSystemLoader
	os.system('touch /var/cache/bind/%s' %domain)
	fdns = open('/var/cache/bind/%s' %domain,'w')
	env = Environment(loader=FileSystemLoader('templates'))
	template = env.get_template('dns_template.tpl')
	out = template.render(domain=domain)
	fdns.write(out)
	fdns.close()


def generate_uid():
	f_uidnumber = open('f_uidnumber', 'r')
	uidnumber = f_uidnumber.readline()
	f_uidnumber.close()

	f_uidnumber = open('f_uidnumber', 'w')
	uidnumber=int(uidnumber)+1
	f_uidnumber.write(str(uidnumber))
	f_uidnumber.close()
	return str(uidnumber)
