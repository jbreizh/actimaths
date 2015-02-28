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
from outils.Affichage import tex_coef, tex_binome, is_int
lettre = "abcdfghkmnpqrstuvwxyz"
    
def solveur(enonce,equation,inconnue,corrige=False):
    enonce.append("\\begin{center}")
    enonce.append("$\\begin{aligned}")
    enonce.append("%s & = %s \\\\" %(tex_binome(equation[:2],inconnue),tex_binome(equation[2:],inconnue)))
    if corrige:
        if equation[1]!=0:
            enonce.append("%s & = %s \\red %s \\\\" %(tex_coef(equation[0],inconnue),tex_binome([equation[2],equation[3]],inconnue),tex_coef(-equation[1],0,1)))
            if equation[2]!=0 and equation[0]!=1:
                enonce.append("%s & = %s \\\\" %(tex_coef(equation[0],inconnue),tex_binome([equation[2],equation[3]-equation[1]],inconnue)))
        if equation[2]!=0:
            enonce.append("%s \\red %s \\black & = %s \\\\" %(tex_coef(equation[0],inconnue),tex_coef(-equation[2],inconnue,1),tex_coef(equation[3]-equation[1],0)))
            enonce.append("%s & = %s \\\\" %(tex_coef(equation[0]-equation[2],inconnue),tex_coef(equation[3]-equation[1],0)))
        if (equation[0]-equation[2])!=1:
            enonce.append("%s & = %s \\div \\red %s \\\\" %(inconnue,tex_coef(equation[3]-equation[1],0),tex_coef(equation[0]-equation[2],0,0,1)))
        if float(equation[3]-equation[1])/(equation[0]-equation[2]) != (equation[3]-equation[1])/(equation[0]-equation[2]):
            enonce.append("%s & \\approx \\boxed{%s} \\\\" %(inconnue,round(float(equation[3]-equation[1])/(equation[0]-equation[2]),2)))
        else:
            enonce.append("%s & = \\boxed{%s} \\\\" %(inconnue,(equation[3]-equation[1])/(equation[0]-equation[2])))
    enonce.append("\\end{aligned}$")
    enonce.append("\\end{center}")

def BiTerme(parametre):
    ## initialisation
    question = u"Résoudre l'équation :"
    exo = [ ]
    cor = [ ]
    ## parametres
    inconnue = lettre[random.randrange(len(lettre))]
    equation = [random.randrange(parametre[0],parametre[1]),0,0,random.randrange(parametre[0],parametre[1])]
    while equation[0]==0 or equation[0]==1 or equation[3]==0:
        equation = [random.randrange(parametre[0],parametre[1]),0,0,random.randrange(parametre[0],parametre[1])]
    ## redaction
    solveur(exo,equation,inconnue)
    solveur(cor,equation,inconnue,True)
    return (exo, cor, question)

def TriTerme(parametre):
    ## initialisation
    question = u"Résoudre l'équation :"
    exo = [ ]
    cor = [ ]
    ## parametres
    inconnue = lettre[random.randrange(len(lettre))]
    equation = [1,random.randrange(parametre[0],parametre[1]),0,random.randrange(parametre[0],parametre[1])]
    while equation[1]==0 or equation[3]==0 or (equation[3]-equation[1])==0:
        equation = [1,random.randrange(parametre[0],parametre[1]),0,random.randrange(parametre[0],parametre[1])]
    ## redaction
    solveur(exo,equation,inconnue)
    solveur(cor,equation,inconnue,True)
    return (exo, cor, question)

def QuadriTerme(parametre):
    ## initialisation
    question = u"Résoudre l'équation :"
    exo = [ ]
    cor = [ ]
    ## parametres
    inconnue = lettre[random.randrange(len(lettre))]
    equation = [random.randrange(parametre[0],parametre[1]),random.randrange(parametre[0],parametre[1]),random.randrange(parametre[0],parametre[1]),random.randrange(parametre[0],parametre[1])]
    while equation[0]==0 or equation[1]==0 or equation[2]==0 or equation[3]==0 or (equation[0]-equation[2])==0 or (equation[3]-equation[1])==0:
        equation = [random.randrange(parametre[0],parametre[1]),random.randrange(parametre[0],parametre[1]),random.randrange(parametre[0],parametre[1]),random.randrange(parametre[0],parametre[1])]
    ## redaction
    solveur(exo,equation,inconnue)
    solveur(cor,equation,inconnue,True)
    return (exo, cor, question)
