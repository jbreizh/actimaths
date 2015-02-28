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
#---------------methode--------------------------------
def tex_tableau(tex, contenu):
    nombreColonne = len(contenu)
    if nombreColonne != 0:
        nombreLigne = len(contenu[0])
        # entete du tableau
        tex.append("\\begin{center}")
        ligne = "\\begin{tabular}{|"
        for i in range(len(contenu)):
            ligne += "c|"
        ligne += "}"
        tex.append(ligne)
        # corps du tableau
        for i in range(nombreLigne):
            tex.append("\\hline")
            ligne = ""
            for j in range(nombreColonne):
                ligne += "%s" % contenu[j][i]
                if j != nombreColonne - 1:
                   ligne += "&"
            ligne += "\\\\"
            tex.append(ligne)
        tex.append("\\hline")
        # fin du tableau
        tex.append("\\end{tabular}")
        tex.append("\\end{center}")

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
    cor.append("Le coefficient est \\fbox{%s}" % coefficient)

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
                 nombreCor.append(["%s" % nombre[i],nombre[i]*coefficient])
            else:
                nombreExo.append([nombre[i],"\\ldots"])
                nombreCor.append([nombre[i],"%s" % (nombre[i]*coefficient)])
        else:
            nombreExo.append([nombre[i],nombre[i]*coefficient])
            nombreCor.append([nombre[i],nombre[i]*coefficient])
        
    tex_tableau(exo, nombreExo)
    tex_tableau(cor, nombreCor)
    cor.append("Le coefficient est %s donc" % coefficient)
    cor.append("$$ %s \\times %s = %s $$" % (nombreExo[colonneExo][0], coefficient, nombreExo[colonneExo][1]))    
    cor.append("$$ \\textbf{%s} \\times %s = %s $$" % (nombreCor[colonneExo][0], coefficient, nombreCor[colonneExo][1]))
    cor.append("Le nombre est \\fbox{%s}" % nombreCor[colonneExo][ligneExo])

#---------------Construction--------------------------------
def CalculCoefficient(parametre):
    question = u"Calculer le coefficient de proportionnalité :"
    exo = []
    cor = []
    tex_calcul_coefficient(exo,cor)
    return (exo, cor,question)

def CompleteTableau(parametre):
    question = u"Compléter le tableau de proportionnalité :"
    exo = []
    cor = []
    tex_complete_tableau(exo,cor)
    return (exo, cor,question)
