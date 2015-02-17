# -*- coding: utf-8 -*-

from functions.py import *

name=(sys.argv[1])
domain=(sys.argv[2])


create_directory(name,domain)
create_db(name)
user_ldap(name)
create_zone(domain)
create_dns(domain)