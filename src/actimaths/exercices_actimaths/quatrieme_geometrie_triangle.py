#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Pyromaths
# Un programme en Python qui permet de créer des fiches d'exercices types de
# mathématiques niveau collège ainsi que leur corrigé en LaTeX.
# Copyright (C) 2006 -- Jérôme Ortais (jerome.ortais@pyromaths.org)
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

import random
from outils.Geometrie import trouve_couples_pythagore, choix_points
from outils.Arithmetique import liste_combinaison


#------------------methode---------------------------------------------
def tex_figure(enonce,nom_point,mesure_cote):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-3,-3)(3.5,3)')
    enonce.append("\\pstTriangle[PointName=none,SegmentSymbolA=\"rt\"](-2,-2){%s}(-2,2){%s}(3,-2){%s}" %(nom_point[0],nom_point[1],nom_point[2]))
    enonce.append("\\pstRightAngle{%s}{%s}{%s}" %(nom_point[1],nom_point[0],nom_point[2]))
    enonce.append("\\rput[t]{%s}(%s,%s){$%s$}" % (90,-2.8,0,mesure_cote[0]))
    enonce.append("\\rput[t]{%s}(%s,%s){$%s$}" % (0,0.5,-2.3,mesure_cote[1]))
    enonce.append("\\rput[t]{%s}(%s,%s){$%s$}" % (-40,1,0.7,mesure_cote[2]))
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def PythagoreTexte(parametre):
    ## ---Initialisation---
    question = u"Calculer la mesure du 3\\up{eme} côté :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    #nom
    nom_sommet = choix_points(3)
    duo_sommet = liste_combinaison(nom_sommet, 2)
    #mesure
    couples_pythagore = trouve_couples_pythagore(parametre[0])
    mesure_corrige = couples_pythagore[random.randrange(len(couples_pythagore))]
    choix = random.randrange(3)
    mesure_sujet = []
    for i in range(len(mesure_corrige)):
        if i == choix:
            mesure_sujet.append("\\ldots")
        else:
            mesure_sujet.append(mesure_corrige[i])
    ## ---Redaction---
    exo.append("%s%s%s est un triangle rectangle \\newline" %(nom_sommet[0],nom_sommet[1],nom_sommet[2]))
    cor.append("%s%s%s est un triangle rectangle \\newline" %(nom_sommet[0],nom_sommet[1],nom_sommet[2]))
    exo.append(u"Son hypoténuse est [%s%s] \\newline" %(duo_sommet[2][0],duo_sommet[2][1]))
    cor.append(u"Son hypoténuse est [%s%s] \\newline" %(duo_sommet[2][0],duo_sommet[2][1]))
    exo.append("On sait que :")
    cor.append("On sait que :")
    exo.append("\\begin{itemize}")
    cor.append("\\begin{itemize}")
    for i in range(len(duo_sommet)):
        exo.append("\\item $%s%s=\\unit{%s}{cm}$" % (duo_sommet[i][0],duo_sommet[i][1],mesure_sujet[i]))
        if i == choix:
            cor.append("\\item $%s%s=\\boxed{\\unit{%s}{cm}}$" % (duo_sommet[i][0],duo_sommet[i][1],mesure_corrige[i]))
        else:
            cor.append("\\item $%s%s=\\unit{%s}{cm}$" % (duo_sommet[i][0],duo_sommet[i][1],mesure_corrige[i]))
    exo.append("\\end{itemize}")
    cor.append("\\end{itemize}")
    return (exo, cor, question)

def PythagoreSchema(parametre):
    ## ---Initialisation---
    question = u"Calculer la mesure du 3\\up{eme} côté :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    #nom
    nom_sommet = choix_points(3)
    #mesure
    couples_pythagore = trouve_couples_pythagore(parametre[0])
    choix = random.randrange(3)
    mesure_temp = couples_pythagore[random.randrange(len(couples_pythagore))]
    mesure_sujet = []
    mesure_corrige = []
    for i in range(len(mesure_temp)):
        if i == choix:
            mesure_sujet.append("\\unit{\\ldots}{cm}")
            mesure_corrige.append("\\boxed{\\unit{%s}{cm}}" %mesure_temp[i])
        else:
            mesure_sujet.append("\\unit{%s}{cm}" %mesure_temp[i])
            mesure_corrige.append("\\unit{%s}{cm}" %mesure_temp[i])
    ## ---Redaction---
    tex_figure(exo,nom_sommet,mesure_sujet)
    tex_figure(cor,nom_sommet,mesure_corrige)
    return (exo, cor, question)

