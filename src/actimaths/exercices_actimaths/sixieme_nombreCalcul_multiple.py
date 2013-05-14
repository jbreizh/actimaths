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

def valeurs_diviseurs():
    diviseurs = [2, 3, 5, 9, 10]
    liste = diviseurs.pop(random.randrange(len(diviseurs))) * random.randrange(11, 100)
    return liste


def liste_diviseurs(l):
    diviseurs = (2, 3, 5, 9, 10)
    reponse = [l]
    for j in range(len(diviseurs)):
        if l % diviseurs[j]:  # n'est pas divisible
            reponse.append("$\\Square$")
        else:
            reponse.append("$\\CheckedBox$")
    return reponse


def Divisible(parametre):
    question = u"Choisir les bonnes réponses :"
    exo = [ ]
    cor = [ ]
    l = valeurs_diviseurs()
    reponse = liste_diviseurs(l)
    exo.append("%s est divisible : \\newline $\\square$ par 2 \\newline $\\square$ par 3 \\newline $\\square$ par 5 \\newline $\\square$ par 9 \\newline $\\square$ par 10 \\newline" % l)
    cor.append("%s est divisible : \\newline %s par 2 \\newline %s par 3 \\newline %s par 5 \\newline %s par 9 \\newline %s par 10 \\newline" % tuple(reponse))
    return (exo, cor,question)
