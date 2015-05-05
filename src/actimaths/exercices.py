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
#

## Import globaux
import os
from os import  chdir, name, remove ,environ, listdir
from os.path import join, getsize, normpath, dirname
from sys import platform, exit
from codecs import open
from csv import reader
from re import findall
from subprocess import call

## Import locaux
from values import DATADIR
import exercices_actimaths
import exercices_pyromaths

###==============================================================
### Fonction de création des exercices
###==============================================================
############## Créer, lance la compilation des fichiers TeX et affiche les PDF
def creation(parametres):
    ## Creation de la liste de question, sujet, corrigé
    (temps, question, enonce, correction) = (['',''], ['',''], ['',''], ['',''])
    for i in range(2):
        if parametres['affichage'] == "csv":
            (temps[i], question[i], enonce[i], correction[i]) = creation_liste_csv(parametres['chemin_csv'])
        else:
            (temps[i], question[i], enonce[i], correction[i]) = creation_liste(parametres['liste_exercice'],parametres['environnement'])
    ## Création et affichage de la présentation sujet en PDF
    if parametres['sujet_presentation']:
        generation(parametres, temps, question, enonce, correction, 'sujet','presentation')
    ## Création et affichage de la présentation corrigé en PDF
    if parametres['corrige_presentation']:
        generation(parametres, temps, question, enonce, correction, 'corrige','presentation')
    ## Création et affichage du sujet papier en PDF
    if parametres['sujet_page']:
        generation(parametres, temps, question, enonce, correction, 'sujet','page')
    ## Création et affichage du corrigé papier en PDF
    if parametres['corrige_page']:
        generation(parametres, temps, question, enonce, correction, 'corrige','page')

############## Génère les exercice à partir du CSV
def creation_liste_csv(chemin_csv):
    ## Ouverture du fichier CSV
    fichier_csv = open(chemin_csv, "rb")
    tableau_csv = reader(fichier_csv)
    ## creation des exercices
    (temps_liste, question_liste, enonce_liste, correction_liste) = ( [], [], [], [] )
    for ligne in tableau_csv:
        if ligne[0]:
            temps_liste.append(ligne[0])
            question_liste.append(ligne[1])
            enonce_liste.append(ligne[2])
            correction_liste.append(ligne[3])
    fichier_csv.close()
    return  temps_liste, question_liste, enonce_liste, correction_liste

############## Génère les exercice à partir de la liste
def creation_liste(liste_exercice,environnement):
    ## creation des exercices
    (temps_liste, question_liste, enonce_liste, correction_liste) = ( [], [], [], [] )
    for i in range(len(liste_exercice)):
        (temps, commande, parametre) = liste_exercice[i]
        # on génère l'exercice et on recommence en cas de duplication
        repetition = True
        essai = 1
        while repetition:
            # On incrémente le nombre d'essai
            essai += 1
            repetition = False
            # crétion de l'exercice
            (enonceTemp, correctionTemp, question ) = eval("exercices_%s.%s" %(environnement,commande))(parametre)
            (enonce, correction) = ("", "")
            for ligne in enonceTemp:
                enonce = enonce + ligne + "\n"
            for ligne in correctionTemp:
                correction = correction + ligne + "\n"
            # On teste pour voir si on a déjà créé un exercice totalement identique
            for enonceValide in enonce_liste:
                if enonceValide == enonce:
                    repetition = True
                    break
            # Au bout de 50 essai on considère qu'il est impossible de créer un nouvel exercice différent
            if essai == 50:
                question = "Erreur :"
                enonce = u"Impossible de générer un nouvel exercice différent avec les paramètres donnés"
                correction = u"Impossible de générer un nouvel exercice différent avec les paramètres donnés"
                break
        # on range l'exercice dans la liste
        temps_liste.append(temps)
        question_liste.append(question)
        enonce_liste.append(enonce)
        correction_liste.append(correction)
    return  temps_liste, question_liste, enonce_liste, correction_liste

############## Generation complete
def generation(parametres, temps, question, enonce, correction, fiche, type):
    ## Dossiers et fichiers d'enregistrement
    dossierTex = unicode(parametres['chemin_fichier'])
    nomTex= u"%s-%s-%s" % (parametres['nom_fichier'],fiche, type)
    cheminTex = unicode(join(dossierTex, "%s.tex" % nomTex))
    ## Ouverture du fichier teX
    tex = open(cheminTex, encoding='utf-8', mode='w')
    ## creation du fichier teX
    creation_latex(tex, parametres, temps, question, enonce, correction, fiche, type)
    ## fermeture du fichier teX
    tex.close()
    ## indentation des fichiers teX créés
    mise_en_forme(cheminTex)
    ## creation du pdf
    if parametres['creer_pdf']:
        creation_pdf(dossierTex, nomTex)
        nettoyage(dossierTex, nomTex, parametres['effacer_tex'])
        # affichage du pdf
        if parametres['afficher_pdf']:
            affichage_pdf(dossierTex, nomTex)

