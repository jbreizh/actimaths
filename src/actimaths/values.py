#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from time import strftime
from os.path import join
from os import environ, name
from sys import  getfilesystemencoding, platform

def home():
	if name == 'nt':
		return unicode(environ['USERPROFILE'], getfilesystemencoding())
	elif platform == "darwin":	
		return unicode(environ['HOME'], getfilesystemencoding())
	else:
		return unicode(environ['HOME'], getfilesystemencoding())

def configdir():
	if name == 'nt':
		return join(unicode(environ['APPDATA'], getfilesystemencoding()),"actimaths")
	elif platform == "darwin":	
		return join(home(), "Library", "Application Support", "Actimaths")
	else:
		return join(home(), ".config", "actimaths")

VERSION = "1.12"
WEBSITE = "http://mathecailloux.ile.nc/article147/aide-en-ligne-d-actimaths"
HOME = home()
CONFIGDIR = configdir()
DESCRIPTION = u"Actimaths est un fork de Pyromaths qui permet de créer des fiches d'activités mentales avec leurs corrigés au format LaTeX et PDF."
COPYRIGHT_YEAR = strftime("%Y")
COPYRIGHTS = "Jean-Baptiste Le Coz"
MAIL = "jb.lecoz@gmail.com"
CREDITS = [u"Jérôme Ortais", u"David Robert", u"Yves Gesnel", u"Arnaud Kientz", u"Guillaume Barthélémy", u"Nicolas Bissonnier", u"Nicolas Pourcelot", u"Jacqueline Gouguenheim-Desloy"]
LICENSE = "GPL"
