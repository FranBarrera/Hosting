# -*- coding: utf-8 -*-

from functions import *
import sys, os

name=(sys.argv[1])
domain=(sys.argv[2])


create_directory(name,domain)
create_db(name)
user_ldap(name)
create_zone(domain)
create_dns(domain)

os.system('service apache2 restart 1>/dev/null 2>/dev/null')
os.system('service bind9 restart 1>/dev/null 2>/dev/null')