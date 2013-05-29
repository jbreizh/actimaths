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
from outils.Priorites import OperateurPrioritaire
from outils.TeXMiseEnForme import Affichage
from outils.Fractions import Fractions

#Choisit des valeurs aléatoires pour effectuer un produit de fractions en fonction du niveau de difficulté souhaité (de 1 à 4)
def produits_fractions_4e(nombre_min, nombre_max, level):
    while True:
        n1=Arithmetique.valeur_alea(nombre_min, nombre_max)
        d1=Arithmetique.valeur_alea(nombre_min, nombre_max)
        n2=Arithmetique.valeur_alea(nombre_min, nombre_max)
        d2=Arithmetique.valeur_alea(nombre_min, nombre_max)
        fr1 = Fractions(n1, d1)
        fr2 = Fractions(n2, d2)
        simplifiable = abs(fr1.d * fr2.d) != Fractions.simplifie(fr1 * fr2).d
        if not simplifiable:
            if level ==1:
                break
        else:
            if level ==2:
                break
    l = [fr1, '*', fr2]
    (cor, res, niveau) = OperateurPrioritaire(l, 4, solution=[])
    return (l, cor, res)

#
# ------------------- CONSTRUCTION EXERCICE -------------------
def construction(nombre_min, nombre_max, style):
    question = "Calculer et simplifier :"
    exo = [ ]
    cor = [ ]
    (l, sol, res) = produits_fractions_4e(nombre_min, nombre_max, style)
    exo.append("$$ A = %s $$" % Affichage(l))
    cor.append("$$ A = %s $$" % Affichage(l))
    for l in sol:
        if l == sol[-1]:
            cor.append("$$ \\boxed{A = %s} $$" % l)
        else:
            cor.append("\\[A = %s\\]" % l)
    return (exo, cor, question)

def Relatif(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 1)
    return (exo, cor, question)

def RelatifSimplifiable(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 2)
    return (exo, cor, question)
