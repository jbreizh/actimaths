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


def valeurs_dec():
    lpuissances = [3, 2, 1, 0, -1, -2, -3]
    p = []
    v = []
    for i in range(3):
        p.append(lpuissances.pop(random.randrange(len(lpuissances))))
        v.append(random.randrange(1, 10))
    return (v, p)


def tex_decomposition(v, p):
    (exo, cor) = (["$$"], ["$$"])
    for i in range(3):
        if p[i] < 0:
            exo.append('%s\\times \\cfrac{1}{%s}' % (v[i], Affichage.decimaux(10 ** (-p[i]), 1)))
            cor.append('%s\\times \\cfrac{1}{%s}' % (v[i], Affichage.decimaux(10 ** (-p[i]), 1)))
        else:
            exo.append('%s\\times %s' % (v[i], Affichage.decimaux(10 ** p[i], 1)))
            cor.append('%s\\times %s' % (v[i], Affichage.decimaux(10 ** p[i], 1)))
        if i < 2:
            exo.append('+')
            cor.append('+')
        else:
            exo.append('=')
            cor.append('=')
    exo.append('$$')
    cor.append('%s$$' % Affichage.decimaux(v[0] * 10 ** p[0] + v[1] * 10 ** p[1] + v[2] * 10 ** p[2], 1))
    return " ".join(exo), " ".join(cor)


def Decomposition(parametre):
    question = u"Compléter avec un nombre décimal :"
    exo = []
    cor = []
    (chiffres, puissances) = valeurs_dec()
    (txt_exo, txt_cor) = tex_decomposition(chiffres, puissances)
    exo.append(txt_exo)
    cor.append(txt_cor)
    return (exo, cor, question)
