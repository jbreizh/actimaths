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
def tex_figure_egalite_pythagore(enonce,nom_point):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-3,-3)(4,3)')
    # trace du triangle
    enonce.append("\\pstTriangle[SegmentSymbolA=\"rt\"](-2,-2){%s}(-2,2){%s}(3,-2){%s}" %(nom_point[0],nom_point[1],nom_point[2]))
    # trace de l'angle droit
    enonce.append("\\pstRightAngle{%s}{%s}{%s}" %(nom_point[1],nom_point[0],nom_point[2]))
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

def tex_figure_calcul_pythagore(enonce,nom_point,mesure_cote):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-3,-3)(4,3)')
    # trace du triangle
    enonce.append("\\pstTriangle[SegmentSymbolA=\"rt\"](-2,-2){%s}(-2,2){%s}(3,-2){%s}" %(nom_point[0],nom_point[1],nom_point[2]))
    # trace de l'angle droit
    enonce.append("\\pstRightAngle{%s}{%s}{%s}" %(nom_point[1],nom_point[0],nom_point[2]))
    # affichage des mesure
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{cm}$}" % (90,-2.8,0,mesure_cote[0]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{cm}$}" % (0,0.5,-2.3,mesure_cote[1]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{cm}$}" % (-40,1,0.7,mesure_cote[2]))
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def EgalitePythagoreTexte(parametre):
    ## ---Calcul des paramètres---
    #nom
    nom_sommet = choix_points(3)
    duo_sommet = liste_combinaison(nom_sommet, 2)
    ## ---Initialisation---
    question = u"Donner l'égalité de Pythagore :"
    exo = [ ]
    cor = [ ]
    ## ---Redaction du sujet---
    exo.append("\\begin{center}")
    exo.append("%s%s%s est rectangle en %s" %(nom_sommet[0],nom_sommet[1],nom_sommet[2],nom_sommet[0]))
    exo.append("\\end{center}")
    ## ---Redaction du corrigé---
    cor.append("\\begin{center}")
    cor.append("%s%s%s est rectangle en %s" %(nom_sommet[0],nom_sommet[1],nom_sommet[2],nom_sommet[0]))
    cor.append("\\end{center}")
    cor.append("\\begin{center}")
    cor.append("$\\boxed{%s%s^2 = %s%s^2 + %s%s^2}$" % (duo_sommet[2][0],duo_sommet[2][1],duo_sommet[1][0],duo_sommet[1][1],duo_sommet[0][0],duo_sommet[0][1]))
    cor.append("\\end{center}")
    return (exo, cor, question)

def CalculPythagoreTexte(parametre):
    ## ---Calcul des paramètres---
    #nom
    nom_sommet = choix_points(3)
    duo_sommet = liste_combinaison(nom_sommet, 2)
    #mesure
    couples_pythagore = trouve_couples_pythagore(parametre[0])
    choix = random.randrange(3)
    mesure_corrige = couples_pythagore[random.randrange(len(couples_pythagore))]
    mesure_sujet = []
    for i in range(len(mesure_corrige)):
        if i == choix:
            mesure_sujet.append("\\ldots")
        else:
            mesure_sujet.append(mesure_corrige[i])
    ## ---Initialisation---
    question = u"Calculer %s%s :" %(duo_sommet[choix][0],duo_sommet[choix][1])
    exo = [ ]
    cor = [ ]
    ## ---Redaction du sujet---
    exo.append("%s%s%s est rectangle en %s tel que :" %(nom_sommet[0],nom_sommet[1],nom_sommet[2],nom_sommet[0]))
    exo.append("\\begin{itemize}")
    for i in range(len(duo_sommet)):
        exo.append("\\item $%s%s=\\unit{%s}{cm}$" % (duo_sommet[i][0],duo_sommet[i][1],mesure_sujet[i]))
    exo.append("\\end{itemize}")
    ## ---Redaction du corrigé---
    cor.append("%s%s%s est rectangle en %s tel que :" %(nom_sommet[0],nom_sommet[1],nom_sommet[2],nom_sommet[0]))
    cor.append("\\begin{itemize}")
    for i in range(len(duo_sommet)):
        cor.append("\\item $%s%s=\\unit{%s}{cm}$" % (duo_sommet[i][0],duo_sommet[i][1],mesure_sujet[i]))
    cor.append("\\end{itemize}")
    cor.append("\\begin{tabular}{ll}")
    cor.append("\\underline{On a} :     & %s%s%s rectangle en %s \\\\" % (nom_sommet[0],nom_sommet[1],nom_sommet[2],nom_sommet[0]))
    cor.append(u"\\underline{D'après} : & Pythagore \\\\")
    cor.append("\\underline{Donc} :     & $%s%s^2 = %s%s^2 + %s%s^2$ \\\\" % (duo_sommet[2][0],duo_sommet[2][1],duo_sommet[1][0],duo_sommet[1][1],duo_sommet[0][0],duo_sommet[0][1]))
    if choix == 0:
        cor.append("                        & $%s%s^2 = %s^2 - %s^2$ \\\\" % (duo_sommet[0][0],duo_sommet[0][1],mesure_corrige[2],mesure_corrige[1]))
        cor.append("                        & $%s%s = \\boxed{\\unit{%s}{cm}}$ \\\\" % (duo_sommet[0][0],duo_sommet[0][1],mesure_corrige[0]))
    elif choix == 1:
        cor.append("                        & $%s%s^2 = %s^2 - %s^2$ \\\\" % (duo_sommet[1][0],duo_sommet[1][1],mesure_corrige[2],mesure_corrige[0]))
        cor.append("                        & $%s%s = \\boxed{\\unit{%s}{cm}}$ \\\\" % (duo_sommet[1][0],duo_sommet[1][1],mesure_corrige[1]))
    elif choix == 2:
        cor.append("                        & $%s%s^2 = %s^2 + %s^2$ \\\\" % (duo_sommet[2][0],duo_sommet[2][1],mesure_corrige[1],mesure_corrige[0]))
        cor.append("                        & $%s%s = \\boxed{\\unit{%s}{cm}}$ \\\\" % (duo_sommet[2][0],duo_sommet[2][1],mesure_corrige[2]))
    cor.append("\\end{tabular}")
    return (exo, cor, question)

