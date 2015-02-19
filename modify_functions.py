import os

def modify_db(name,passwd):
	import MySQLdb
	db = MySQLdb.connect(host='localhost', user='root', passwd='asdasd')
	cursor = db.cursor()
	cursor.execute("SET PASSWORD FOR '%s' = PASSWORD('%s')" % (name,passwd))
	db.commit()
	print 'password mysql modificada'

def modify_ldap(name,passwd):
	from jinja2 import Environment, FileSystemLoader
	os.system('touch /tmp/modify.ldif')
	ldif = open('/tmp/modify.ldif','w')
	env = Environment(loader=FileSystemLoader('templates'))
	template = env.get_template('ldap_template.tpl')
	out = template.render(name=name,passwd=passwd)
	ldif.write(out)
	ldif.close()
	os.system('ldapmodify -D "cn=admin,dc=example,dc=com" -w asdasd -f /tmp/modify.ldif 1>/dev/null 2>/dev/null')
	print 'password ldap modificada'