#------------------methode---------------------------------------------
def caracteristique_sommet():
    ## Nom des sommets
    choix = random.randrange(3)
    if choix == 0:
        nom = ["A","B","C"]
    elif choix == 1:
        nom = ["C","A","B"]
    else:
        nom = ["B","C","A"]
    ## coordonnées des sommets
    coordonnee = (random.uniform(-2,2),random.uniform(2,4),random.uniform(-4,-2),random.uniform(-4,-2),random.uniform(2,4),random.uniform(-4,-2))
    return (nom,coordonnee)

def caracteristique_cote(longueur_min,longueur_max):
    ## Codage
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    ## longueur des cotés
    demi_cote = random.randrange(longueur_min,longueur_max)
    if random.randrange(2):
        mesure_sujet = ["$\\unit{%s}{cm}$" %(2*demi_cote),"$\\unit{\\ldots}{cm}$"]
        mesure_corrige = ["$\\unit{%s}{cm}$" %(2*demi_cote),"$\\boxed{\\unit{%s}{cm}}$" %demi_cote]
    else:
        mesure_sujet = ["$\\unit{\\ldots}{cm}$","$\\unit{%s}{cm}$" %demi_cote]
        mesure_corrige = ["$\\boxed{\\unit{%s}{cm}}$" %(2*demi_cote),"$\\unit{%s}{cm}$" %demi_cote]
    return (codage,mesure_sujet,mesure_corrige)

def tex_figure_droite_milieu(enonce,nom,coordonnee,codage,mesure):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-5,-5)(5,5)')
    enonce.append("\\pstGeonode[PointName=none](%s,%s){%s}(%s,%s){%s}(%s,%s){%s}" %(coordonnee[0],coordonnee[1],nom[0],coordonnee[2],coordonnee[3],nom[1],coordonnee[4],coordonnee[5],nom[2]))
    enonce.append("\\pstMiddleAB[PointName=none]{A}{B}{E}")
    enonce.append("\\pstMiddleAB[PointName=none]{A}{C}{F}")
    enonce.append("\\pstLineAB{A}{B}")
    enonce.append("\\pstLineAB{A}{C}")
    enonce.append("\\pstLineAB{B}{C}")
    enonce.append("\\pstLineAB{E}{F}")
    enonce.append("\\pstSegmentMark[%s]{A}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{A}{F}" %codage[1])
    enonce.append("\\pstSegmentMark[%s]{F}{C}" %codage[1])
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{B}{C} \\mput*{%s}" %mesure[0])
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{E}{F} \\mput*{%s}" %mesure[1])
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def DroiteMilieu(parametre):
    ## ---Initialisation---
    question = u"Calcul la mesure demandée :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    (nom_sommet,coordonnee_sommet) = caracteristique_sommet()
    (codage_cote,mesure_cote_sujet,mesure_cote_corrige) = caracteristique_cote(parametre[0],parametre[1])
    ## ---Redaction---
    tex_figure_droite_milieu(exo,nom_sommet,coordonnee_sommet,codage_cote,mesure_cote_sujet)
    tex_figure_droite_milieu(cor,nom_sommet,coordonnee_sommet,codage_cote,mesure_cote_corrige)
    cor.append(u"On utilise la \\textbf{Propriété des Milieux}")
    return (exo, cor, question)

#------------------methode---------------------------------------------
def caracteristique_sommet_droite_particuliere():
    ## Nom des sommets
    i = random.randrange(3)
    if i == 0:
        nom = ["A","B","C"]
    elif i == 1:
        nom = ["C","A","B"]
    else:
        nom = ["B","C","A"]
    ## coordonnées des sommets
    coordonnee = (random.uniform(-2,2),random.uniform(2,4),random.uniform(-4,-2),random.uniform(-4,-2),random.uniform(2,4),random.uniform(-4,-2))
    ## Choix du sommet
    j = random.randrange(3)
    if j == 0:
        choix = [0,1,2]
    elif j == 1:
        choix = [1,2,0]
    else:
        choix = [2,0,1]
    return (choix, nom,coordonnee)


