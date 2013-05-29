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

from outils.Fractions import Fractions  #Fractions de pyromaths
import random
import string
from outils.Arithmetique import valeur_alea


def Fraction(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    #Génération des nombres
    n = d = 1
    while n == d:
        n = valeur_alea(parametre[0], parametre[1])
        d = valeur_alea(parametre[0], parametre[1])
    c = random.randrange(2, 11)
    #Construction
    cas = random.randrange(2)
    if cas:
        enonce = [n, d, n * c, d * c]
        solution = [n, d, n * c, d * c]
    else:
        enonce = [n * c, d * c, n, d]
        solution = [n * c, d * c, n, d]
    trou = random.randrange(4)
    enonce[trou] = "\\ldots"
    solution[trou] = "\\mathbf{%s}" % solution[trou]
    if cas:
        solution.insert(2, c)
        solution.insert(1, c)
    else:
        solution.insert(4, c)
        solution.insert(3, c)
    #Affichage
    exo.append("$$\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$$" % tuple(enonce))
    if cas:
        cor.append("$$\\dfrac{%s_{(\\times %s)}}{%s_{(\\times %s)}}=\\dfrac{%s}{%s}$$" % tuple(solution))
    else:
        cor.append("$$\\dfrac{%s}{%s}=\\dfrac{%s_{(\\times %s)}}{%s_{(\\times %s)}}$$" % tuple(solution))
    return (exo, cor, question)
