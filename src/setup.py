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
import glob, os, sys
from actimaths.values import VERSION, DESCRIPTION, LICENSE, COPYRIGHTS, MAIL, WEBSITE
py2exe, innosetup = None, None
try:
    import py2exe, innosetup

except ImportError:
    pass

## Fonction d'import recursif des data_files
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

## Option specifique à windows
def _win_opt():
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

    return dict(platforms = ['windows'],
                data_files = [('imageformats',['C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qjpeg4.dll'])]
                           + find_data_files('data/images','data/images',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/modeles','data/modeles',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/onglets','data/onglets',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/packages','data/packages',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/vignettes','data/vignettes',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/texlive','data/texlive',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*","*/*/*/*/*/*","*/*/*/*/*/*/*","*/*/*/*/*/*/*/*","*/*/*/*/*/*/*/*/*","*/*/*/*/*/*/*/*/*/*","*/*/*/*/*/*/*/*/*/*/*","*/*/*/*/*/*/*/*/*/*/*/*","*/*/*/*/*/*/*/*/*/*/*/*/*"]),
                zipfile = None,
                windows=[dict(script = "actimaths-gui", icon_resources = [(1, 'data/actimaths.ico')])],
                options = dict(py2exe = dict(compressed = 1, optimize = 2, bundle_files = 3, includes = ["sip", "gzip" ]), innosetup=dict(inno_script=setup_iss,compressed= True)))

## Option specifique à linux
def _unix_opt():
    return dict(platforms = ['unix'],
                data_files = [(r'share/applications', [r'data/actimaths.desktop'])] 
                           + find_data_files('data/images','share/actimaths/images',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/modeles','share/actimaths/modeles',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/onglets','share/actimaths/onglets',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/packages','share/actimaths/packages',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"])
                           + find_data_files('data/vignettes','share/actimaths/vignettes',["*","*/*","*/*/*","*/*/*/*","*/*/*/*/*"]),     
                scripts = ["actimaths-gui"])

## Mise en place des options specifiques à la plateforme
if sys.platform == 'win32':
    options = _win_opt()
else:
    options = _unix_opt()

## Setup
setup(
    # Données du projet
    name = "actimaths",
    version = VERSION,
    description = DESCRIPTION,
    long_description = DESCRIPTION,
    license = LICENSE,
    author = COPYRIGHTS,
    author_email = MAIL,
    url = WEBSITE,
    # Packages python
    packages=['actimaths','actimaths.exercices_actimaths','actimaths.exercices_actimaths.outils','actimaths.exercices_pyromaths','actimaths.exercices_pyromaths.outils'],
    # Options specifiques à la plateforme
    **options
)
