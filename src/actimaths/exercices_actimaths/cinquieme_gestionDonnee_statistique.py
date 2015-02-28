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

def tex_tableau(texte, nombre):
    texte.append("\\begin{center}")
    texte.append("\\begin{tabular}{|c|c|c|c|}")
    texte.append("\\hline")
    texte.append("%s & %s & %s & %s \\\\" % (nombre[0][0], nombre[1][0], nombre[2][0], nombre[3][0]))
    texte.append("\\hline")
    texte.append("%s & %s & %s & %s \\\\" % (nombre[0][1], nombre[1][1], nombre[2][1], nombre[3][1]))
    texte.append("\\hline")   
    texte.append("\\end{tabular}")
    texte.append("\\end{center}")

def tex_calcul_coefficient(exo,cor):
    nombre = random.sample(range(1,11), 4)
    coefficient = random.randrange (2, 10)
    colonneCor = random.randrange (0, 4)
    nombreExo = []
    nombreCor = []
    for i in range(len(nombre)):
        nombreExo.append([nombre[i],nombre[i]*coefficient])
        if i == colonneCor:
            nombreCor.append(["\\textbf{%s}" % nombre[i],"\\textbf{%s}" % (nombre[i]*coefficient)])
        else:
            nombreCor.append([nombre[i],nombre[i]*coefficient])
     
    tex_tableau(exo, nombreExo)
    tex_tableau(cor, nombreCor)
    cor.append("$$ %s \\times \\ldots = %s $$" % (nombreExo[colonneCor][0], nombreExo[colonneCor][1]))    
    cor.append("$$ %s \\times \\textbf{%s} = %s $$" % (nombreExo[colonneCor][0], coefficient, nombreExo[colonneCor][1]))
    cor.append("Le coefficient est \\textbf{%s}" % coefficient)

def tex_complete_tableau(exo,cor):
    nombre = random.sample(range(1,11), 4)
    coefficient = random.randrange (2, 10)
    colonneExo = random.randrange (0, len(nombre))
    ligneExo = random.randrange (0, 2)
    nombreExo = []
    nombreCor = []
    for i in range(len(nombre)):
        if i == colonneExo:
            if ligneExo == 0:
                 nombreExo.append(["\\ldots",nombre[i]*coefficient])
                 nombreCor.append(["\\textbf{%s}" % nombre[i],nombre[i]*coefficient])
            else:
                nombreExo.append([nombre[i],"\\ldots"])
                nombreCor.append([nombre[i],"\\textbf{%s}" % (nombre[i]*coefficient)])
                print nombre[i]*coefficient
        else:
            nombreExo.append([nombre[i],nombre[i]*coefficient])
            nombreCor.append([nombre[i],nombre[i]*coefficient])
        
    tex_tableau(exo, nombreExo)
    tex_tableau(cor, nombreCor)
    cor.append("Le coefficient est %s donc" % coefficient)
    cor.append("$$ %s \\times %s = %s $$" % (nombreExo[colonneExo][0], coefficient, nombreExo[colonneExo][1]))    
    cor.append("$$ %s \\times %s = %s $$" % (nombreCor[colonneExo][0], coefficient, nombreCor[colonneExo][1]))
    cor.append("Le nombre est %s" % nombreCor[colonneExo][ligneExo])

def CalculEffectif(parametre):
    exo = [ u"\\question{Calcul le coefficient de proportionnalité du tableau}"]
    cor = [ u"\\corrige{Calcul le coefficient de proportionnalité du tableau}"]
    for i in range(2):
	exo.extend(["\\begin{column}{.5\\textwidth}"])
        cor.extend(["\\begin{column}{.5\\textwidth}"])

        exo.extend(["\\end{column}"])
        cor.extend(["\\end{column}"])
    return (exo, cor)

def CalculFrequence(parametre):
    exo = [ u"\\question{Calcul le coefficient de proportionnalité du tableau}"]
    cor = [ u"\\corrige{Calcul le coefficient de proportionnalité du tableau}"]
    for i in range(2):
	exo.extend(["\\begin{column}{.5\\textwidth}"])
        cor.extend(["\\begin{column}{.5\\textwidth}"])

        exo.extend(["\\end{column}"])
        cor.extend(["\\end{column}"])
    return (exo, cor)

