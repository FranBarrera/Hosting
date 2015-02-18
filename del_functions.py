# -*- coding: utf-8 -*-

import os

def delete_db(name):
	import MySQLdb
	db = MySQLdb.connect(host='localhost', user='root', passwd='super')
	cursor = db.cursor()
	cursor.execute('drop database %s' %name)
	db.commit()


def delete_directory(name,domain):
	os.system('rm -r /var/www/users/%s' %name)
	os.system('rm /etc/apache2/sites-avaliable/%s' %domain)
	os.system('a2dissite %s 1>/dev/null' %domain)



