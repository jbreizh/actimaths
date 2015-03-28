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

############## Creation du menu
def creation_menu(liste_exercice):
    html = ""
    ## Creation du formulaire d'exercices
    for onglet in range(len(liste_exercice)):
        html += u"Niveau = \"%s\" \n""" % liste_exercice[onglet][0]
        # Construction du contenu des onglets
        for categorie in range(len(liste_exercice[onglet][1])):
            html += u"    Domaine = \"%s\" \n" % liste_exercice[onglet][1][categorie][0]
            # Construction de la ligne correspondant à un exercice
            for exercice in range(len(liste_exercice[onglet][1][categorie][1])):
                html += u"Commande = \"%s\" \n" % liste_exercice[onglet][1][categorie][1][exercice][2]
    print html.encode('utf-8')

############## Creation des exercices
def creation_exercice(environnement,commande,valeur_parametre):
    ## Creation de parametre
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
                  'modele_presentation': 'vignette',
                  'modele_page': '',
                  'creer_pdf': True,
                  'effacer_tex': True,
                  'afficher_pdf' : False}
    parametres['liste_exercice'] = [(10, commande, valeur_parametre)]
    ## Creation des exercices
    creation(parametres)

def creation_vignette(environnement,commande):
    ## Creation de parametre
    if environnement == 'pyromaths':
        call(["convert", "-density", "288", "/tmp/test-sujet-presentation.pdf", "-alpha", "Opaque", "-resize", "25%", "-crop", "710x560+0+0", "-fuzz" , "1%" ,"-trim", "-resize", "200x70!", "/tmp/%s.jpg" % commande])
    elif environnement == 'actimaths':
        call(["convert", "-density", "288", "/tmp/test-sujet-presentation.pdf", "-alpha", "Opaque", "-resize", "25%", "-crop", "182x210+0+40", "-fuzz" , "1%" ,"-trim", "-resize", "200x70!", "/tmp/%s.jpg" % commande])

###==============================================================
###                            Main
###==============================================================
def main():
    #choix de l'environnement
    choix_environnement = raw_input("Choisir l'environnement : [1]Actimaths [2]Pyromaths ?")
    if choix_environnement == "1":
        environnement = 'actimaths'
    else:
        environnement = 'pyromaths'
    #creation de variable
    liste_exercice = lire_liste_exercice(join(DATADIR, 'onglets', environnement,'niveau.xml'))
    #choix de l'action
    choix_action = raw_input("Creer la vignette de : [1]Un exercice [2]Tous les exercices ?")
    if choix_action == "1":
        creation_menu(liste_exercice)
        choix_commande = raw_input("Entrez la commande de l\'exercice : ")

    for onglet in range(len(liste_exercice)):
        for categorie in range(len(liste_exercice[onglet][1])):
            for exercice in range(len(liste_exercice[onglet][1][categorie][1])):
                commande = liste_exercice[onglet][1][categorie][1][exercice][2]
                valeur_parametre = []
                for parametre in range(len(liste_exercice[onglet][1][categorie][1][exercice][1])):
                    valeur_parametre.append(int(liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
                if choix_action == "2":
                    choix_commande = commande

                if commande == choix_commande:
                    creation_exercice(environnement,commande,valeur_parametre)
                    creation_vignette(environnement,commande)

if __name__ == "__main__":
    main()

