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

def caracteristique_sommet():
    choix = random.randrange(3)
    if choix == 0:
        nom = ["A","B","C"]
    elif choix == 1:
        nom = ["C","A","B"]
    else:
        nom = ["B","C","A"]
    coordonnee = (random.uniform(-1.5,1.5),random.uniform(1.5,2.5),random.uniform(-2.5,-1.5),random.uniform(-2.5,-1.5),random.uniform(1.5,2.5),random.uniform(-2.5,-1.5))
    return (nom,coordonnee)

def tex_debut(enonce,nom,coordonnee):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-3,-3)(3,3)")
    enonce.append("\\pstTriangle[PointName=none](%s,%s){%s}(%s,%s){%s}(%s,%s){%s}" %(coordonnee[0],coordonnee[1],nom[0],coordonnee[2],coordonnee[3],nom[1],coordonnee[4],coordonnee[5],nom[2]))

def tex_fin(enonce):
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_quelconque_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],3)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[1])
    enonce.append("\\pstSegmentMark[%s]{C}{A}" %codage[2])

def tex_quelconque_angle(enonce):
    ## Paramètre
    codage = random.sample(["Mark=None","Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],3)
    ## Construction
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{C}{B}{A}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{B}{A}{C}{}" %codage[1])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{A}{C}{B}{}" %codage[2])

def tex_isocele_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    while codage[0] == "SegmentSymbol=None":
        codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{C}{A}" %codage[1])

def tex_isocele_angle(enonce):
    ## Paramètre
    codage = random.sample(["Mark=None","Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],2)
    while codage[0] == "Mark=None":
        codage = random.sample(["Mark=None","Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],2)
    ## Construction
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{C}{B}{A}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{B}{A}{C}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{A}{C}{B}{}" %codage[1])

def tex_equilateral_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],1)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{C}{A}" %codage[0])

def tex_equilateral_angle(enonce):
    ## Paramètre
    codage = random.sample(["Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],1)
    ## Construction
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{C}{B}{A}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{B}{A}{C}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{A}{C}{B}{}" %codage[0])

def tex_rectangle_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],3)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[1])
    enonce.append("\\pstSegmentMark[%s]{C}{A}" %codage[2])
    enonce.append("\\pstRightAngle{C}{B}{A}")

def tex_rectangle_angle(enonce):
    ## Paramètre
    codage = random.sample(["Mark=None","Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],2)
    ## Construction
    enonce.append("\\pstRightAngle{C}{B}{A}")
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{B}{A}{C}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{A}{C}{B}{}" %codage[1])

def tex_isocele_rectangle_cote(enonce):
    ## Paramètre
    codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    while codage[0] == "SegmentSymbol=None":
        codage = random.sample(["SegmentSymbol=None","SegmentSymbol=pstslash","SegmentSymbol=pstslashh","SegmentSymbol=pstslashhh"],2)
    ## Construction
    enonce.append("\\pstSegmentMark[%s]{A}{B}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{B}{C}" %codage[0])
    enonce.append("\\pstSegmentMark[%s]{C}{A}" %codage[1])
    enonce.append("\\pstRightAngle{C}{B}{A}")

def tex_isocele_rectangle_angle(enonce):
    ## Paramètre
    codage = random.sample(["Mark=pstslash","Mark=pstslashh","Mark=pstslashhh"],1)
    ## Construction
    enonce.append("\\pstRightAngle{C}{B}{A}")
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{B}{A}{C}{}" %codage[0])
    enonce.append("\\pstMarkAngle[MarkAngleRadius=.6,%s]{A}{C}{B}{}" %codage[0])

def CodageCote(parametre):
    question = u"Quelle est la nature du triangle :"
    exo = []
    cor = []
    ## Paramètre
    style = ["quelconque",u"isocèle",u"équilatéral","rectangle",u"isocèle rectangle"]
    choix = random.randrange(5)
    (nom_sommet,coordonnee_sommet) = caracteristique_sommet()
    tex_debut(exo, nom_sommet,coordonnee_sommet)
    tex_debut(cor, nom_sommet,coordonnee_sommet)
    if choix == 0:
        tex_quelconque_cote(exo)
        tex_quelconque_cote(cor)
    if choix == 1:
        tex_isocele_cote(exo)
        tex_isocele_cote(cor)
    if choix == 2:
        tex_equilateral_cote(exo)
        tex_equilateral_cote(cor)
    if choix == 3:
        tex_rectangle_cote(exo)
        tex_rectangle_cote(cor)
    if choix == 4:
        tex_isocele_rectangle_cote(exo)
        tex_isocele_rectangle_cote(cor)
    tex_fin(exo)
    tex_fin(cor)
    cor.append("\\begin{center}")
    cor.append(u"C'est un triangle \\fbox{%s}" %style[choix])
    cor.append("\\end{center}")
    return (exo, cor, question)

def CodageAngle(parametre):
    question = u"Quelle est la nature du triangle :"
    exo = []
    cor = []
    ## Paramètre
    style = ["quelconque",u"isocèle",u"équilatéral","rectangle",u"isocèle rectangle"]
    choix = random.randrange(5)
    (nom_sommet,coordonnee_sommet) = caracteristique_sommet()
    tex_debut(exo, nom_sommet,coordonnee_sommet)
    tex_debut(cor, nom_sommet,coordonnee_sommet)
    if choix == 0:
        tex_quelconque_angle(exo)
        tex_quelconque_angle(cor)
    if choix == 1:
        tex_isocele_angle(exo)
        tex_isocele_angle(cor)
    if choix == 2:
        tex_equilateral_angle(exo)
        tex_equilateral_angle(cor)
    if choix == 3:
        tex_rectangle_angle(exo)
        tex_rectangle_angle(cor)
    if choix == 4:
        tex_isocele_rectangle_angle(exo)
        tex_isocele_rectangle_angle(cor)
    tex_fin(exo)
    tex_fin(cor)
    cor.append("\\begin{center}")
    cor.append(u"C'est un triangle \\fbox{%s}" %style[choix])
    cor.append("\\end{center}")
    return (exo, cor, question)
