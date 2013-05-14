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
from outils import Arithmetique

#
##---------------------Valeurs-----------------------
def valeurs(nombre_min, nombre_max, carre_parfait, non_simplifiable):
    iteration = 0
    while True:
        # generation d'un nombre entre nombre_min et nombre_max
        nombre = random.randrange(nombre_min, nombre_max)
        # decomposition en facteur premier
        decomposition = Arithmetique.factor(nombre)
        compte = [(k, decomposition.count(k)) for k in set( decomposition)]
        # les facteurs qui apparaissent 2 fois forment le carré, les autres sont le coefficient   
        (coefficient, carre) = (1, 1)
        for i in range(len(compte)):
            coefficient = coefficient * compte[i][0] ** (compte[i][1] % 2)
            carre = carre * compte[i][0] ** (compte[i][1] / 2)
        #Choix
        if carre_parfait == 1 and non_simplifiable == 0 and coefficient == 1:
            break
        if carre_parfait == 0 and non_simplifiable == 1 and carre == 1:
            break
        if carre_parfait == 0 and non_simplifiable == 0 and coefficient != 1 and carre != 1:
            break
        # Controle du bouclage si l'utilisateur fait un choix de valeur min et max absurde
        if iteration > 10000:
            (coefficient, carre) = (0, 0)
            break
    return coefficient, carre

#
##--------------------Construction-------------------
def CarreParfait(parametre):
    question = u"Calculer :"
    exo = []
    cor = []
    (coefficient, carre) = valeurs(parametre[0], parametre[1], 1, 0)
    exo.append("$$ A= \\sqrt{%s}$$" % (carre*carre))
    cor.append("$$ A= \\sqrt{%s} = \\boxed{ %s } $$" % (carre*carre, carre))
    return (exo, cor, question)

def Simplifier(parametre):
    question = "Simplifier :"
    exo = []
    cor = []
    (coefficient, carre) = valeurs(parametre[0], parametre[1], 0, 0)
    exo.append("$$ A= \\sqrt{ %s } $$" % (coefficient * carre ** 2 ))
    cor.append("$$ A= \\sqrt{ %s } $$" % (coefficient * carre ** 2))
    cor.append("$$ A= \\sqrt{ %s \\times %s } $$" % (carre ** 2, coefficient))
    cor.append("$$ A= \\sqrt{ %s^2 \\times %s } $$" % (carre, coefficient))
    cor.append("$$ A= \\sqrt{ %s^2 } \\times \\sqrt{ %s } $$" % (carre, coefficient))
    cor.append("$$ A= \\boxed{ %s \\sqrt{ %s } } $$" % (carre, coefficient))
    return (exo, cor, question)
