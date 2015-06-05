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
from outils.Geometrie import choix_points
from math import sqrt

#------------------methode---------------------------------------------
def caracteristique_sommet_thales():
    ## Nom des sommets
    nom_ordre = choix_points(5)
    choix = random.randrange(3)
    if choix == 0:
        nom_melange = [nom_ordre[0],nom_ordre[1],nom_ordre[2]]
    elif choix == 1:
        nom_melange = [nom_ordre[2],nom_ordre[0],nom_ordre[1]]
    else:
        nom_melange = [nom_ordre[1],nom_ordre[2],nom_ordre[0]]
    ## coordonnées des sommets
    coordonnee = (random.uniform(-1,1),random.uniform(1,3),random.uniform(-3,-1),random.uniform(-3,-1),random.uniform(1,3),random.uniform(-3,-1))
    return (nom_ordre,nom_melange,coordonnee)

def caracteristique_cote_thales(longueur_min,longueur_max):
    ## longueur des cotés du petit triangle
    mesure = [random.randint(int(sqrt(longueur_min)),int(sqrt(longueur_max))) for i in xrange(3)]
    ## coefficient d'agrandissement pour avoir le grand triangle > 2
    coef_agrandissement = random.randint(max(int(sqrt(longueur_min)),2),max(int(sqrt(longueur_max)),2))
    ## longueur des cotés du grand triangle
    for i in range(3):
        mesure.append(mesure[i]*coef_agrandissement)
    ## choix de la mesure manquante
    mesure_manquante = random.randrange(6)
    ## Tex des mesures pour le sujet et le corrigé
    tex_mesure_sujet =[]
    tex_mesure_corrige =[]
    for i in range(6):
        if i != mesure_manquante:
            tex_mesure_sujet.append("%s" % mesure[i])
            tex_mesure_corrige.append("%s" % mesure[i])
        else:
            tex_mesure_sujet.append("\\ldots")
            tex_mesure_corrige.append("\\boxed{%s}" % mesure[i])

    return (tex_mesure_sujet,tex_mesure_corrige)

def tex_figure_thales(enonce,nom_ordre,nom_melange,coordonnee):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-5,-5)(5,5)')
    # points du grand triangle
    enonce.append("\\pstGeonode(%s,%s){%s}(%s,%s){%s}(%s,%s){%s}" %(coordonnee[0],coordonnee[1],nom_melange[0],coordonnee[2],coordonnee[3],nom_melange[1],coordonnee[4],coordonnee[5],nom_melange[2]))
    # points du petit triangle
    enonce.append("\\pstHomO[HomCoef=-0.3]{%s}{%s,%s}[%s,%s]" %(nom_ordre[0],nom_ordre[1],nom_ordre[2],nom_ordre[3],nom_ordre[4]))
    # grand triangle
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[1],nom_ordre[0]))
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[2],nom_ordre[1]))
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[0],nom_ordre[2]))
    # petit triangle
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[3],nom_ordre[0]))
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[4],nom_ordre[3]))
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[0],nom_ordre[4]))
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

