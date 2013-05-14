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

from outils.Arithmetique import valeur_alea, signe, pgcd
from outils.Affichage import tex_coef, tex_binome, tex_dev0
import random

#
# ------------------- DIVERS -------------------

variable_list = ['x', 'y', 'a', 'b', 'k', 'm', 'p']

def simplifie(a):  #renvoie la fraction a simplifiee
    b = pgcd(a[0], a[1])
    if b != 1:
        return (a[0] // b, a[1] // b)
    else:
        return ''


def tex_frac(a):  #renvoie l'ecriture au format tex de la fraction a
    if not isinstance(a, tuple):
        return ''
    else:
        a = ((a[0] * a[1]) // abs(a[1]), abs(a[1]))
        if a[1] == 1:
            if abs(a[1]) >= 1000:
                return '\\nombre{%i}' % a[0]
            else:
                return '%i' % a[0]
        else:
            if abs(a[0]) >= 1000:
                if abs(a[1]) >= 1000:
                    return '\\frac{\\nombre{%s}}{\\nombre{%s}}' % a
                else:
                    return '\\frac{\\nombre{%s}}{%s}' % a
            elif abs(a[1]) >= 1000:
                return '\\frac{%s}{\\nombre{%s}}' % a
            else:
                return '\\frac{%s}{%s}' % a

#
# ------------------- AFFICHAGE -------------------

def tex_equations(valeurs, variable, cor):  # renvoie un tuple contenant les deux binomes egaux a 0
    cor.append('$$ %s=0 \\text{ ou } %s=0 $$' % (tex_binome(valeurs[0], variable), tex_binome(valeurs[1], variable)))
    eq = equations1(valeurs)
    if not isinstance(eq, tuple):
        cor.append("\\fbox{Aucune solution.}")
    elif not isinstance(eq[0], tuple):
        cor.append('$$ %s=%s $$' % (tex_coef(eq[1][0], variable), eq[1][1]))
        if eq[1][0] != 1:
            cor.append('$$ x=%s $$' % tex_frac(equations2(eq)[1]))
        cor.append(u'La solution est $\\boxed{%s}$' % tex_frac(equations3(eq)[1]))
    elif not isinstance(eq[1], tuple):
        cor.append('$$ %s=%s $$' % (tex_coef(eq[0][0], variable), eq[0][1]))
        if eq[0][0] != 1:
            cor.append('$$ x=%s $$' % tex_frac(equations2(eq)[0]))
        cor.append(u'La solution est $\\boxed{%s}$' % tex_frac(equations3(eq)[0]))
    else:
        cor.append('$$ %s=%s \\text{ ou } %s=%s $$' % (tex_coef(eq[0][0], variable), eq[0][1], tex_coef(eq[1][0], variable), eq[1][1]))
        if eq[0][0] != 1 or eq[1][0] != 1:
            cor.append('$$ x=%s \\text{ ou } x=%s $$' % (tex_frac(equations2(eq)[0]), tex_frac(equations2(eq)[1])))
        cor.append(u'Les solutions sont $\\boxed{%s\\,\\text{ et }\\,%s}$' % (tex_frac(equations3(eq)[0]), tex_frac(equations3(eq)[1])))


def equations1(a):  #renvoie ((9,5),(3,-7)) pour pouvoir ecrire 9x=5 ou 3x=-7
    if a[0][0] == 0:
        if a[1][0] == 0:
            return ''
        else:
            return ('', (a[1][0], -a[1][1]))
    elif a[1][0] == 0:
        return ((a[0][0], -a[0][1]), '')
    else:
        return ((a[0][0], -a[0][1]), (a[1][0], -a[1][1]))


def equations2(a):  # renvoie ((5,9),(-7,3)) pour pouvoir ecrire x=5/9 ou x=-7/3
    if not isinstance(a, tuple):
        return ''
    elif not isinstance(a[0], tuple):
        return ('', (a[1][1], a[1][0]))
    elif not isinstance(a[1], tuple):
        return ((a[0][1], a[0][0]), '')
    else:
        return ((a[0][1], a[0][0]), (a[1][1], a[1][0]))


def equations3(a):  # renvoie les solutions éventuellement simplifiée
    a = equations2(a)
    if not isinstance(a, tuple):
        return ''
    elif not isinstance(a[0], tuple):
        if simplifie(a[1]):
            return ('', simplifie(a[1]))
        else:
            return a
    elif not isinstance(a[1], tuple):
        if simplifie(a[0]):
            return (simplifie(a[0]), '')
        else:
            return a
    else:
        if simplifie(a[0]):
            if simplifie(a[1]):
                return (simplifie(a[0]), simplifie(a[1]))
            else:
                return (simplifie(a[0]), a[1])
        elif simplifie(a[1]):
            return (a[0], simplifie(a[1]))
        else:
            return a

#
# ------------------- GENERATION DES VALEURS -------------------

def valeurs_equation(nombre_min, nombre_max):  # renvoie in tuple contenant ((a,b),(c,d)) avec a != c ou b != d (en valeur absolue)
    a = valeur_alea(nombre_min, nombre_max)
    b = valeur_alea(nombre_min, nombre_max)
    c = valeur_alea(nombre_min, nombre_max)
    d = valeur_alea(nombre_min, nombre_max)
    while abs(a) == abs(c) and abs(b) == abs(d):
        c = valeur_alea(nombre_min, nombre_max)
        d = valeur_alea(nombre_min, nombre_max)
    return ((a, b), (c, d))

#
# ------------------- CONSTRUCTION -------------------

def Produit(parametre):
    question = u"Résoudre l'équation"
    exo = []
    cor = []
    valeurs = valeurs_equation(parametre[0], parametre[1])
    variable = variable_list[ random.randrange(7) ]
    exo.append(u"$$ %s = 0 $$" % tex_dev0(valeurs, variable))
    cor.append(u"$$ %s = 0 $$" % tex_dev0(valeurs, variable))
    tex_equations(valeurs, variable, cor)
    return (exo, cor, question)
