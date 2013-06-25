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
import cinquieme_geometrie_angle
import cinquieme_geometrie_triangle
import cinquieme_gestionDonnee_abscisse
import cinquieme_gestionDonnee_plan
import cinquieme_gestionDonnee_statistique
import cinquieme_grandeurMesure_aire
import cinquieme_grandeurMesure_volume
import cinquieme_nombreCalcul_calcul
import cinquieme_nombreCalcul_developpements
import cinquieme_nombreCalcul_difference
import cinquieme_nombreCalcul_ecrire
import cinquieme_nombreCalcul_egale
import cinquieme_nombreCalcul_numeration
import cinquieme_nombreCalcul_operations
import cinquieme_nombreCalcul_priorites
import cinquieme_nombreCalcul_produit
import cinquieme_nombreCalcul_simplifier
import cinquieme_nombreCalcul_somme
import quatrieme_nombreCalcul_developpements
import quatrieme_nombreCalcul_ecritureScientifique
import quatrieme_nombreCalcul_priorite
import quatrieme_nombreCalcul_puissance
import quatrieme_nombreCalcul_quotient
import quatrieme_nombreCalcul_reduction
import sixieme_geometrie_droiteDemidroiteSegment
import sixieme_gestionDonnee_abscisse
import sixieme_gestionDonnee_pourcentage
import sixieme_gestionDonnee_tableau
import sixieme_grandeurMesure_perimetre
import sixieme_grandeurMesure_aire
import sixieme_grandeurMesure_angle
import sixieme_grandeurMesure_conversion
import sixieme_grandeurMesure_volume
import sixieme_nombreCalcul_arrondi
import sixieme_nombreCalcul_classerNombres
import sixieme_nombreCalcul_complement
import sixieme_nombreCalcul_decomposition
import sixieme_nombreCalcul_ecriture
import sixieme_nombreCalcul_ecritureFractionnaire
import sixieme_nombreCalcul_egale
import sixieme_nombreCalcul_mentale
import sixieme_nombreCalcul_multiple
import sixieme_nombreCalcul_ordreGrandeur
import sixieme_nombreCalcul_placerVirgule
import sixieme_nombreCalcul_pose
import sixieme_nombreCalcul_puissanceDix
import sixieme_nombreCalcul_quantite
import sixieme_nombreCalcul_rang
import troisieme_gestionDonnee_affine
import troisieme_nombreCalcul_developpements
import troisieme_nombreCalcul_factorisations
import troisieme_nombreCalcul_modification
import troisieme_nombreCalcul_operation
import troisieme_nombreCalcul_secondDegre

###==============================================================
### Fonction de création des exercices
###==============================================================
############## Créer, lance la compilation des fichiers TeX et affiche les PDF
def creation(parametres):
    ## Creation de la liste de question, sujet, corrigé
    (question, enonce, correction) = (['',''], ['',''], ['',''])
    for i in range(2):
        if parametres['affichage'] == "csv":
            (question[i], enonce[i], correction[i]) = creation_liste_csv(parametres['chemin_csv'])
        else:
            (question[i], enonce[i], correction[i]) = creation_liste(parametres['liste_exercice'])
    ## Création et affichage de la présentation sujet en PDF
    if parametres['sujet_presentation']:
        generation(parametres, question, enonce, correction, 'sujet','presentation')
    ## Création et affichage de la présentation corrigé en PDF
    if parametres['corrige_presentation']:
        generation(parametres, question, enonce, correction, 'corrige','presentation')
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
    mise_en_forme(cheminTex)
    ## creation du pdf
    creation_pdf(dossierTex, nomTex)
    nettoyage(dossierTex, nomTex)
    if parametres['afficher_pdf']:
        affichage_pdf(dossierTex, nomTex)

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
    longueur_liste_exercice = len(question[0])
    for numero in range(longueur_liste_exercice):
        inverse = longueur_liste_exercice - numero - 1
        texte = [str(numero + 1) , question[0][numero]  , enonce[0][numero] , correction[0][numero],
                 str(inverse + 1), question[0][inverse] , enonce[0][inverse], correction[0][inverse],
                 str(numero + 1) , question[1][numero]  , enonce[1][numero] , correction[1][numero]]
        copie_modele(tex, parametres, fiche, type, 'exercice', texte)
    copie_modele(tex, parametres, fiche, type, 'pied')

############## Supprime les fichiers temporaires créés par LaTeX
def nettoyage(dossier, fichier):
    chdir(dossier)
    for ext in ('.aux', '.dvi', '.out', '.ps','.nav','.snm','.toc'):
        try:
            remove(fichier+ext)
        except OSError:
            pass
            #le fichier à supprimer n'existe pas et on s'en moque.
    if getsize("%s.pdf" % fichier) > 1000 :
        remove("%s.log" % fichier)
        remove("%s-actimaths.log" % fichier)

############## Créé les fichiers PDF
def creation_pdf(dossier, fichier):
    chdir(dossier)
    log = open("%s-actimaths.log" % fichier, 'w')
    for i in range(2):
        call(["latex", "-interaction=batchmode", "%s.tex" % fichier], stdout=log)
    call(["dvips", "-q", "%s.dvi" % fichier, "-o%s.ps" % fichier], stdout=log)
    call(["ps2pdf", "-sPAPERSIZE#a4", "%s.ps" % fichier, "%s.pdf" % fichier], stdout=log)
    log.close()

############## Affiche les fichiers PDF créés par actimaths
def affichage_pdf(dossier, fichier):
    chdir(dossier)
    #Cas de Windows
    if name == "nt":
         os.startfile("%s.pdf" % fichier)
    #Cas de Mac OS X
    elif platform == "darwin":  #Cas de Mac OS X.
         call(["open", "%s.pdf" % fichier])
    #Cas de Linux
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
