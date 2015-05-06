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
