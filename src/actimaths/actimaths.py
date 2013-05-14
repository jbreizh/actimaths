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

from sys import argv, exit
from os import access, R_OK, makedirs
from os.path import join, isdir
from codecs import open
from PyQt4 import QtGui, QtCore

from values import CONFIGDIR
from system import create_config_file, modify_config_file, test
from interface import Ui_MainWindow


## class StartQT4
class StartQT4(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#===============================================================================
# Demarrage de actimaths
#===============================================================================
def main():
    ## Création du fichier de configuration si inexistant
    if not access(join(CONFIGDIR, "actimaths.xml"), R_OK):
        if not isdir(CONFIGDIR): makedirs(CONFIGDIR)
        f = open(join(CONFIGDIR, "actimaths.xml"), encoding='utf-8', mode='w')
        f.write(u"" + create_config_file())
        f.close()
    modify_config_file(join(CONFIGDIR, "actimaths.xml"))
    app = QtGui.QApplication(argv)
    actimaths = StartQT4()
    actimaths.show()
    test(actimaths)
    exit(app.exec_())

if __name__ == "__main__":
	main()
