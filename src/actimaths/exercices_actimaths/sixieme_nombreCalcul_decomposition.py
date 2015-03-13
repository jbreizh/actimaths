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
from outils import Affichage, Arithmetique

#===============================================================================
#    Décomposition des nombres décimaux
#===============================================================================

#
##------------------VALEURS--------------------------------------------------
def valeurs_dec(rang_partie_decimal, rang_partie_entier):
    liste_puissances = range(rang_partie_decimal, rang_partie_entier)
    puissances = []
    chiffres = []
    longueur = min(3,len(liste_puissances))
    nombre = 0
    for i in range(longueur):
        puissances.append(liste_puissances.pop(random.randrange(len(liste_puissances))))
        chiffres.append(random.randrange(1, 10))
        nombre += chiffres[i] * 10 ** puissances[i]
    return (chiffres, puissances, longueur, nombre)

#
##------------------AFFICHAGE--------------------------------------------------
def tex_composition(exo, cor, chiffres, puissances, longueur, nombre):
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("$")
    cor.append("$")
    for i in range(longueur):
        if puissances[i] < 0:
            exo.append("%s\\times \\cfrac{1}{%s}" % (chiffres[i], Affichage.decimaux(10 ** (-puissances[i]), 1)))
            cor.append("%s\\times \\cfrac{1}{%s}" % (chiffres[i], Affichage.decimaux(10 ** (-puissances[i]), 1)))
        else:
            exo.append("%s\\times %s" % (chiffres[i], Affichage.decimaux(10 ** puissances[i], 1)))
            cor.append("%s\\times %s" % (chiffres[i], Affichage.decimaux(10 ** puissances[i], 1)))
        if i < longueur-1:
            exo.append("+")
            cor.append("+")
        else:
            exo.append("=")
            cor.append("=")
    exo.append("\\ldots$")
    cor.append("\\boxed{%s}$" % Affichage.decimaux(nombre, 1))
    exo.append("\\end{center}")
    cor.append("\\end{center}")

def tex_decomposition(exo, cor, chiffres, puissances, longueur, nombre):
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("$ %s = \\ldots $" % Affichage.decimaux(nombre, 1))
    cor.append("$ %s = \\boxed{" % Affichage.decimaux(nombre, 1))
    for i in range(longueur):
        if puissances[i] < 0:
            cor.append("%s\\times \\cfrac{1}{%s}" % (chiffres[i], Affichage.decimaux(10 ** (-puissances[i]), 1)))
        else:
            cor.append("%s\\times %s" % (chiffres[i], Affichage.decimaux(10 ** puissances[i], 1)))
        if i < longueur-1:
            cor.append("+")
    cor.append("}$")
    exo.append("\\end{center}")
    cor.append("\\end{center}")

#
##---------------------CONSTRUCTION----------------------------------------------
def Composition(parametre):
    question = u"Compléter avec un nombre décimal :"
    exo = []
    cor = []
    (chiffres, puissances, longueur, nombre) = valeurs_dec(parametre[0], parametre[1])
    tex_composition(exo, cor, chiffres, puissances, longueur, nombre)
    return (exo, cor, question)

def Decomposition(parametre):
    question = u"Compléter avec la décomposition :"
    exo = []
    cor = []
    (chiffres, puissances, longueur, nombre) = valeurs_dec(parametre[0], parametre[1])
    tex_decomposition(exo, cor, chiffres, puissances, longueur, nombre)
    return (exo, cor, question)