############## Copie des modèles latex en remplacant certaines variables
def copie_modele(tex, parametres, type, master, texte_original='', texte_identique='', texte_inverse=''):
    ## Les variables à remplacer :
    titre = parametres['titre']
    niveau = parametres['niveau']
    etablissement = parametres['nom_etablissement']
    auteur = parametres['nom_auteur']
    dateactivite = parametres['date_activite']
    ## ouverture du modele
    source = join(DATADIR, 'modeles', parametres['environnement'],type, parametres['modele_%s' % type] + '.tex' )
    modele = open(source, encoding='utf-8', mode='r')
    ## Remplacement des variables et copie dans le fichier latex
    master_debut = '% ' + master
    master_fin = '% fin ' + master
    n = 0
    for ligne in modele:
        # On arrete la copie
        if master_fin in ligne:
            break
        # On copie
        if n > 0:
            # Substitution des variables
            variableSubstituableListe = findall('##{{[A-Z]*}}##',ligne)
            if variableSubstituableListe:
                for variableSubstituable in variableSubstituableListe:
                    occ = variableSubstituable[ 4 : len(variableSubstituable)- 4 ].lower()
                    ligne = ligne.replace(variableSubstituable, eval(occ))
            # Substitution du texte original
            texteSubstituableListe = findall('##{{ORIGINAL[0-9]*}}##',ligne)
            if texteSubstituableListe:
                for texteSubstituable in texteSubstituableListe:
                    occ = texteSubstituable[ 12 : len(texteSubstituable)- 4 ]
                    ligne = ligne.replace(texteSubstituable, texte_original[int(occ)])
            # Substitution du texte identique
            texteSubstituableListe = findall('##{{IDENTIQUE[0-9]*}}##',ligne)
            if texteSubstituableListe:
                for texteSubstituable in texteSubstituableListe:
                    occ = texteSubstituable[ 13 : len(texteSubstituable)- 4 ]
                    ligne = ligne.replace(texteSubstituable, texte_identique[int(occ)])
            # Substitution du texte inverse
            texteSubstituableListe = findall('##{{INVERSE[0-9]*}}##',ligne)
            if texteSubstituableListe:
                for texteSubstituable in texteSubstituableListe:
                    occ = texteSubstituable[ 11 : len(texteSubstituable)- 4 ]
                    ligne = ligne.replace(texteSubstituable, texte_inverse[int(occ)])
            # ecriture de la ligne
            tex.write(ligne)
        # On peut débuter la copie
        if master_debut in ligne:
            n = 1
    modele.close()

############## Génère le code latex
def creation_latex(tex, parametres, temps, question, enonce, correction, fiche, type):
    ## Copie de l'entête
    copie_modele(tex, parametres, type, 'entete')
    longueur_liste_exercice = len(question[0])
    ## Copie du corps
    for numero in range(longueur_liste_exercice):
        # Enoncé des exercices pour la substitution (original, inverse et indentique)
        inverse = longueur_liste_exercice - numero - 1
        texte_original = [question[0][numero] , enonce[0][numero] , correction[0][numero] , str(numero + 1) , str(temps[0][numero]) , str(float(temps[0][numero])/3) , str(50/float(temps[0][numero])) ]
        texte_identique = [question[1][numero], enonce[1][numero] , correction[1][numero] , str(numero + 1) , str(temps[0][numero]) , str(float(temps[0][numero])/3) , str(50/float(temps[0][numero])) ]
        texte_inverse = [question[0][inverse] , enonce[0][inverse], correction[0][inverse], str(inverse + 1), str(temps[0][inverse]), str(float(temps[0][inverse])/3), str(50/float(temps[0][inverse]))]
        # Copie de l'exercice
        copie_modele(tex, parametres, type, fiche, texte_original, texte_identique, texte_inverse)
    ## Copie du pied
    copie_modele(tex, parametres, type, 'pied')

