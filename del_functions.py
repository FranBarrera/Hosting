def delete_db(name):
	import MySQLdb
	passwd = generate_passwd()
	db = MySQLdb.connect(host='localhost', user='root', passwd='super')
	cursor = db.cursor()
	cursor.execute('drop database %s' %name)
	db.commit()
