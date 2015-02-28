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
uniteAire = [ "mm^2", "cm^2", "dm^2", "m^2", "dam^2", "hm^2", "km^2"]

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
    exo.append(u"d'un carré d'aire $\\unit{%s}{%s}$" %(cote*cote,uniteAire[unite]))
    cor.append(u"d'un carré d'aire $\\unit{%s}{%s}$" %(cote*cote,uniteAire[unite]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    cor.append("\\textbf{On sait que :} \\newline")
    cor.append(u"$\\text{Aire} = \\text{côté}^2$ \\newline")
    cor.append("$\\text{Aire} = \\unit{%s}{%s}$ \\newline" %(cote*cote,uniteAire[unite]))
    cor.append("\\textbf{Conclusion :} \\newline")
    cor.append(u"$\\text{côté} = \\sqrt{%s} = \\boxed{\\unit{%s}{%s}}$ " %(cote*cote,cote,uniteLongueur[unite]))
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
    exo.append(u"d'un rectangle d'aire $\\unit{%s}{%s}$ avec un côté de mesure $\\unit{%s}{%s}$" %(cote1*cote2,uniteAire[unite],cote1,uniteLongueur[unite]))
    cor.append(u"d'un rectangle d'aire $\\unit{%s}{%s}$ avec un côté de mesure $\\unit{%s}{%s}$" %(cote1*cote2,uniteAire[unite],cote1,uniteLongueur[unite]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    cor.append("\\textbf{On sait que :} \\newline")
    cor.append(u"$\\text{Aire} = \\text{côté 1} \\times \\text{côté 2}$ \\newline")
    cor.append(u"$\\text{Aire} = %s \\times \\text{côté 2}$ \\newline" %cote1)
    cor.append(u"$\\text{Aire} = \\unit{%s}{%s} \\newline$" %(cote1*cote2,uniteAire[unite]))
    cor.append("\\textbf{Conclusion :} \\newline")
    cor.append(u"$\\text{côté 2} = %s \\div %s = \\boxed{\\unit{%s}{%s}}$" %(cote1*cote2,cote1,cote2,uniteLongueur[unite]))
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
    exo.append("d'un disque d'aire $\\unit{%s}{%s}$" %(3*rayon*rayon,uniteAire[unite]))
    cor.append("d'un disque d'aire $\\unit{%s}{%s}$" %(3*rayon*rayon,uniteAire[unite]))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    cor.append("\\textbf{On sait que :} \\newline")
    cor.append("$\\text{Aire} = \\pi \\times \\text{rayon}^2$ \\newline")
    cor.append("$\\text{Aire} = 3 \\times \\text{rayon}^2$ \\newline")
    cor.append("$\\text{Aire} = \\unit{%s}{%s}$ \\newline" %(3*rayon*rayon,uniteAire[unite]))
    cor.append("\\textbf{Conclusion :} \\newline")
    cor.append("$\\text{rayon}^2 = %s \\div 3 = %s$ \\newline" %(3*rayon*rayon,rayon*rayon))
    cor.append("$\\text{rayon} = \\sqrt{%s} = \\boxed{\\unit{%s}{%s}}$" %(rayon*rayon,rayon,uniteLongueur[unite]))
    return (exo, cor, question)
