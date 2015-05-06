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
