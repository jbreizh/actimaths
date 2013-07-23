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

#------------------Construction-------------------------
def Oppose(parametre):
    question = u"Donner l'opposé de :"
    exo = []
    cor = []
    nombre = random.randrange(parametre[0],parametre[1])
    oppose = - nombre
    exo.append("$$ %s $$" % nombre)
    cor.append("$$ %s $$"% nombre)
    cor.append(u"L'opposé de $%s$ est $\\boxed{%s}$" % (nombre, oppose))
    return (exo, cor, question)

def Signe(parametre):
    question = u"Donner le signe du nombre :"
    exo = []
    cor = []
    nombre = random.randrange(parametre[0],parametre[1])
    exo.append("$$ %s $$" % nombre)
    cor.append("$$ %s $$"% nombre)
    if nombre == 0:
        cor.append(u"Le nombre $%s$ est \\textbf{positif} ou \\textbf{négatif}" % nombre )
    elif nombre > 0:
        cor.append(u"Le nombre $%s$ est \\textbf{positif}" % nombre )
    else:
        cor.append(u"Le nombre $%s$ est \\textbf{négatif}" % nombre )
    return (exo, cor, question)
