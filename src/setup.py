#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from actimaths.values import VERSION, DESCRIPTION, LICENSE, COPYRIGHTS, MAIL, WEBSITE

setup(name = "actimaths",
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
    data_files=[(r'share/applications', [r'data/linux/actimaths.desktop']),
                (r'share/actimaths/images', [r'data/images/actimaths.png'])],     
    scripts = ["actimaths-gui"],
    platforms = ['unix'],
    long_description = DESCRIPTION
    )
