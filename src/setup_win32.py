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

from distutils.core import setup
import glob, os
import py2exe, innosetup
from actimaths.values import VERSION, DESCRIPTION, LICENSE, COPYRIGHTS, MAIL, WEBSITE

def find_data_files(source,target,patterns):
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path,[]).append(filename)
    return sorted(ret.items())

setup_iss = '''
[Setup]
Compression=lzma/max
OutputBaseFilename=actimaths-%s-win32
[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}" ;Flags: unchecked
[Icons]
Name: "{group}\Actimaths";  Filename: "{app}\\actimaths-gui.exe"
Name: "{commondesktop}\Actimaths"; Filename: "{app}\\actimaths-gui.exe"; Tasks: desktopicon
''' % VERSION

setup(name = "Actimaths",
    version = VERSION,
    description = DESCRIPTION,
    license = LICENSE,
    author = COPYRIGHTS,
    author_email = MAIL,
    url = WEBSITE,
    packages=['actimaths',
              'actimaths.exercices_actimaths','actimaths.exercices_actimaths.outils',
              'actimaths.exercices_pyromaths','actimaths.exercices_pyromaths.outils'],
    data_files = find_data_files('data','data/',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"]) + [('imageformats',['C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qjpeg4.dll'])],
    platforms = ['windows'],
    options =
    {
        'py2exe':
        {
            "compressed": 1, "optimize": 2, "bundle_files": 3,
            "includes":["sip", "gzip"]
        },
       'innosetup':
       {
           'inno_script': setup_iss,
           'compressed': True,
       }
    },
    zipfile = None,
    windows=[
      {'script': "actimaths-gui",
       'icon_resources': [(1, 'data/actimaths.ico')],
       }]
    )

