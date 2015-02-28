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

def tex_debut(enonce):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-5)(5,5)")

def tex_fin(enonce):
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_cercle_rayon(enonce,coordonnee):
    enonce.append("\\pstGeonode[PointName=none](0,0){O}(%s,%s){A}" % (coordonnee[0],coordonnee[1]))
    enonce.append("\\pstCircleOA{O}{A}")
    enonce.append("\\pstLineAB[linecolor=red]{O}{A}")

def tex_cercle_diametre(enonce,coordonnee):
    enonce.append("\\pstGeonode[PointName=none](0,0){O}(%s,%s){A}(%s,%s){B}" % (coordonnee[0],coordonnee[1],-coordonnee[0],-coordonnee[1]))
    enonce.append("\\pstCircleOA{O}{A}")
    enonce.append("\\pstLineAB[linecolor=red]{A}{B}")

def tex_cercle_corde(enonce,coordonnee):
    enonce.append("\\pstGeonode[PointName=none](0,0){O}(%s,%s){A}" % (coordonnee[0],coordonnee[1]))
    enonce.append("\\pstCircleOA{O}{A}")
    enonce.append("\\pstCurvAbsNode[PointName=none]{O}{A}{B}{\\pstDistVal{%s}}" %random.uniform(3,6))
    enonce.append("\\pstLineAB[linecolor=red]{A}{B}")

def tex_cercle_arc(enonce,coordonnee):
    enonce.append("\\pstGeonode[PointName=none](0,0){O}(%s,%s){A}" % (coordonnee[0],coordonnee[1]))
    enonce.append("\\pstCircleOA{O}{A}")
    enonce.append("\\pstCurvAbsNode[PointName=none]{O}{A}{B}{\\pstDistVal{%s}}" %random.uniform(3,6))
    enonce.append("\\pstArcOAB[linecolor=red]{O}{A}{B}")

def Vocabulaire(parametre):
    question = u"Quelle est la nature de l'objet rouge :"
    exo = []
    cor = []
    ## Paramètre
    style = ["un rayon",u"un diamètre",u"une corde","un arc de cercle"]
    choix = random.randrange(4)
    coordonnee_point = (random.uniform(-3,-2),random.uniform(-3,3))
    tex_debut(exo)
    tex_debut(cor)
    if choix == 0:
        tex_cercle_rayon(exo,coordonnee_point)
        tex_cercle_rayon(cor,coordonnee_point)
    if choix == 1:
        tex_cercle_diametre(exo,coordonnee_point)
        tex_cercle_diametre(cor,coordonnee_point)
    if choix == 2:
        tex_cercle_corde(exo,coordonnee_point)
        tex_cercle_corde(cor,coordonnee_point)
    if choix == 3:
        tex_cercle_arc(exo,coordonnee_point)
        tex_cercle_arc(cor,coordonnee_point)
    tex_fin(exo)
    tex_fin(cor)
    cor.append("\\begin{center}")
    cor.append(u"C'est \\fbox{%s}" %style[choix])
    cor.append("\\end{center}")
    return (exo, cor, question)
