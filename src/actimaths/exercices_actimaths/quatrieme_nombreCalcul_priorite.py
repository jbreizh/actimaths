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

from outils import Arithmetique
from outils.Priorites import OperateurPrioritaire
from outils.TeXMiseEnForme import Affichage
import random
from outils.Fractions import Fractions #Classe Fractions de pyromaths


def valeurs_priorites_fractions(nb, nombre_min, nombre_max, entier=1):  # renvoie les 2 listes contenant les opérateurs et les opérandes.
    listoperateurs = ["+", "*", "-", "/", '(', '(', '(', '(', ')', ')', ')', ')' ]
    loperateurs = []
    loperandes = []
    i = 0  #nombre d'opérateurs créés
    p = 0  #nombre de parenthèses ouvertes
    cpt = 0  #compteur pour éviter que le programme ne boucle.
    while i < nb - 1:
        cpt = cpt + 1
        if cpt > 10:  #On recommence
            (cpt, i, p, loperateurs) = (0, 0, 0, [])
        if p:
            if loperateurs[-1] == '(':  # On n'écrit pas 2 parenthèses à suivre
                operateur = listoperateurs[random.randrange(4)]
            else:
                operateur = listoperateurs[random.randrange(12)]
        elif loperateurs == []:# On ne commence pas par une parenthèse
            operateur = listoperateurs[random.randrange(4)]
        else:
            operateur = listoperateurs[random.randrange(8)]
        if nb > 3:
            test = ('-*/').find(operateur) >= 0 and loperateurs.count(operateur) < 1 or operateur == "+" and loperateurs.count(operateur) < 2
        else:
            test = ('-*/+').find(operateur) >= 0 and loperateurs.count(operateur) < 1
        if test: #On n'accepte pas plus de 1 produit, différence, quotient et de 2 sommes ou parenthèses par calcul.
            if i == 0 or loperateurs[-1] != '(' or ('*/').find(operateur) <  0:  #pas de * ou / dans une parenthèse.
                i = i + 1
                loperateurs.append(operateur)
        elif operateur == '(' and (')+').find(loperateurs[-1]) < 0: #Il ne peut y avoir de ( après une ) ou après un +
            p = p + 1
            loperateurs.append(operateur)
        elif operateur == ')':
            p = p - 1
            loperateurs.append(operateur)
    while p > 0:
        loperateurs.append(')')
        p = p - 1
    loperandes = []
    for i in range(nb):
        (n, d) = (2, 1)
        while  abs(d) == 1:
            n = Arithmetique.valeur_alea(nombre_min, nombre_max)
            d = Arithmetique.valeur_alea(nombre_min, nombre_max)
        loperandes.append(Fractions(n, d))
    exercice = [loperandes[0]]
    i = 1
    j = 0
    while i < len(loperandes) or j < len(loperateurs):
        if j < len(loperateurs):
            exercice.append(loperateurs[j])
            j = j + 1
        while j < len(loperateurs) and (loperateurs[j] == '(' or  loperateurs[j - 1] == ')'):
            exercice.append(loperateurs[j])
            j = j + 1
        if i < len(loperandes):
            exercice.append(loperandes[i])
            i = i + 1
    return exercice

def Relatif3Operande(parametre):
    question = "Calculer et simplifier:"
    exo = [ ]
    cor = [ ]
    l = valeurs_priorites_fractions(3, parametre[0], parametre[1])
    (sol, res, niveau) = OperateurPrioritaire(l, 4, solution=[])
    exo.append("$$ A = %s $$" % Affichage(l))
    cor.append("$$ A = %s $$" % Affichage(l))
    for l in sol:
        if l == sol[-1]:
            cor.append("$$ \\boxed{A = %s} $$" % l)
        else:
            cor.append("$$ A = %s $$" % l)
    return (exo, cor, question)

def Relatif4Operande(parametre):
    question = "Calculer et simplifier:"
    exo = [ ]
    cor = [ ]
    l = valeurs_priorites_fractions(4, parametre[0], parametre[1])
    (sol, res, niveau) = OperateurPrioritaire(l, 4, solution=[])
    exo.append("$$ A = %s $$" % Affichage(l))
    cor.append("$$ A = %s $$" % Affichage(l))
    for l in sol:
        if l == sol[-1]:
            cor.append("$$ \\boxed{A = %s} $$" % l)
        else:
            cor.append("$$ A = %s $$" % l)
    return (exo, cor, question)
