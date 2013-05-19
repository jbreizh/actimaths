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
    packages=['actimaths','actimaths.exercices_actimaths','actimaths.exercices_actimaths.outils','actimaths.exercices_actimaths.classes','actimaths.exercices_pyromaths','actimaths.exercices_pyromaths.outils','actimaths.exercices_pyromaths.classes'],
    data_files=[
        (r'data/images', [r'data/images/actimaths.ico',r'data/images/actimaths.png', r'data/images/whatsthis.png']),
        (r'data/images/vignettes', glob.glob(r'data/images/vignettes/*.png')),
        (r'data/packages', glob.glob(r'data/packages/*')),  
        (r'data/actimaths/modeles/page/BiColonneIdentique', glob.glob(r'data/actimaths/modeles/page/BiColonneIdentique/*.tex')),
        (r'data/actimaths/modeles/page/BiColonneInverse', glob.glob(r'data/actimaths/modeles/page/BiColonneInverse/*.tex')),
        (r'data/actimaths/modeles/page/MonoColonne', glob.glob(r'data/actimaths/modeles/page/MonoColonne/*.tex')),
        (r'data/actimaths/modeles/page/Test', glob.glob(r'data/actimaths/modeles/page/Test/*.tex')),
        (r'data/actimaths/modeles/presentation/BiColonneIdentique', glob.glob(r'data/actimaths/modeles/presentation/BiColonneIdentique/*.tex')),
        (r'data/actimaths/modeles/presentation/BiColonneIdentiqueCompteur', glob.glob(r'data/actimaths/modeles/presentation/BiColonneIdentiqueCompteur/*.tex')),
        (r'data/actimaths/modeles/presentation/BiColonneInverse', glob.glob(r'data/actimaths/modeles/presentation/BiColonneInverse/*.tex')),
        (r'data/actimaths/modeles/presentation/BiColonneInverseCompteur', glob.glob(r'data/actimaths/modeles/presentation/BiColonneInverseCompteur/*.tex')),
        (r'data/actimaths/modeles/presentation/MonoColonne', glob.glob(r'data/actimaths/modeles/presentation/MonoColonne/*.tex')),
        (r'data/actimaths/modeles/presentation/MonoColonneCompteur', glob.glob(r'data/actimaths/modeles/presentation/MonoColonneCompteur/*.tex')),
        (r'data/pyromaths/modeles/page/TriColonne', glob.glob(r'data/pyromaths/modeles/page/TriColonne/*.tex')),
        (r'data/pyromaths/modeles/page/BiColonne', glob.glob(r'data/pyromaths/modeles/page/BiColonne/*.tex')),
        (r'data/pyromaths/modeles/page/MonoColonne', glob.glob(r'data/pyromaths/modeles/page/MonoColonne/*.tex')),
        (r'data/pyromaths/modeles/presentation/Vignette',glob.glob(r'data/pyromaths/modeles/presentation/Vignette/*.tex')),
        (r'data/pyromaths/onglets', glob.glob(r'data/pyromaths/onglets/*.xml')),
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
