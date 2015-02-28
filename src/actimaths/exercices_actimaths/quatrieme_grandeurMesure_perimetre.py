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
uniteLongueur = [ "mm", "cm", "dm", "m", "dam", "hm", "km"]

def Carre(parametre):
    ## ---Initialisation---
    question = u"Donner la mesure du côté :"
    exo = [ ]
    cor = [ ]
    ## ---Paramètre---
    unite = random.randrange(7)
    cote = random.randrange(parametre[0],parametre[1])
    ## ---Initialisation---
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append(u"d'un carré de périmètre $\\unit{%s}{%s}$" %(4*cote,uniteLongueur[unite]))
    cor.append(u"d'un carré de périmètre $\\unit{%s}{%s}$" %(4*cote,uniteLongueur[unite]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    cor.append("\\textbf{On sait que :} \\newline")
    cor.append(u"$\\text{périmètre} = 4 \\times \\text{côté}$ \\newline")
    cor.append(u"$\\text{périmètre} = \\unit{%s}{%s}$ \\newline" %(4*cote,uniteLongueur[unite]))
    cor.append("\\textbf{Conclusion :} \\newline")
    cor.append(u"$\\text{côté} = %s \\div 4 = \\boxed{\\unit{%s}{%s}}$ " %(4*cote,cote,uniteLongueur[unite]))
    return (exo, cor, question)

def Rectangle(parametre):
    ## ---Initialisation---
    question = u"Donner la mesure de l'autre côté :"
    exo = [ ]
    cor = [ ]
    ## ---Paramètre---
    unite = random.randrange(7)
    cote1 = random.randrange(parametre[0],parametre[1])
    cote2 = random.randrange(parametre[0],parametre[1])
    ## ---Initialisation---
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append(u"d'un rectangle de périmètre $\\unit{%s}{%s}$ avec un côté de mesure $\\unit{%s}{%s}$" %(2*cote1+2*cote2,uniteLongueur[unite],cote1,uniteLongueur[unite]))
    cor.append(u"d'un rectangle de périmètre $\\unit{%s}{%s}$ avec un côté de mesure $\\unit{%s}{%s}$" %(2*cote1+2*cote2,uniteLongueur[unite],cote1,uniteLongueur[unite]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    cor.append("\\textbf{On sait que :} \\newline")
    cor.append(u"$\\text{périmètre} = 2 \\times \\text{côté 1} +  2 \\times \\text{côté 2}$ \\newline")
    cor.append(u"$\\text{périmètre} = 2 \\times %s + \\text{côté 2}$ \\newline" %cote1)
    cor.append(u"$\\text{périmètre} = %s + \\text{côté 2}$ \\newline" %(2*cote1))
    cor.append(u"$\\text{périmètre} = \\unit{%s}{%s} \\newline$" %(2*cote1+2*cote2,uniteLongueur[unite]))
    cor.append("\\textbf{Conclusion :} \\newline")
    cor.append(u"$2 \\times \\text{côté 2} = %s - %s = %s $" %(2*cote1+2*cote2,2*cote1,2*cote2))
    cor.append(u"$\\text{côté 2} = %s \\div 2 = \\boxed{\\unit{%s}{%s}}$" %(2*cote2,cote2,uniteLongueur[unite]))
    return (exo, cor, question)

def Disque(parametre):
    ## ---Initialisation---
    question = u"Donner la mesure du rayon ($\\pi \\approx 3$) :"
    exo = [ ]
    cor = [ ]
    ## ---Paramètre---
    unite = random.randrange(7)
    rayon = random.randrange(parametre[0],parametre[1])
    ## ---Initialisation---
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append(u"d'un disque de périmètre $\\unit{%s}{%s}$" %(6*rayon,uniteLongueur[unite]))
    cor.append(u"d'un disque de périmètre $\\unit{%s}{%s}$" %(6*rayon,uniteLongueur[unite]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    cor.append("\\textbf{On sait que :} \\newline")
    cor.append(u"$\\text{périmètre} = 2 \\times \\pi \\times \\text{rayon}$ \\newline")
    cor.append(u"$\\text{périmètre} = 6 \\times \\text{rayon}$ \\newline")
    cor.append(u"$\\text{périmètre} = \\unit{%s}{%s}$ \\newline" %(6*rayon,uniteLongueur[unite]))
    cor.append("\\textbf{Conclusion :} \\newline")
    cor.append("$\\text{rayon} = %s \\div 6 = \\boxed{\\unit{%s}{%s}}$" %(6*rayon,rayon,uniteLongueur[unite]))
    return (exo, cor, question)
