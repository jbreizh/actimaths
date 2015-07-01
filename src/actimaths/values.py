#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Actimaths
# Un programme en Python qui permet de créer des presentation de
# mathématiques niveau collège ainsi que leur corrigé en LaTeX.
# Copyright (C) 2013 -- Jean-Baptiste Le Coz (jb.lecoz@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#

from time import strftime
from os.path import normpath, dirname, exists, abspath, join
from os import environ, name
from sys import  executable, getfilesystemencoding, platform
import sys

def we_are_frozen():
    """Returns whether we are frozen via py2exe.
    This will affect how we find out where we are located."""
    return hasattr(sys, "frozen")

def data_dir():
    """Renvoie le dossier data, selon qu'on utilise actimaths à partir des sources, de l'exécutable win32 ou du paquet deb"""
    if we_are_frozen():
        return join(normpath(dirname(unicode(executable, getfilesystemencoding()))), 'data')
    elif exists(join(abspath(dirname(__file__)),'../data/')):
        return normpath(join(abspath(dirname(__file__)),'../data/'))
    else:
        return '/usr/share/actimaths/'

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

VERSION = "1.25"
WEBSITE = "http://mathecailloux.ile.nc"
DATADIR = data_dir()
HOME = home()
CONFIGDIR = configdir()
DESCRIPTION = u"Actimaths est un fork de Pyromaths qui permet de créer des fiches d'activités mentales avec leurs corrigés au format LaTeX et PDF."
COPYRIGHT_YEAR = strftime("%Y")
COPYRIGHTS = "Jean-Baptiste Le Coz"
MAIL = "jb.lecoz@gmail.com"
CREDITS = [u"Jérôme Ortais", u"David Robert", u"Yves Gesnel", u"Arnaud Kientz", u"Guillaume Barthélémy", u"Nicolas Bissonnier", u"Nicolas Pourcelot", u"Jacqueline Gouguenheim-Desloy"]
LICENSE = "GPL"
