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

def valeurs_produit(nombre_min, nombre_max):
    iteration = 0
    while True:
        # generation de 2 nombres entre nombre_min et nombre_max
        nombre1 = random.randrange(nombre_min, nombre_max)
        nombre2 = random.randrange(nombre_min, nombre_max)
        # decomposition en facteur premier du produit des 2 nombres
        decomposition = Arithmetique.factor(nombre1*nombre2)
        compte = [(k, decomposition.count(k)) for k in set( decomposition)]
        # les facteurs qui apparaissent 2 fois forment le carré, les autres sont le coefficient   
        (coefficient, carre) = (1, 1)
        for i in range(len(compte)):
            coefficient = coefficient * compte[i][0] ** (compte[i][1] % 2)
            carre = carre * compte[i][0] ** (compte[i][1] / 2)
        #Choix
        if coefficient != 1 and carre != 1:
            break  
        # Controle du bouclage si l'utilisateur fait un choix de valeur min et max absurde
        if iteration > 10000:
            (nombre1, nombre2, coefficient, carre, decomposition) = (0, 0, 0, 0, 0)
            break 
    return nombre1, nombre2, coefficient, carre, decomposition


def valeurs_addition(nombre_min, nombre_max):
    iteration = 0
    while True:
        # generation de 2 entiers simplifiable entre nombre_min et nombre_max
        (coefficient1, carre1) = valeurs(nombre_min, nombre_max, 0, 0)
        (coefficient2, carre2) = valeurs(nombre_min, nombre_max, 0, 0)
        # on regenère l'entier 2 jusqu'a ce qu'il ai le même coefficient et qu'il soit différent que l'entier 1
        compteur = 0
        while True:
            iteration += 1
            (coefficient2, carre2) = valeurs(nombre_min, nombre_max, 0, 0)
            if coefficient2 == coefficient1 and carre1 != carre2:
                break
            # si on dépasse 50 itérations sans trouver, c'est surement impossible
            compteur += 1
            if compteur > 50:
                break
        if coefficient2 == coefficient1 and carre1 != carre2:
            break
        # Controle du bouclage si l'utilisateur fait un choix de valeur min et max absurde
        if iteration > 10000:
            (coefficient1, carre1, coefficient2, carre2) = (0, 0, 0, 0)
            break
    return coefficient1, carre1, coefficient2, carre2
#
##--------------------Affichage-------------------
def tex_produit(facteurs):
    """Affiche sous forme de produit les éléments d'une liste."""
    prodfacteurs = ''
    for element in facteurs:
        prodfacteurs += str(element) + ' \\times '
    return prodfacteurs[:-7]
#
##--------------------Construction-------------------

def Addition(parametre):
    question = u"Calculer et simplifier :"
    exo = []
    cor = []
    (coefficient1, carre1, coefficient2, carre2) = valeurs_addition(parametre[0], parametre[1])
    exo.append("$$ A = \\sqrt{%s} + \\sqrt{%s} $$" % (coefficient1 *  carre1 ** 2, coefficient2 *  carre2 ** 2))
    cor.append("$$ A = \\sqrt{%s} + \\sqrt{%s} $$" % (coefficient1 *  carre1 ** 2, coefficient2 *  carre2 ** 2))
    cor.append("$$ A = \\sqrt{%s \\times %s} + \\sqrt{%s \\times %s} $$" % (carre1 ** 2, coefficient1, carre2 ** 2, coefficient2))
    cor.append("$$ A = \\sqrt{%s} \\times \\sqrt{%s} + \\sqrt{%s} \\times \\sqrt{%s} $$" % (carre1 ** 2, coefficient1, carre2 ** 2, coefficient2))
    cor.append("$$ A = \\sqrt{%s^2} \\times \\sqrt{%s} + \\sqrt{%s^2} \\times \\sqrt{%s} $$" % (carre1, coefficient1, carre2, coefficient2))
    cor.append("$$ A = %s \\times \\sqrt{%s} + %s \\times \\sqrt{%s} $$" % (carre1, coefficient1, carre2, coefficient2))
    cor.append("$$ A = (%s + %s) \\times \\sqrt{%s} $$" % (carre1, carre2, coefficient1))
    cor.append("$$ A = \\boxed{%s \\sqrt{%s}} $$" % (carre1 + carre2, coefficient1))
    return (exo, cor, question)

def Soustraction(parametre):
    question = u"Calculer et simplifier :"
    exo = []
    cor = []
    (coefficient1, carre1, coefficient2, carre2) = valeurs_addition(parametre[0], parametre[1])
    exo.append("$$ A = \\sqrt{%s} - \\sqrt{%s} $$" % (coefficient1 *  carre1 ** 2, coefficient2 *  carre2 ** 2))
    cor.append("$$ A = \\sqrt{%s} - \\sqrt{%s} $$" % (coefficient1 *  carre1 ** 2, coefficient2 *  carre2 ** 2))
    cor.append("$$ A = \\sqrt{%s \\times %s} - \\sqrt{%s \\times %s} $$" % (carre1 ** 2, coefficient1, carre2 ** 2, coefficient2))
    cor.append("$$ A = \\sqrt{%s} \\times \\sqrt{%s} - \\sqrt{%s} \\times \\sqrt{%s} $$" % (carre1 ** 2, coefficient1, carre2 ** 2, coefficient2))
    cor.append("$$ A = \\sqrt{%s^2} \\times \\sqrt{%s} - \\sqrt{%s^2} \\times \\sqrt{%s} $$" % (carre1, coefficient1, carre2, coefficient2))
    cor.append("$$ A = %s \\times \\sqrt{%s} - %s \\times \\sqrt{%s} $$" % (carre1, coefficient1, carre2, coefficient2))
    cor.append("$$ A = (%s - %s) \\times \\sqrt{%s} $$" % (carre1, carre2, coefficient1))
    cor.append("$$ A = \\boxed{%s \\sqrt{%s}} $$" % (carre1 - carre2, coefficient1))
    return (exo, cor, question)

def Multiplication(parametre):
    question = u"Calculer et simplifier :"
    exo = []
    cor = []
    (nombre1, nombre2, coefficient, carre, decomposition) = valeurs_produit(parametre[0], parametre[1])
    exo.append("$$ A = \\sqrt{%s} \\times \\sqrt{%s} $$" % (nombre1, nombre2))
    cor.append("$$ A = \\sqrt{%s} \\times \\sqrt{%s} $$" % (nombre1, nombre2))
    cor.append("$$ A = \\sqrt{%s \\times %s} $$" % (nombre1, nombre2))
    cor.append("$$ A =\\sqrt{ %s } $$" % tex_produit(decomposition))
    cor.append("$$ A = \\sqrt{%s \\times %s} $$" % (carre ** 2, coefficient))
    cor.append("$$ A = \\sqrt{%s^2 \\times %s} $$" % (carre, coefficient))
    cor.append("$$ A = %s \\times \\sqrt{%s} $$" % (carre, coefficient))
    cor.append("$$ A = \\boxed{%s \\sqrt{%s}} $$" % (carre, coefficient))
    return (exo, cor, question)
