#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
from actimaths.values import VERSION, DESCRIPTION, LICENSE, COPYRIGHTS, MAIL, WEBSITE

setup(name = "actimaths",
    version = VERSION,
    description = DESCRIPTION,
    license = LICENSE,
    author = COPYRIGHTS,
    author_email = MAIL,
    url = WEBSITE,
    package_dir={'actimaths':'src/actimaths'},
    packages=[   'actimaths',
                 'actimaths.exercices_actimaths','actimaths.exercices_actimaths.outils','actimaths.exercices_actimaths.classes',
                 'actimaths.exercices_pyromaths','actimaths.exercices_pyromaths.outils','actimaths.exercices_pyromaths.classes'],
    data_files=[ (r'share/applications', [r'data/linux/actimaths.desktop']),
                 (r'share/actimaths/images', [r'data/images/actimaths.ico',r'data/images/actimaths.png', r'data/images/whatsthis.png']),
                 (r'share/actimaths/images/vignettes', glob.glob(r'data/images/vignettes/*.png')),
                 (r'share/actimaths/packages', glob.glob(r'data/packages/*')),  
                 (r'share/actimaths/actimaths/modeles/page/BiColonneIdentique', glob.glob(r'data/actimaths/modeles/page/BiColonneIdentique/*.tex')),
                 (r'share/actimaths/actimaths/modeles/page/BiColonneInverse', glob.glob(r'data/actimaths/modeles/page/BiColonneInverse/*.tex')),
                 (r'share/actimaths/actimaths/modeles/page/MonoColonne', glob.glob(r'data/actimaths/modeles/page/MonoColonne/*.tex')),
                 (r'share/actimaths/actimaths/modeles/page/Test', glob.glob(r'data/actimaths/modeles/page/Test/*.tex')),
                 (r'share/actimaths/actimaths/modeles/presentation/BiColonneIdentique', glob.glob(r'data/actimaths/modeles/presentation/BiColonneIdentique/*.tex')),
                 (r'share/actimaths/actimaths/modeles/presentation/BiColonneIdentiqueCompteur', glob.glob(r'data/actimaths/modeles/presentation/BiColonneIdentiqueCompteur/*.tex')),
                 (r'share/actimaths/actimaths/modeles/presentation/BiColonneInverse', glob.glob(r'data/actimaths/modeles/presentation/BiColonneInverse/*.tex')),
                 (r'share/actimaths/actimaths/modeles/presentation/BiColonneInverseCompteur', glob.glob(r'data/actimaths/modeles/presentation/BiColonneInverseCompteur/*.tex')),
                 (r'share/actimaths/actimaths/modeles/presentation/MonoColonne', glob.glob(r'data/actimaths/modeles/presentation/MonoColonne/*.tex')),
                 (r'share/actimaths/actimaths/modeles/presentation/MonoColonneCompteur', glob.glob(r'data/actimaths/modeles/presentation/MonoColonneCompteur/*.tex')),
                 (r'share/actimaths/actimaths/onglets', glob.glob(r'data/actimaths/onglets/*.xml')),
                 (r'share/actimaths/pyromaths/modeles/page/TriColonne', glob.glob(r'data/pyromaths/modeles/page/TriColonne/*.tex')),
                 (r'share/actimaths/pyromaths/modeles/page/BiColonne', glob.glob(r'data/pyromaths/modeles/page/BiColonne/*.tex')),
                 (r'share/actimaths/pyromaths/modeles/page/MonoColonne', glob.glob(r'data/pyromaths/modeles/page/MonoColonne/*.tex')),
                 (r'share/actimaths/pyromaths/modeles/presentation/Vignette',glob.glob(r'data/pyromaths/modeles/presentation/Vignette/*.tex')),
                 (r'share/actimaths/pyromaths/onglets', glob.glob(r'data/pyromaths/onglets/*.xml'))],
    scripts = ["actimaths-gui"],
    platforms = ['unix'],
    long_description = DESCRIPTION
    )
