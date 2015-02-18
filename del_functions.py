# -*- coding: utf-8 -*-

import os

def delete_db(name):
	import MySQLdb
	db = MySQLdb.connect(host='localhost', user='root', passwd='super')
	cursor = db.cursor()
	cursor.execute('drop database %s' %name)
	db.commit()
