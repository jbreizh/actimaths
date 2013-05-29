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
from outils.Fractions import Fractions #Classe Fractions de pyromaths
import random

# Choisit des valeurs aléatoires pour effectuer une différence de fractions en fonction du niveau de difficulté souhaité (de 1 à 4)
def sommes_fractions_4e(nombre_min, nombre_max, level):
    while True:
        n1 = Arithmetique.valeur_alea(nombre_min, nombre_max)
        d1 = Arithmetique.valeur_alea(nombre_min, nombre_max)
        n2 = Arithmetique.valeur_alea(nombre_min, nombre_max)
        d2 = Arithmetique.valeur_alea(nombre_min, nombre_max)
        # Creation des 2 fractions
        fr1 = Fractions(n1, d1)
        fr2 = Fractions(n2, d2)
        # Sortie de boucle 
        if Arithmetique.pgcd(fr1.n, fr1.d) == 1 and Arithmetique.pgcd(fr2.n, fr2.d) == 1:
            if abs(fr1.d)== abs(fr2.d):
                # Sortie de boucle niveau 1
                if level == 1:
                    break
            else:
                if Arithmetique.pgcd(fr1.d, fr2.d) == abs(fr1.d) or Arithmetique.pgcd(fr1.d, fr2.d) == abs(fr2.d): 
                    # Sortie de boucle niveau 2
                    if level == 2:
                        break
                else: 
                    simplifiable = abs(fr1.d * fr2.d) != abs(Fractions.simplifie(fr1 - fr2).d)
                    if not simplifiable:
                        # Sortie de boucle niveau 3
                        if level == 3:
                            break
                    else:
                        # Sortie de boucle niveau 4
                        if level == 4:
                            break
    l = [fr1, '-', fr2]
    (cor, res, niveau) = OperateurPrioritaire(l, 4, solution=[])
    return ([fr1, '-', fr2], cor, res)

#
# ------------------- CONSTRUCTION EXERCICE -------------------

def construction(nombre_min, nombre_max, style):
    question = "Calculer et simplifier :"
    exo = [ ]
    cor = [ ]
    (l, sol, res) = sommes_fractions_4e(nombre_min, nombre_max, style)
    exo.append("$$ A = %s $$" % Affichage(l))
    cor.append("$$ A = %s $$" % Affichage(l))
    for l in sol:
        if l == sol[-1]:
            cor.append("$$ \\boxed{A = %s} $$" % l)
        else:
            cor.append("$$ A = %s $$" % l)
    return (exo, cor, question)

def RelatifCommun(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 1)
    return (exo, cor, question)

def RelatifMultiple(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 2)
    return (exo, cor, question)

def Relatif(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 3)
    return (exo, cor, question)

def RelatifSimplifiable(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 4)  
    return (exo, cor, question)
