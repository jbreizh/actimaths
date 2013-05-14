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
from math import log10, floor
import string

#------------------------------------------------------------------------------
#  Écritures scientifiques
#------------------------------------------------------------------------------


def val_sc():
    while True:
        a = randrange(10) * 1000 + randrange(10) + randrange(10) * 10 ** \
            (randrange(2) + 1)
        a = a * 10 ** randrange(-5, 5)

        if a >= 10 or (a < 1 and a >0) :
            break
    return a


def ecritureScientifique(parametre):
    question = u"Compléter l\'écriture scientifique :"
    exo = [ ]
    cor = [ ]
    a = val_sc()
    exp = int(floor(log10(a)))
    a_sc = (a * 1.) / 10 ** exp
    s_a = decimaux(a, 1)
    s_a_sc = decimaux(a_sc, 1)
    if randrange(2):  # forme : a=a_sc*...
        exo.append("$$%s=%s\\times\\ldots$$" % (s_a, s_a_sc))
        cor.append("$$%s=%s\\times\\mathbf{10^{%s}}$$" % (s_a, s_a_sc, decimaux(exp, 1)))
    else:  # forme : a_sc*...=a
        exo.append("$$%s\\times\\ldots=%s$$" % (s_a_sc, s_a))
        cor.append("$$%s\\times\\mathbf{10^{%s}}=%s$$" % (s_a_sc, decimaux(exp, 1), s_a))
    return (exo, cor, question)