def tex_figure_thales_mesure(enonce,nom_ordre,nom_melange,coordonnee,tex_mesure):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.4cm}")
    enonce.append('\\begin{pspicture*}(-5,-5)(5,5)')
    # points du grand triangle
    enonce.append("\\pstGeonode[PointName=none](%s,%s){%s}(%s,%s){%s}(%s,%s){%s}" %(coordonnee[0],coordonnee[1],nom_melange[0],coordonnee[2],coordonnee[3],nom_melange[1],coordonnee[4],coordonnee[5],nom_melange[2]))
    # points du petit triangle
    enonce.append("\\pstHomO[HomCoef=-0.3,PointName=none]{%s}{%s,%s}[%s,%s]" %(nom_ordre[0],nom_ordre[1],nom_ordre[2],nom_ordre[3],nom_ordre[4]))
    # grand triangle
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[1],nom_ordre[0]))
    enonce.append("\\ncline[offset=3pt,linestyle=dashed,arrows=<->]{%s}{%s}" %(nom_ordre[1],nom_ordre[0]))
    enonce.append("\\naput{\\footnotesize{$%s$}}" %tex_mesure[3])
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[2],nom_ordre[1]))
    enonce.append("\\ncline[offset=3pt,linestyle=dashed,arrows=<->]{%s}{%s}" %(nom_ordre[2],nom_ordre[1]))
    enonce.append("\\naput{\\footnotesize{$%s$}}" %tex_mesure[4])
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[0],nom_ordre[2]))
    enonce.append("\\ncline[offset=3pt,linestyle=dashed,arrows=<->]{%s}{%s}" %(nom_ordre[0],nom_ordre[2]))
    enonce.append("\\naput{\\footnotesize{$%s$}}" %tex_mesure[5])
    # petit triangle
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[3],nom_ordre[0]))
    enonce.append("\\ncline[offset=3pt,linestyle=dashed,arrows=<->]{%s}{%s}" %(nom_ordre[3],nom_ordre[0]))
    enonce.append("\\naput{\\footnotesize{$%s$}}" %tex_mesure[0])
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[4],nom_ordre[3]))
    enonce.append("\\ncline[offset=3pt,linestyle=dashed,arrows=<->]{%s}{%s}" %(nom_ordre[4],nom_ordre[3]))
    enonce.append("\\naput{\\footnotesize{$%s$}}" %tex_mesure[1])
    enonce.append("\\pstLineAB{%s}{%s}" %(nom_ordre[0],nom_ordre[4]))
    enonce.append("\\ncline[offset=3pt,linestyle=dashed,arrows=<->]{%s}{%s}" %(nom_ordre[0],nom_ordre[4]))
    enonce.append("\\naput{\\footnotesize{$%s$}}" %tex_mesure[2])
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def ThalesQuotient(parametre):
    ## ---Initialisation---
    question = u"Écrire l'égalité de thalès :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    (nom_ordre,nom_melange,coordonnee) = caracteristique_sommet_thales()
    ## ---Redaction---
    tex_figure_thales(exo,nom_ordre,nom_melange,coordonnee)
    tex_figure_thales(cor,nom_ordre,nom_melange,coordonnee)
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("$\\dfrac{\\ldots}{\\ldots}=\\dfrac{\\ldots}{\\ldots}=\\dfrac{\\ldots}{\\ldots}$")
    cor.append("$\\dfrac{%s%s}{%s%s}=\\dfrac{%s%s}{%s%s}=\\dfrac{%s%s}{%s%s}$" %(nom_ordre[0],nom_ordre[3],nom_ordre[0],nom_ordre[1],nom_ordre[0],nom_ordre[4],nom_ordre[0],nom_ordre[2],nom_ordre[3],nom_ordre[4],nom_ordre[1],nom_ordre[2]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor, question)

def ThalesTableau(parametre):
    ## ---Initialisation---
    question = u"Écrire l'égalité de thalès :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    (nom_ordre,nom_melange,coordonnee) = caracteristique_sommet_thales()
    ## ---Redaction---
    tex_figure_thales(exo,nom_ordre,nom_melange,coordonnee)
    tex_figure_thales(cor,nom_ordre,nom_melange,coordonnee)
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("\\begin{tabular}{|l|c|c|c|}")
    exo.append("\\hline")
    exo.append("Petit triangle & $\\ldots$ & $\\ldots$ & $\\ldots$ \\\\")
    exo.append("\\hline")
    exo.append("Grand triangle & $\\ldots$ & $\\ldots$ & $\\ldots$ \\\\")
    exo.append("\\hline")
    exo.append("\\end{tabular}")
    cor.append("\\begin{tabular}{|l|c|c|c|}")
    cor.append("\\hline")
    cor.append("Petit triangle & %s%s & %s%s & %s%s \\\\" %(nom_ordre[0],nom_ordre[3],nom_ordre[0],nom_ordre[4],nom_ordre[3],nom_ordre[4]))
    cor.append("\\hline")
    cor.append("Grand triangle & %s%s & %s%s & %s%s \\\\" %(nom_ordre[0],nom_ordre[1],nom_ordre[0],nom_ordre[2],nom_ordre[1],nom_ordre[2]))
    cor.append("\\hline")
    cor.append("\\end{tabular}")
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor, question)

def ThalesQuotientMesure(parametre):
    ## ---Initialisation---
    question = u"Calculer la longueur manquante :"
    exo = [ ]
    cor = [ ]
    ## ---Calcul des paramètres---
    (nom_ordre,nom_melange,coordonnee) = caracteristique_sommet_thales()
    (tex_mesure_sujet,tex_mesure_corrige) = caracteristique_cote_thales(parametre[0],parametre[1])
    ## ---Redaction du sujet---
    tex_figure_thales_mesure(exo,nom_ordre,nom_melange,coordonnee,tex_mesure_sujet)
    ## ---Redaction du corrige---
    tex_figure_thales_mesure(cor,nom_ordre,nom_melange,coordonnee,tex_mesure_corrige)
    cor.append(u"On utilise le \\textbf{Théorème de Thalès}")
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("\\dfrac{%s}{%s} & = & \\dfrac{%s}{%s} & = & \\dfrac{%s}{%s} \\\\" %(tex_mesure_sujet[0],tex_mesure_sujet[3],tex_mesure_sujet[1],tex_mesure_sujet[4],tex_mesure_sujet[2],tex_mesure_sujet[5]))
    cor.append("\\dfrac{%s}{%s} & = & \\dfrac{%s}{%s} & = & \\dfrac{%s}{%s} \\\\" %(tex_mesure_corrige[0],tex_mesure_corrige[3],tex_mesure_corrige[1],tex_mesure_corrige[4],tex_mesure_corrige[2],tex_mesure_corrige[5]))
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)
