

def modify_db(name,passwd):
	import MySQLdb
	passwd = generate_passwd()
	db = MySQLdb.connect(host='localhost', user='root', passwd='super')
	cursor = db.cursor()
	
	cursor.execute("SET PASSWORD FOR '%s' = PASSWORD('%s')" % (name,passwd))
	db.commit()
	print 'password modificada'

