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

from outils.Priorites3 import texify, priorites
import random

#----------------------------------------------------------------------
# Simple
#----------------------------------------------------------------------

def valeurs_reduire(op):
    """Travail sur les bases du calcul littéral en quatrième"""
    var = "abcdfghkmnpqrstuvwxyz"
    var = var[random.randrange(len(var))]
    if op == "*":
        deg1 = random.randrange(3)
        if deg1 == 2: deg2=0
        elif deg1 == 1: deg2 = random.randrange(2)
        else: deg2 = random.randrange(1, 3)
    else:
        deg1 = random.randrange(1, 3)
        deg2 = [i for i in range(3)]
        deg2.extend([deg1]*7)
        random.shuffle(deg2)
        deg2 = deg2.pop(random.randrange(len(deg2)))
    a1, a2 = 0, 0
    while not a1 or not a2:
        a1 = random.randrange(-10, 11)
        a2 = random.randrange(-10, 11)
    p1 = "Polynome(\"%s%s^%s\")" % (a1, var, deg1)
    p2 = "Polynome(\"%s%s^%s\")" % (a2, var, deg2)
    return p1 + op + p2


def somme(parametre):
    question = u"Réduire :"
    exo = [ ]
    cor = [ ]
    a = valeurs_reduire('+')
    solve = [a]
    exo.append("$$A = " + texify(solve)[0] + "$$")
    cor.append("$$A = " + texify(solve)[0] + "$$")
    solve = priorites(a)
    solve.insert(0, a)
    solve = texify(solve)
    if len(solve)>1:
        for e in solve[1:]:
            cor.append("$$A = "  + e + "$$")
    return (exo, cor,question)

def produit(parametre):
    question = u"Réduire :"
    exo = [ ]
    cor = [ ]
    a = valeurs_reduire('*')
    solve = [a]
    exo.append("$$A = " + texify(solve)[0] + "$$")
    cor.append("$$A = " + texify(solve)[0] + "$$")
    solve = priorites(a)
    solve.insert(0, a)
    solve = texify(solve)
    if len(solve)>1:
        for e in solve[1:]:
            cor.append("$$A = "  + e + "$$")
    return (exo, cor, question)

#----------------------------------------------------------------------
# Expression
#----------------------------------------------------------------------


def valeurs_reduire_somme():
    """Réduire une somme de six monômes de degrés 0, 1 et 2"""
    import random
    var = "abcdfghkmnpqrstuvwxyz"
    var = var[random.randrange(len(var))]
    l=[]
    for i in range(3):
        a = 0
        degre = i//2
        while not a:
            a = random.randrange(-10, 11)
        l.append("Polynome(\"%s%s^%s\")" % (a, var, degre))
    random.shuffle(l)
    t = l[0]
    for i in range(1, len(l)):
        t += "+-"[random.randrange(2)] + l[i]
    return t

def valeurs_reduire_prod():
    """Réduire une expression de six monômes de degrés 0, 1 et 2"""
    import random
    var = "abcdfghkmnpqrstuvwxyz"
    var = var[random.randrange(len(var))]
    l=[]
    for i in range(3):
        a = 0
        degre = i//2
        while not a:
            a = random.randrange(-10, 11)
        l.append("Polynome(\"%s%s^%s\")" % (a, var, degre))
    random.shuffle(l)
    t = l[0]
    for i in range(1, len(l)):
        t += "*" + l[i]
    return t

def valeurs_reduire_sommeprod():
    """Réduire une expression de six monômes de degrés 0, 1 et 2"""
    import random
    var = "abcdfghkmnpqrstuvwxyz"
    var = var[random.randrange(len(var))]
    l=[]
    for i in range(3):
        a = 0
        degre = i//2
        while not a:
            a = random.randrange(-10, 11)
        l.append("Polynome(\"%s%s^%s\")" % (a, var, degre))
    random.shuffle(l)
    t = l[0]+ "+-"[random.randrange(2)]+ l[1] + "*" + l[2]
    return t

def expressionSomme(parametre):
    question = u"Réduire :"
    exo = [ ]
    cor = [ ]
    a = valeurs_reduire_somme()
    solve = [a]
    exo.append("$$A = " + texify(solve)[0] + "$$")
    cor.append("$$A = " + texify(solve)[0] + "$$")
    solve = priorites(a)
    solve.insert(0, a)
    solve = texify(solve)
    if len(solve)>1:
        for e in solve[1:]:
            cor.append("$$A = "  + e + "$$")
    return (exo, cor,question)

def expressionProduit(parametre):
    question = u"Réduire :"
    exo = [ ]
    cor = [ ]
    a = valeurs_reduire_prod()
    solve = [a]
    exo.append("$$A = " + texify(solve)[0] + "$$")
    cor.append("$$A = " + texify(solve)[0] + "$$")
    solve = priorites(a)
    solve.insert(0, a)
    solve = texify(solve)
    if len(solve)>1:
        for e in solve[1:]:
            cor.append("$$A = "  + e + "$$")
    return (exo, cor, question)

def expressionSommeProduit(parametre):
    question = u"Développer et réduire :"
    exo = [ ]
    cor = [ ]
    a = valeurs_reduire_sommeprod()
    solve = [a]
    exo.append("$$A = " + texify(solve)[0] + "$$")
    cor.append("$$A = " + texify(solve)[0] + "$$")
    solve = priorites(a)
    solve.insert(0, a)
    solve = texify(solve)
    if len(solve)>1:
        for e in solve[1:]:
            cor.append("$$A = "  + e + "$$")
    return (exo, cor, question)
