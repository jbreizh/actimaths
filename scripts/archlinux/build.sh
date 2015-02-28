#!/bin/bash
#copie du repertoire source
cp -R ../../src src
#creation du paquet archlinux et nettoyage
makepkg -c
