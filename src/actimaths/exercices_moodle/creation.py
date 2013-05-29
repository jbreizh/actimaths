#!/usr/bin/python
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

## Import globaux
import os
from os import  chdir, name, remove ,environ
from os.path import join, getsize, normpath, dirname
from sys import platform, exit
from codecs import open
from csv import reader
from re import findall
from subprocess import call

## Import spécifique à Actimaths
import sixieme_grandeurMesure_angles

###==============================================================
### Fonction de création des exercices
###==============================================================
############## Créer fichiers des fichier XML
def creation(parametres):
    ## Creation de la liste de question, sujet, corrigé
    if parametres['affichage'] == "csv":
        (question, enonce, correction) = creation_liste_csv(parametres['chemin_csv'])
    else:
        (question, enonce, correction) = creation_liste(parametres['liste_exercice'])
    ## Création et affichage du sujet en PDF
    if parametres['sujet_page']:
        generation(parametres, question, enonce, correction, 'sujet','page')
    ## Création et affichage du corrigé en PDF
    if parametres['corrige_page']:
        generation(parametres, question, enonce, correction, 'corrige','page')

############## Génère les exercice à partir du CSV
def creation_liste_csv(chemin_csv):
    fichier_csv = open(chemin_csv, "rb")
    tableau_csv = reader(fichier_csv)
    ## creation des exercices
    (enonce_liste, correction_liste, question_liste) = ( [], [], [] )
    for ligne in tableau_csv:
        if ligne[0]:
            enonce_liste.append(ligne[1])
            correction_liste.append(ligne[2])
            question_liste.append(ligne[0])
    fichier_csv.close()
    return  question_liste, enonce_liste, correction_liste

############## Génère les exercice à partir de la liste
def creation_liste(liste_exercice):
    ## creation des exercices
    (enonce_liste, correction_liste, question_liste) = ( [], [], [] )
    for i in range(len(liste_exercice)):
        (commande, parametre) = liste_exercice[i]
        # on génère l'exercice et on recommence en cas de duplication
        repetition = True
        essai = 1
        while repetition:
            if essai == 50:
                print(u"Impossible de générer un exercice unique avec les paramètres donnés")
                exit(0)
            # crétion de l'exercice
            (enonceTemp, correctionTemp, question ) = eval(commande)(parametre)
            (enonce, correction) = ("", "")
            for ligne in enonceTemp:
                enonce = enonce + ligne + "\n"
            for ligne in correctionTemp:
                correction = correction + ligne + "\n"
            # On teste pour voir si on a déjà créé un exercice totalement identique
            repetition = False
            for enonceValide in enonce_liste:
                if enonceValide == enonce:
                    repetition = True
                    break
            essai += 1
        # on range l'exercice dans la liste
        enonce_liste.append(enonce)
        correction_liste.append(correction)
        question_liste.append(question)
    return  question_liste, enonce_liste, correction_liste

############## Generation complete
def generation(parametres, question, enonce, correction, fiche, type):
    ## Dossiers et fichiers d'enregistrement
    dossierTex = unicode(parametres['chemin_fichier'])
    nomTex= u"%s-%s-%s" % (parametres['nom_fichier'],fiche, type)
    cheminTex = unicode(join(dossierTex, "%s.tex" % nomTex))
    ## Ouverture du fichier teX
    tex = open(cheminTex, encoding='utf-8', mode='w')
    ## creation du fichier teX
    creation_latex(tex, parametres, question, enonce, correction, fiche, type)
    ## fermeture du fichier teX
    tex.close()
    ## indentation des fichiers teX créés
    #mise_en_forme(cheminTex)


############## Copie des modèles latex en remplacant certaines variables
def copie_modele(tex, parametres, fiche, type, master, texte=''):
    ## chemin du modele
    source = join(dirname(__file__), 'modeles', type, parametres['modele_%s' % type] , fiche + '_' + master  + '.tex' )
    ## Les variables à remplacer :
    titre = parametres['titre']
    niveau = parametres['niveau']
    etablissement = parametres['nom_etablissement']
    auteur = parametres['nom_auteur']
    tempsslide = parametres['temps_slide']
    tempscompteur = str(float(parametres['temps_slide'])/3)
    dateactivite = parametres['date_activite']
    if name == 'nt':
        environ['TEXINPUTS']= normpath(join(dirname(__file__),'packages'))
        tabvar = 'tabvar.tex'
    else:
        tabvar = normpath(join(dirname(__file__), 'packages', 'tabvar.tex'))
    ## Remplacement des variables et copie dans le fichier latex
    modele = open(source, encoding='utf-8', mode='r')
    for ligne in modele:
        # Substitution des variables
        variableSubstituableListe = findall('##{{[A-Z]*}}##',ligne)
        if variableSubstituableListe:
            for variableSubstituable in variableSubstituableListe:
                occ = variableSubstituable[ 4 : len(variableSubstituable)- 4 ].lower()
                ligne = ligne.replace(variableSubstituable, eval(occ))
        # Substitution du texte
        texteSubstituableListe = findall('##{{[0-9]*}}##',ligne)
        if texteSubstituableListe:
            for texteSubstituable in texteSubstituableListe:
                occ = texteSubstituable[ 4 : len(texteSubstituable)- 4 ]
                ligne = ligne.replace(texteSubstituable, texte[int(occ)])
        tex.write(ligne)
    modele.close()

############## Génère le code latex
def creation_latex(tex, parametres, question, enonce, correction, fiche, type):
    copie_modele(tex, parametres, fiche, type, 'entete')
    for numero in range(len(question)):
        texte = [str(numero + 1) , question[numero]  , enonce[numero] , correction[numero]]
        copie_modele(tex, parametres, fiche, type, 'exercice', texte)
    copie_modele(tex, parametres, fiche, type, 'pied')

###==============================================================
### Fonction de mise en forme des fichier xml
###==============================================================
############## Indente correctement les fichiers xml. By Filip Salomonsson; published on February 06, 2007.  http://infix.se/2007/02/06/gentlemen-indent-your-xml
