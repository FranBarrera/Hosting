# -*- coding: utf-8 -*-

from del_functions import *
import sys, os

name=(sys.argv[1])
domain=(sys.argv[2])


delete_directory(name,domain)
delete_db(name)
delete_ldap(name)
delete_zone(domain)
delete_zone(domain)

os.system('service apache2 restart 1>/dev/null 2>/dev/null')
os.system('service bind9 restart 1>/dev/null 2>/dev/null')