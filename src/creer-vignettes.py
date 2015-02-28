#!/usr/bin/python2
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

## Import globaux
from os.path import join, dirname
from subprocess import call
## Import locaux
from actimaths.values import DATADIR
from actimaths.system import lire_liste_exercice
from actimaths.exercices import creation

environnement = 'pyromaths'
fichier_liste_exercice = join(DATADIR, 'onglets', environnement,'niveau.xml')
liste_exercice = lire_liste_exercice(fichier_liste_exercice)
parametres = {'sujet_presentation': True,
              'corrige_presentation': False,
              'sujet_page': False,
              'corrige_page': False,
              'titre': 'test',
              'nom_etablissement': 'test',
              'nom_auteur': 'test',
              'temps_slide': '1',
              'date_activite': '1',
              'niveau': 'test',
              'nom_fichier': 'test',
              'chemin_fichier': '/tmp/',
              'environnement': environnement,
              'affichage': 'niveau',
              'modele_presentation': 'Vignette',
              'modele_page': '',
              'creer_pdf': True,
              'effacer_tex': True,
              'afficher_pdf' : False}

for onglet in range(len(liste_exercice)):
    for categorie in range(len(liste_exercice[onglet][1])):
        for exercice in range(len(liste_exercice[onglet][1][categorie][1])):
            valeur_parametre = []
            commande = liste_exercice[onglet][1][categorie][1][exercice][2]
            for parametre in range(len(liste_exercice[onglet][1][categorie][1][exercice][1])):
                valeur_parametre.append(int(liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
            liste = ((commande, valeur_parametre),)
            parametres['liste_exercice'] = liste
            creation(parametres)
            if environnement == 'pyromaths':
                call(["convert", "-density", "288", "/tmp/test-sujet-presentation.pdf", "-alpha", "Opaque", "-resize", "25%", "-crop", "710x560+0+0", "-fuzz" , "1%" ,"-trim", "-resize", "200x70!", "/tmp/%s.jpg" % commande])
            elif environnement == 'actimaths':
                call(["convert", "-density", "288", "/tmp/test-sujet-presentation.pdf[1]", "-alpha", "Opaque", "-resize", "25%", "-crop", "182x210+0+40", "-fuzz" , "1%" ,"-trim", "-resize", "200x70!", "/tmp/%s.jpg" % commande])
