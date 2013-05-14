#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe, glob, os, innosetup
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
    package_dir={'actimaths':'actimaths'},
    packages=['actimaths','actimaths.exercices' ,'actimaths.outils', 'actimaths.classes' ],
    data_files=[
        ('data/images', ['data/images/actimaths.ico','data/images/actimaths.png', 'data/images/whatsthis.png']),
        (r'data/images/vignettes', glob.glob(r'data/images/vignettes/*.png')),
        (r'data/modeles/page/BiColonneIdentique', glob.glob(r'data/modeles/page/BiColonneIdentique/*.tex')),
        (r'data/modeles/page/BiColonneInverse', glob.glob(r'data/modeles/page/BiColonneInverse/*.tex')),
        (r'data/modeles/page/MonoColonne', glob.glob(r'data/modeles/page/MonoColonne/*.tex')),
        (r'data/modeles/page/Test', glob.glob(r'data/modeles/page/Test/*.tex')),
        (r'data/modeles/presentation/BiColonneIdentique', glob.glob(r'data/modeles/presentation/BiColonneIdentique/*.tex')),
        (r'data/modeles/presentation/BiColonneIdentiqueCompteur', glob.glob(r'data/modeles/presentation/BiColonneIdentiqueCompteur/*.tex')),
        (r'data/modeles/presentation/BiColonneInverse', glob.glob(r'data/modeles/presentation/BiColonneInverse/*.tex')),
        (r'data/modeles/presentation/BiColonneInverseCompteur', glob.glob(r'data/modeles/presentation/BiColonneInverseCompteur/*.tex')),
        (r'data/modeles/presentation/MonoColonne', glob.glob(r'data/modeles/presentation/MonoColonne/*.tex')),
        (r'data/modeles/presentation/MonoColonneCompteur', glob.glob(r'data/modeles/presentation/MonoColonneCompteur/*.tex')),
        (r'data/onglets', glob.glob(r'data/onglets/*.xml')),
        ],

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
       'icon_resources': [(1, 'data/images/actimaths.ico')],
       }]
    )
