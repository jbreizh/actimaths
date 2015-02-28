# Pyromaths
# -*- coding: utf-8 -*-
#
# Pyromaths
# Un programme en Python qui permet de créer des fiches d"exercices types de
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
# along with this program; if notPopen, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#

import random
from outils.Arithmetique import liste_combinaison

def caracteristique_sommet():
    #Nom
    choix = random.randrange(4)
    if choix == 0:
        nom_point = ["A","B","C","D","E"]
    if choix == 1:
        nom_point = ["D","A","B","C","E"]
    if choix == 2:
        nom_point = ["C","D","A","B","E"]
    if choix == 3:
        nom_point = ["B","C","D","A","E"]
    #Segment
    duo_point = liste_combinaison(nom_point[0:4],2)
    #Coordonnée
    coordonnee_point = []
    coordonnee_point.append([random.uniform(-4,-3),random.uniform(3,4)])
    coordonnee_point.append([random.uniform(-4,-3),random.uniform(-4,-3)])
    coordonnee_point.append([random.uniform(3,4),random.uniform(-4,-3)])
    coordonnee_point.append([random.uniform(3,4),random.uniform(3,4)])
    return (nom_point,duo_point,coordonnee_point)

def tex_debut_cote(enonce,nom_point,coordonnee_point):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
    for i in range(len(nom_point)-1):
        enonce.append("\\pstGeonode[PointName=none](%s,%s){%s}" %(coordonnee_point[i][0],coordonnee_point[i][1],nom_point[i]))
    enonce.append("\\pstLineAB{A}{B}")
    enonce.append("\\pstLineAB{B}{C}")
    enonce.append("\\pstLineAB{C}{D}")
    enonce.append("\\pstLineAB{D}{A}")

def tex_debut_diagonale(enonce,nom_point,coordonnee_point,duo_point):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
    for i in range(len(nom_point)-1):
        enonce.append("\\pstGeonode[PointName=none](%s,%s){%s}" %(coordonnee_point[i][0],coordonnee_point[i][1],nom_point[i]))
    for i in range(len(duo_point)):
        enonce.append("\\pstLineAB{%s}{%s}" %(duo_point[i][0],duo_point[i][1]))
    enonce.append("\\pstInterLL[PointName=none]{%s}{%s}{%s}{%s}{%s}" %(nom_point[0],nom_point[2],nom_point[1],nom_point[3],nom_point[4]))

def tex_fin(enonce):
    enonce.append("\\end{pspicture*}")
    enonce.append("\\end{center}")

def tex_quelconque_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],4)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[1])
    enonce.append("\\pstSegmentMark[%s]{C}{D}" %codage[2])
    enonce.append("\\pstSegmentMark[%s]{D}{A}" %codage[3])

def tex_quelconque_diagonale(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],3)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{E}" %codage[1])
    enonce.append("\\pstSegmentMark[%s]{E}{D}" %codage[2])

def tex_rectangle_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    style = random.randrange(3)
    ## Construction
    if style==0:
        enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{C}{D}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[1])
        enonce.append("\\pstSegmentMark[%s]{D}{A}" %codage[1])
        enonce.append("\\pstRightAngle{C}{B}{A}")
    elif style==1:
        enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{C}{D}" %codage[0])
        enonce.append("\\pstRightAngle{B}{A}{D}")
        enonce.append("\\pstRightAngle{A}{D}{C}")
    else:
        enonce.append("\\pstRightAngle{C}{B}{A}")
        enonce.append("\\pstRightAngle{B}{A}{D}")
        enonce.append("\\pstRightAngle{A}{D}{C}")
        enonce.append("\\pstRightAngle{D}{C}{B}")

def tex_rectangle_diagonale(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],1)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{D}" %codage[0])

def tex_losange_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],1)
    codage_angle = random.sample(["Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],2)
    style = random.randrange(2)
    ## Construction
    if style==0:
        enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{C}{D}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{D}{A}" %codage[0])
    else:
        enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{C}{B}{A}{}" %codage_angle[0])
        enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{B}{A}{D}{}" %codage_angle[1])
        enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{A}{D}{C}{}" %codage_angle[0])
        enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{D}{C}{B}{}" %codage_angle[1])

def tex_losange_diagonale(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{E}" %codage[1])
    enonce.append("\\pstSegmentMark[%s]{E}{D}" %codage[1])
    enonce.append("\\pstRightAngle{A}{E}{B}")

def tex_carre_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],1)
    style = random.randrange(3)
    ## Construction
    if style==0:
        enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{C}{D}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{D}{A}" %codage[0])
        enonce.append("\\pstRightAngle{C}{B}{A}")
    if style==1:
        enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{C}{D}" %codage[0])
        enonce.append("\\pstRightAngle{B}{A}{D}")
        enonce.append("\\pstRightAngle{A}{D}{C}")
    if style==2:
        enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
        enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
        enonce.append("\\pstRightAngle{C}{B}{A}")
        enonce.append("\\pstRightAngle{B}{A}{D}")
        enonce.append("\\pstRightAngle{A}{D}{C}")

def tex_carre_diagonale(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],1)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{E}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{E}{D}" %codage[0])
    enonce.append("\\pstRightAngle{A}{E}{B}")

def CodageCote(parametre):
    question = u"Quelle est la nature du quadrilatère :"
    exo = []
    cor = []
    ## Paramètre
    style = ["quelconque","rectangle","losange",u"carré"]
    choix = random.randrange(4)
    (nom_sommet,arete,coordonnee_sommet) = caracteristique_sommet()
    tex_debut_cote(exo, nom_sommet,coordonnee_sommet)
    tex_debut_cote(cor, nom_sommet,coordonnee_sommet)
    if choix == 0:
        tex_quelconque_cote(exo)
        tex_quelconque_cote(cor)
    if choix == 1:
        tex_rectangle_cote(exo)
        tex_rectangle_cote(cor)
    if choix == 2:
        tex_losange_cote(exo)
        tex_losange_cote(cor)
    if choix == 3:
        tex_carre_cote(exo)
        tex_carre_cote(cor)
    tex_fin(exo)
    tex_fin(cor)
    cor.append("\\begin{center}")
    cor.append(u"Le quadrilatère est un \\fbox{%s}" %style[choix])
    cor.append("\\end{center}")
    return (exo, cor, question)

def CodageDiagonale(parametre):
    question = u"Quelle est la nature du quadrilatère :"
    exo = []
    cor = []
    ## Paramètre
    style = ["quelconque","rectangle","losange",u"carré"]
    choix = random.randrange(4)
    (nom_sommet,arete,coordonnee_sommet) = caracteristique_sommet()
    tex_debut_diagonale(exo, nom_sommet,coordonnee_sommet,arete)
    tex_debut_diagonale(cor, nom_sommet,coordonnee_sommet,arete)
    if choix == 0:
        tex_quelconque_diagonale(exo)
        tex_quelconque_diagonale(cor)
    if choix == 1:
        tex_rectangle_diagonale(exo)
        tex_rectangle_diagonale(cor)
    if choix == 2:
        tex_losange_diagonale(exo)
        tex_losange_diagonale(cor)
    if choix == 3:
        tex_carre_diagonale(exo)
        tex_carre_diagonale(cor)
    tex_fin(exo)
    tex_fin(cor)
    cor.append("\\begin{center}")
    cor.append(u"Le quadrilatère est un \\fbox{%s}" %style[choix])
    cor.append("\\end{center}")
    return (exo, cor, question)
