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
import string

def valeurs(nombre_min, nombre_max):  # renvoie les 2 listes contenant les opérateurs et les opérandes.
    operateur = [' + ', ' - ', ' \\times ', ' \\div ', '']
    nom_operateur = ['de la somme ', u'de la différence ', 'du produit ', 'du quotient ', '']
    nom_operateur1 = ['la somme ', u'la différence ', 'le produit ', 'le quotient ', '']
    separateur_operateur = [' et ', ' et ', ' par ', ' par ', '']
    choix = random.sample(range(5),3)
    while choix[0] == 4:
	choix = random.sample(range(5),3)
    operande = [random.randint(nombre_min, nombre_max) for i in range(4)]

    expression = ['' for i in range(11)]
    nom_expression = ['' for i in range(10)]
    # on place les opérateurs
    expression[2]= operateur[choix[1]]
    expression[5]= operateur[choix[0]]
    expression[8]= operateur[choix[2]]

    nom_expression[0]= nom_operateur1[choix[0]]
    nom_expression[1]= nom_operateur[choix[1]]
    nom_expression[3]= separateur_operateur[choix[1]]
    nom_expression[5]= separateur_operateur[choix[0]]
    nom_expression[8]= separateur_operateur[choix[2]]

    if choix[0] > 1:
        nom_expression[6]= nom_operateur1[choix[2]]
        if choix[1] < 2:
            expression[0]= '('
            expression[4]= ')'
        if choix[2] < 2:
            expression[6]= '('
            expression[10]= ')'
    else:
        nom_expression[6]= nom_operateur[choix[2]]

    # on place les opérandes
    if choix[1] == 4:
        expression[1]= "%s" % operande[0]
        nom_expression[2] = "de %s" % operande[0]
    else:
        expression[1]= "%s" % operande[0]        
        expression[3]= "%s" % operande[1]
        nom_expression[2] = "de %s" % operande[0]
        nom_expression[4] = "%s" % operande[1]

    if choix[2] == 4:
        expression[7]= "%s" % operande[2]
        nom_expression[7] = "de %s" % operande[2]
    else:
        expression[7]= "%s" % operande[2]    
        expression[9]= "%s" % operande[3]
        nom_expression[7] = "de %s" % operande[2]
        nom_expression[9] = "%s" % operande[3]

    expression = "".join(expression)
    nom_expression = "".join(nom_expression)
    return expression, nom_expression

#------------------Construction-------------------------
def Expression(parametre):
    question = "Traduire par une expression :"
    exo = []
    cor = []
    (expression, nom_expression) = valeurs(parametre[0], parametre[1])
    exo.append(nom_expression)
    cor.append("$$ %s $$" % expression)
    return (exo, cor, question)

def NomExpression(parametre):
    question = "Traduire par une suite de calculs :"
    exo = []
    cor = []
    (expression, nom_expression) = valeurs(parametre[0], parametre[1])
    exo.append("$$ %s $$" % expression)
    cor.append(nom_expression)
    return (exo, cor, question)

