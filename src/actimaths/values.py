#!/usr/bin/python
# -*- coding: utf-8 -*-
#
from time import strftime
from os.path import normpath, dirname, exists, abspath, join
from os import environ, name
from sys import executable, getfilesystemencoding, platform
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

if name == 'nt':
    def home():
        return unicode(environ['USERPROFILE'], getfilesystemencoding())
    def configdir():
        return join(unicode(environ['APPDATA'], getfilesystemencoding()),"actimaths")
elif platform == "darwin":
    def home():
        return unicode(environ['HOME'], getfilesystemencoding())
    def configdir():
        return join(home(), "Library", "Application Support", "Actimaths")
else:
    def home():
        return unicode(environ['HOME'], getfilesystemencoding())
    def configdir():
        return join(home(), ".config", "actimaths")

VERSION = "1.12"
WEBSITE = "http://mathecailloux.ile.nc/article147/aide-en-ligne-d-actimaths"
DATADIR = data_dir()
HOME = home()
CONFIGDIR = configdir()
DESCRIPTION = u"Actimaths est un fork de Pyromaths qui permet de créer des fiches d'activités mentales avec leurs corrigés au format LaTeX et PDF."
COPYRIGHT_YEAR = strftime("%Y")
COPYRIGHTS = "Jean-Baptiste Le Coz"
MAIL = "jb.lecoz@gmail.com"
CREDITS = [u"Jérôme Ortais", u"David Robert", u"Yves Gesnel", u"Arnaud Kientz", u"Guillaume Barthélémy", u"Nicolas Bissonnier", u"Nicolas Pourcelot", u"Jacqueline Gouguenheim-Desloy"]
LICENSE = "GPL"
