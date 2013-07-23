#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import py2exe, innosetup
from actimaths.values import VERSION, DESCRIPTION, LICENSE, COPYRIGHTS, MAIL, WEBSITE

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
    package_data={'actimaths': [r'images/*'],
                  'actimaths.exercices_actimaths': [r'modeles/*/*/*', r'onglets/*', r'packages/*', r'vignettes/*'],
                  'actimaths.exercices_pyromaths': [r'modeles/*/*/*', r'onglets/*', r'packages/*', r'vignettes/*']},
    data_files=[(r'data/images', [r'data/images/actimaths.ico'])],   
    platforms = ['windows'],
    options =
    {
        'py2exe':
        {
            "skip_archive": True,
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
       'icon_resources': [(1, 'data/images/actimaths.ico')],
       }]
    )
