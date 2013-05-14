#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup
import glob
from actimaths.values import VERSION, DESCRIPTION, LICENSE, COPYRIGHTS, MAIL, WEBSITE

setup(name = "actimaths",
    version = VERSION,
    description = DESCRIPTION,
    license = LICENSE,
    author = COPYRIGHTS,
    author_email = MAIL,
    url = WEBSITE,
    package_dir={'actimaths':'actimaths'},
    packages=['actimaths','actimaths.exercices' ,'actimaths.outils', 'actimaths.classes' ],
    data_files=[
        ('share/applications', ['data/linux/actimaths.desktop']),
        ('share/actimaths/images', ['data/images/actimaths.ico','data/images/actimaths.png', 'data/images/whatsthis.png']),
        (r'share/actimaths/images/vignettes', glob.glob(r'data/images/vignettes/*.png')),
        (r'share/actimaths/modeles/page/BiColonneIdentique', glob.glob(r'data/modeles/page/BiColonneIdentique/*.tex')),
        (r'share/actimaths/modeles/page/BiColonneInverse', glob.glob(r'data/modeles/page/BiColonneInverse/*.tex')),
        (r'share/actimaths/modeles/page/MonoColonne', glob.glob(r'data/modeles/page/MonoColonne/*.tex')),
        (r'share/actimaths/modeles/page/Test', glob.glob(r'data/modeles/page/Test/*.tex')),
        (r'share/actimaths/modeles/presentation/BiColonneIdentique', glob.glob(r'data/modeles/presentation/BiColonneIdentique/*.tex')),
        (r'share/actimaths/modeles/presentation/BiColonneIdentiqueCompteur', glob.glob(r'data/modeles/presentation/BiColonneIdentiqueCompteur/*.tex')),
        (r'share/actimaths/modeles/presentation/BiColonneInverse', glob.glob(r'data/modeles/presentation/BiColonneInverse/*.tex')),
        (r'share/actimaths/modeles/presentation/BiColonneInverseCompteur', glob.glob(r'data/modeles/presentation/BiColonneInverseCompteur/*.tex')),
        (r'share/actimaths/modeles/presentation/MonoColonne', glob.glob(r'data/modeles/presentation/MonoColonne/*.tex')),
        (r'share/actimaths/modeles/presentation/MonoColonneCompteur', glob.glob(r'data/modeles/presentation/MonoColonneCompteur/*.tex')),
        (r'share/actimaths/onglets', glob.glob(r'data/onglets/*.xml')),
         ],
    scripts = ["actimaths-gui"],
    platforms = ['unix'],
    long_description = DESCRIPTION
    )
