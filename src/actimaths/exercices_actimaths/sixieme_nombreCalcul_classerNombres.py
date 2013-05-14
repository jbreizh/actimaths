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
# Classer des nombres dans l'ordre
#===============================================================================
def choix_nombres():
    nb = []
    unite = random.randrange(10)
    for i in range(3):
        n = unite
        for j in range(i + 1):
            n = n + random.randrange(1, 10) * 10 ** (-(j + 1))
        nb.append(n)
    n = random.randrange(10) + random.randrange(10) / 10.0
    while n == nb[0]:
        n = random.randrange(10) + random.randrange(10) / 10.0
    nb.append(n)
    return nb


def ClasserNombres(parametre):
    # Choix de l'ordre
    if random.randrange(2):
        ordre = "croissant"
    else:
        ordre = u"décroissant"
    # Entête
    question = "Classer dans l'ordre %s :" % ordre
    exo = []
    cor = []
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    lnb = choix_nombres()
    random.shuffle(lnb)
    str=""
    for i in range(len(lnb)):
        if i:
            str += " || "
        str += Affichage.decimaux(lnb[i], 0)
    exo.append(str)

    lnb.sort()
    if ordre == "croissant" or ordre == "\\textless":
        ordre = "\\textless"
    else:
        ordre = "\\textgreater"
        lnb.reverse()
    str=""
    for i in range(len(lnb)):
        if i:
            str +=" %s " % ordre
        str += Affichage.decimaux(lnb[i], 0)

    cor.append(str)
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor, question)
