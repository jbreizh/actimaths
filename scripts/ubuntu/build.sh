#!/bin/bash
#copie du repertoire source
cp -R ../../src src
cp stdeb.cfg src
#creation du paquet
cd src
python2 setup.py --command-packages=stdeb.command bdist_deb
cd ..
#nettoyage
find -name "*.deb"  -print -exec cp {} . \;
rm -R src