def EgalitePythagoreSchema(parametre):
    ## ---Calcul des paramètres---
    #nom
    nom_sommet = choix_points(3)
    duo_sommet = liste_combinaison(nom_sommet, 2)
    ## ---Initialisation---
    question = u"Donner l'égalité de Pythagore :"
    exo = [ ]
    cor = [ ]
    ## ---Redaction du sujet---
    tex_figure_egalite_pythagore(exo,nom_sommet)
    ## ---Redaction du corrigé---
    tex_figure_egalite_pythagore(cor,nom_sommet)
    cor.append("\\begin{center}")
    cor.append("$\\boxed{%s%s^2 = %s%s^2 + %s%s^2}$" % (duo_sommet[2][0],duo_sommet[2][1],duo_sommet[1][0],duo_sommet[1][1],duo_sommet[0][0],duo_sommet[0][1]))
    cor.append("\\end{center}")
    return (exo, cor, question)

def CalculPythagoreSchema(parametre):
    ## ---Calcul des paramètres---
    #nom
    nom_sommet = choix_points(3)
    duo_sommet = liste_combinaison(nom_sommet, 2)
    #mesure
    couples_pythagore = trouve_couples_pythagore(parametre[0])
    choix = random.randrange(3)
    mesure_corrige = couples_pythagore[random.randrange(len(couples_pythagore))]
    mesure_sujet = []
    for i in range(len(mesure_corrige)):
        if i == choix:
            mesure_sujet.append("\\ldots")
        else:
            mesure_sujet.append(mesure_corrige[i])
    ## ---Initialisation---
    question = u"Calculer %s%s :" %(duo_sommet[choix][0],duo_sommet[choix][1])
    exo = [ ]
    cor = [ ]
    ## ---Redaction du sujet---
    tex_figure_calcul_pythagore(exo,nom_sommet,mesure_sujet)
    ## ---Redaction du corrigé---
    tex_figure_calcul_pythagore(cor,nom_sommet,mesure_sujet)
    cor.append("\\begin{tabular}{ll}")
    cor.append("\\underline{On a} :     & %s%s%s rectangle en %s \\\\" % (nom_sommet[0],nom_sommet[1],nom_sommet[2],nom_sommet[0]))
    cor.append(u"\\underline{D'après} : & Pythagore \\\\")
    cor.append("\\underline{Donc} :     & $%s%s^2 = %s%s^2 + %s%s^2$ \\\\" % (duo_sommet[2][0],duo_sommet[2][1],duo_sommet[1][0],duo_sommet[1][1],duo_sommet[0][0],duo_sommet[0][1]))
    if choix == 0:
        cor.append("                        & $%s%s^2 = %s^2 - %s^2$ \\\\" % (duo_sommet[0][0],duo_sommet[0][1],mesure_corrige[2],mesure_corrige[1]))
        cor.append("                        & $%s%s = \\boxed{\\unit{%s}{cm}}$ \\\\" % (duo_sommet[0][0],duo_sommet[0][1],mesure_corrige[0]))
    elif choix == 1:
        cor.append("                        & $%s%s^2 = %s^2 - %s^2$ \\\\" % (duo_sommet[1][0],duo_sommet[1][1],mesure_corrige[2],mesure_corrige[0]))
        cor.append("                        & $%s%s = \\boxed{\\unit{%s}{cm}}$ \\\\" % (duo_sommet[1][0],duo_sommet[1][1],mesure_corrige[1]))
    elif choix == 2:
        cor.append("                        & $%s%s^2 = %s^2 + %s^2$ \\\\" % (duo_sommet[2][0],duo_sommet[2][1],mesure_corrige[1],mesure_corrige[0]))
        cor.append("                        & $%s%s = \\boxed{\\unit{%s}{cm}}$ \\\\" % (duo_sommet[2][0],duo_sommet[2][1],mesure_corrige[2]))
    cor.append("\\end{tabular}")
    return (exo, cor, question)
