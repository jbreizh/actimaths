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

from outils.Arithmetique import pgcd, valeur_alea
from outils.Affichage import decimaux, tex_coef
from random import choice, randrange
import string


def tex_proprietes_val(exp_max, nb_max, type):
    """
    Renvoie des valeurs pour l'exercice sur les propriétés des puissances
    @param exp_max: valeur maximale pour les exposants
    @type exp_max: Integer
    @param nb_max: Valeur maximale pour les nombres
    @type nb_max: integer
    @param type: 0 : 2 exposants et 1 nombre ; 1 : 1 exposant et 2 nombres
    @type type: integer
    """

    if type:
        while 1:
            nb1 = randrange(2, nb_max)
            nb2 = randrange(2, nb_max)
            exp1 = randrange(2, exp_max)
            exp2 = exp1
            if nb1 != nb2:
                break
    else:
        while 1:
            nb1 = randrange(2, nb_max)
            nb2 = nb1
            exp1 = randrange(2, exp_max)
            exp2 = randrange(2, exp_max)
            if exp1 != exp2:
                break
    return (nb1, exp1, nb2, exp2)


def produitNombreIdentique(parametre):
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 0)
    exo.append("$$%s^{%s}\\times%s^{%s}=\\ldots$$" % lval)
    cor.append("$$%s^{%s}\\times%s^{%s}=" % lval)
    cor.append("%s^{%s}$$" % (lval[0], lval[1] + lval[3]))
    return (exo, cor, question)

def produitExposantIdentique(parametre):
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 1)
    exo.append("$$%s^{%s}\\times%s^{%s}=\\ldots$$" % lval)
    cor.append("$$%s^{%s}\\times%s^{%s}=" % lval)
    cor.append("%s^{%s}$$" % (lval[0] * lval[2], lval[1]))
    return (exo, cor, question)

def quotient(parametre): 
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 0)
    exo.append("$$\\dfrac{%s^{%s}}{%s^{%s}}=\\ldots$$" % lval)
    cor.append("$$\\dfrac{%s^{%s}}{%s^{%s}}=" % lval)
    cor.append("%s^{%s}$$" % (lval[0], lval[1] - lval[3]))
    return (exo, cor, question)

def puissance(parametre):
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 0)
    exo.append("$$(%s^{%s})^{%s}=\\ldots$$" % (lval[0], lval[1], lval[3]))
    cor.append("$$(%s^{%s})^{%s}=" % (lval[0], lval[1], lval[3]))
    cor.append("%s^{%s}$$" % (lval[0], lval[1] * lval[3]))
    return (exo, cor, question)


def produitDix(parametre):
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 0)
    exo.append("$$10^{%s}\\times10^{%s}=\\ldots$$" % (lval[1], lval[3]))
    cor.append("$$10^{%s}\\times10^{%s}=" % (lval[1], lval[3]))
    cor.append("10^{%s}$$" % (lval[1] + lval[3]))
    return (exo, cor, question)

def quotientDix(parametre): 
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 0)
    exo.append("$$\\dfrac{10^{%s}}{10^{%s}}=\\ldots$$" % (lval[1], lval[3]))
    cor.append("$$\\dfrac{10^{%s}}{10^{%s}}=" % (lval[1], lval[3]))
    cor.append("10^{%s}$$" % (lval[1] - lval[3]))
    return (exo, cor, question)

def puissanceDix(parametre):
    question = u"Compléter par $a^n$ ($a$ et $n$ entiers):"
    exo = [ ]
    cor = [ ]
    lval = tex_proprietes_val(12, 12, 0)
    exo.append("$$(10^{%s})^{%s}=\\ldots$$" % (lval[1], lval[3]))
    cor.append("$$(10^{%s})^{%s}=" % (lval[1], lval[3]))
    cor.append("10^{%s}$$" % (lval[1] * lval[3]))
    return (exo, cor, question)