def tex_figure_droite_particuliere(enonce,nom,coordonnee,choix_sommet,choix_droite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-5,-5)(5,5)')
    enonce.append("\\pstTriangle[PointSymbol=none](%s,%s){%s}(%s,%s){%s}(%s,%s){%s}" %(coordonnee[0],coordonnee[1],nom[0],coordonnee[2],coordonnee[3],nom[1],coordonnee[4],coordonnee[5],nom[2]))
    if choix_droite == 0:
        enonce.append("\\pstProjection[PointName=none,PointSymbol=none]{%s}{%s}{%s}[H]" %(nom[choix_sommet[1]],nom[choix_sommet[2]],nom[choix_sommet[0]]))
        enonce.append("\\pstLineAB[linecolor=red]{%s}{H}" %nom[choix_sommet[0]])
        enonce.append("\\pstRightAngle{%s}{H}{%s}" %(nom[choix_sommet[0]],nom[choix_sommet[1]]))
    if choix_droite == 1:
        enonce.append("\\pstMiddleAB[PointName=none,PointSymbol=none]{%s}{%s}{H}" %(nom[choix_sommet[1]],nom[choix_sommet[2]]))
        enonce.append("\\pstLineAB[linecolor=red]{%s}{H}" %nom[choix_sommet[0]])
        enonce.append("\\pstSegmentMark[SegmentSymbol=pstslash]{%s}{H}" %nom[choix_sommet[1]])
        enonce.append("\\pstSegmentMark[SegmentSymbol=pstslash]{H}{%s}" %nom[choix_sommet[2]])
    if choix_droite == 2:
        enonce.append("\\pstBissectBAC[PointName=none,PointSymbol=none,linecolor=red]{%s}{%s}{%s}{H}" %(nom[choix_sommet[1]],nom[choix_sommet[0]],nom[choix_sommet[2]]))
        enonce.append("\\pstMarkAngle[MarkAngleRadius=1.5,Mark=MarkHash]{%s}{%s}{H}{}" %(nom[choix_sommet[1]],nom[choix_sommet[0]]))
        enonce.append("\\pstMarkAngle[MarkAngleRadius=1.5,Mark=MarkHash]{H}{%s}{%s}{}" %(nom[choix_sommet[0]],nom[choix_sommet[2]]))
    if choix_droite == 3:
        enonce.append("\\pstMediatorAB[PointName=none,PointSymbol=none,linecolor=red,CodeFig=true,CodeFigColor=black,nodesep=-2]{%s}{%s}{H}{K}" %(nom[choix_sommet[1]],nom[choix_sommet[2]]))
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def DroiteParticuliere(parametre):
    ## ---Initialisation---
    question = u"Donner le nom de la droite rouge :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    (choix_sommet, nom_sommet,coordonnee_sommet) = caracteristique_sommet_droite_particuliere()
    choix_droite = random.randrange(4)
    droite=[u"la hauteur issue de %s" %nom_sommet[choix_sommet[0]],
            u"la médiane issue de %s" %nom_sommet[choix_sommet[0]],
            u"la bissectrice de l'angle $\\widehat{%s%s%s}$" %(nom_sommet[choix_sommet[1]],nom_sommet[choix_sommet[0]],nom_sommet[choix_sommet[2]]),
            u"la médiatrice du côté [%s%s]" %(nom_sommet[choix_sommet[1]],nom_sommet[choix_sommet[2]])]
    ## ---Redaction---
    tex_figure_droite_particuliere(exo,nom_sommet,coordonnee_sommet,choix_sommet,choix_droite)
    tex_figure_droite_particuliere(cor,nom_sommet,coordonnee_sommet,choix_sommet,choix_droite)
    cor.append(u"C'est \\fbox{%s}" %droite[choix_droite])
    return (exo, cor, question)
