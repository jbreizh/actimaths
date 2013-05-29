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
from outils import Arithmetique

def donne():
    a = b = 1
    while a == b:
        a = random.randrange(1, 11)
        b = random.randrange(2, 11)
    c = random.randrange(1, 6)
    enonce = [a,b,b*c,"\\ldots"]
    solution = [a,b,b*c,"\\mathbf{%s}" % (a*c)]
    return enonce,solution

def donne_vocabulaire():
    fraction = [u"demi", "tiers", "quarts", u"cinquièmes", u"sixièmes", u"septièmes", u"huitièmes", u"neuvièmes", u"dixièmes"]
    a = b = 1
    while a == b:
        a = random.randrange(2, 11)
        b = random.randrange(2, 11)
    c = random.randrange(1, 6)
    enonce = [a,fraction[b-2],b*c,"\\ldots"]
    solution1 = [a,fraction[b-2],b*c,"\\textbf{%s}" % (a*c)]
    solution2 = [a,b,b*c,"\\ldots"]
    solution3 = [a,b,b*c,"\\mathbf{%s}" % (a*c)]
    return enonce,solution1,solution2,solution3

def donne_complement():
    a = b = 1
    while a == b:
        a = random.randrange(1, 11)
        b = random.randrange(2, 11)
    c = random.randrange(1, 6)
    trou = random.randrange(4)
    enonce = [a,b,b*c,a*c]
    solution = [a,b,b*c,a*c]
    enonce[trou] = "\\ldots"
    solution[trou] = "\\mathbf{%s}" % solution[trou]
    return enonce,solution

def FractionQuantite(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (enonce,solution) = donne()
    exo.append("$$\\dfrac{%s}{%s} \\times %s = %s $$" % tuple(enonce))
    cor.append("$$\\dfrac{%s}{%s} \\times %s = %s $$" % tuple(solution))
    return (exo, cor, question)


def VocubulaireFractionQuantite(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (enonce,solution1,solution2,solution3) = donne_vocabulaire()
    exo.append("%s %s de %s valent %s" % tuple(enonce))
    cor.append("%s %s de %s valent %s" % tuple(solution1))
    cor.append("$$\\dfrac{%s}{%s} \\times %s = %s $$" % tuple(solution2))
    cor.append("$$\\dfrac{%s}{%s} \\times %s = %s $$" % tuple(solution3)) 
    return (exo, cor, question)

def ComplementFractionQuantite(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (enonce,solution) = donne_complement()
    exo.append("$$\\dfrac{%s}{%s} \\times %s = %s $$" % tuple(enonce))
    cor.append("$$\\dfrac{%s}{%s} \\times %s = %s $$" % tuple(solution))
    return (exo, cor, question)
