# -*- coding: utf-8 -*-

from modify_functions import *
import sys, os

name=(sys.argv[1])
passwd=(sys.argv[2])

modify_db(name,passwd)
modify_ldap(name,passwd)