############## Créé les fichiers PDF
def creation_pdf(dossier, fichier):
    ## Import des packages locaux
    ligne = ""
    for package in listdir(join(DATADIR, 'packages')):
        ligne += normpath(join(DATADIR, 'packages', package))
        ligne += ';'
    environ['TEXINPUTS']= ligne
    ## Changement de dossier
    chdir(dossier)
    ## Compilation latex(x2)+dvips+ps2pdf
    for i in range(2):
        call(["latex", "-interaction=batchmode", "%s.tex" % fichier])
    call(["dvips", "-q", "%s.dvi" % fichier, "-o%s.ps" % fichier])
    call(["ps2pdf", "-sPAPERSIZE#a4", "%s.ps" % fichier, "%s.pdf" % fichier])

############## Supprime les fichiers temporaires créés par la compilation
def nettoyage(dossier, fichier, effacer_tex):
    ## Changement de dossier
    chdir(dossier)
    ## Liste des extensions à supprimer
    extensions = ['.aux','.dvi','.out','.ps','.nav','.snm','.toc','.log']
    if effacer_tex:
        extensions.append('.tex')
    ## Suppression des fichiers
    for extension in extensions:
        try:
            remove(fichier+extension)
        except OSError:
            pass
            #le fichier à supprimer n'existe pas et on s'en moque.

############## Affiche les fichiers PDF créés par actimaths
def affichage_pdf(dossier, fichier):
    chdir(dossier)
    ## Cas de Windows
    if name == "nt":
         os.startfile("%s.pdf" % fichier)
    ## Cas de Mac OS X
    elif platform == "darwin":
         call(["open", "%s.pdf" % fichier])
    ## Cas de Linux
    else:
         call(["xdg-open", "%s.pdf" % fichier])

###==============================================================
### Fonction de mise en forme des fichier latex
###==============================================================
############## 
def mise_en_forme(file):
    """
    \begin => +2 espaces si pas \begin{document}
    \item => +2 espaces après sauf si c'est \item
    \end => -2 espaces avant sauf si \end{document}
    Si longueur de ligne >80, retour ligne au dernier espace précédent et
        indentation de la ligne suivante.
    Couper la ligne après un \\begin{}[]{} ou un \\end{}
    lline : last line
    cline : current line
    """
    f = open(file, encoding='utf-8', mode='r')
    old_tex = f.readlines()
    new_tex=[]
    indent = 0
    item = False
    for cline in old_tex:
        if new_tex:
            lline = new_tex[-1]
        else:
            lline = ""
        cline = cline.strip()
        indent = trouve_indentation(cline, indent, lline)
        if indent < 0:
            print "problème"
        if cline:
            chaine, indent = traite_chaine(cline, indent)
            new_tex.extend(chaine)
        else:
            new_tex.append("")
    f.close()
    f = open(file, encoding='utf-8', mode='w')
    f.write("\n".join(new_tex))
    f.close()

############## Trouve l'indentation
def trouve_indentation(cline, indent, lline):
    if lline.find(r"\begin{")>=0:
        # indente tout ce qui suit \begin{...}
        indent += 2
    if cline.find(r"\end{")==0:
        # desindente tout ce qui suit \end{...}
        indent -= 2
    if cline.find(r"\item") == 0 :
        indent -= 2
    if lline.find(r"\item") >= 0:
        indent += 2
    indent += compte_paires_ouvertes(lline)
    return indent

############## indente la chaine txt en fonction du paramètre indent
def traite_chaine(cline,  indent):
    list = []
    cline = " "*indent + cline
    list.append(cline)
    while len(list[-1]) > 80:
        if list[-1].rfind(" ", indent + 1, 80) > 0:
            for i in range(79, indent, -1):
                if list[-1][i] == " ":
                    list.append(list[-1][:i])
                    indent = trouve_indentation(list[-2][i+1:], indent, list[-1])
                    list.append(" "*indent + list[-2][i+1:])
                    list.pop(-3)
                    break
        else:
            break
    return list, indent

############## Trouve le caractère fermant pour les symboles {, [, ( qui est le 1er caractère de txt
def trouve_paire(txt):
    ouvrant = ["{", "[", "("]
    fermant = ["}", "]", ")"]
    index = ouvrant.index(txt[0])
    compte = 0
    for i in range(len(txt)):
        if txt[i] == ouvrant[index]:
            compte += 1
        elif txt[i] == fermant[index]:
            compte -= 1
        if compte == 0:
            return i
    return None

############## Compte le nombres de paires {...}, \[...\] qui ne sont pas fermées dans la string txt
def compte_paires_ouvertes(txt):
    diff = 0
    for i in ["{", r"\["]:
        diff += txt.count(i)
    for i in ["}", r"\]"]:
        diff -= txt.count(i)
    return 2*diff
