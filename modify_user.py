# -*- coding: utf-8 -*-

from modify_functions import *
import sys, os

tipo=(sys.argv[1])
name=(sys.argv[2])
passwd=(sys.argv[3])

if tipo == '-sql':
	modify_db(name,passwd)
elif tipo == '-ftp':
	modify_ldap(name,passwd)
else:
	print 'Debe especificar un tipo correcto'