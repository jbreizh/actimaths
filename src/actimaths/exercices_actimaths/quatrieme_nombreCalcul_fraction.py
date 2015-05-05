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

from random import randrange
from outils import Arithmetique
from outils.Priorites import OperateurPrioritaire
from outils.TeXMiseEnForme import Affichage
from outils.Fractions import Fractions

def produits_fractions_4e(nombre_min, nombre_max, level):
    while True:
        n1=Arithmetique.valeur_alea(nombre_min, nombre_max)
        d1=Arithmetique.valeur_alea(nombre_min, nombre_max)
        n2=Arithmetique.valeur_alea(nombre_min, nombre_max)
        d2=Arithmetique.valeur_alea(nombre_min, nombre_max)
        fr1 = Fractions(n1, d1)
        fr2 = Fractions(n2, d2)
        simplifiable = abs(fr1.d * fr2.n) !=   Fractions.simplifie(fr1 / fr2).d
        if not simplifiable:
            if level ==1:
                break
        else:
            if level ==2:
                break
    l = [fr1, '/', fr2]
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
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("A & = %s \\\\" % Affichage(l))
    for l in sol:
        if l == sol[-1]:
            cor.append("A & = \\boxed{%s} \\\\" % l)
        else:
            cor.append("A & = %s \\\\" % l)
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

#
# ------------------------ EXERCICE ------------------------
def Quotient(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 1)
    return (exo, cor, question)

def QuotientSimplifiable(parametre):
    (exo, cor, question)= construction(parametre[0], parametre[1], 2)
    return (exo, cor, question)

def InverseEntier(parametre):
    question = u"Donner l'inverse de :"
    exo = []
    cor = []
    #variable
    nombre = Arithmetique.valeur_alea(parametre[0],parametre[1])
    inverse = Fractions(1, nombre)
    choix = randrange(2)
    #Tex
    if choix == 0:
        exo.append("$$ %s $$" % nombre)
        cor.append(u"L'inverse de $%s$ est $\\boxed{%s}$" % (nombre, Fractions.TeX(inverse)))
    else:
        exo.append("$$ %s $$" % Fractions.TeX(inverse))
        cor.append(u"L'inverse de $%s$ est $\\boxed{%s}$" % (Fractions.TeX(inverse), nombre))
    return (exo, cor, question)

def InverseFraction(parametre):
    question = u"Donner l'inverse de :"
    exo = []
    cor = []
    #variable
    numerateur = Arithmetique.valeur_alea(parametre[0],parametre[1])
    denominateur = Arithmetique.valeur_alea(parametre[0],parametre[1])
    nombre = Fractions(numerateur, denominateur)
    inverse = Fractions(denominateur, numerateur)
    #Tex
    exo.append("$$ %s $$" % Fractions.TeX(nombre))
    cor.append(u"L'inverse de $%s$ est $\\boxed{%s}$" % (Fractions.TeX(nombre), Fractions.TeX(inverse)))
    return (exo, cor, question)
