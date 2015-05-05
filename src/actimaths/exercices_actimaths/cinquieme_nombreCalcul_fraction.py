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
from math import sqrt
from outils.Fractions import Fractions #Classe Fractions de pyromaths
from outils.Arithmetique import pgcd, valeur_alea


#def valeur_fraction(nombre_min, nombre_max):
#    while True:
#        n = valeur_alea( nombre_min, nombre_max)
#        d = valeur_alea( nombre_min, nombre_max)
#        pgcdMax = min( 10 , int(sqrt(min(abs(n),abs(d)))))
#        if pgcdMax > 5:
#            pgcdnd = valeur_alea( 2, pgcdMax)
#            if pgcd( n , d ) == pgcdnd and abs(n) != abs(d):
#                break
#    fr = Fractions(n, d)
#    return fr

def valeur_fraction(nombre_min, nombre_max):
    #Génération de  2 nombres différents premiers entre eux
    numerateur = valeur_alea(nombre_min, nombre_max)
    denominateur = valeur_alea(nombre_min, nombre_max)
    while numerateur == denominateur or pgcd( numerateur , denominateur ) != 1:
        numerateur = valeur_alea(nombre_min, nombre_max)
        denominateur = valeur_alea(nombre_min, nombre_max)
    #Génération d'un PGCD libre entre 2 et 10 si < 100 (table) ou 2;3;4;5;9;10 si > 100 (critere)
    pgcdNumerateurDenominateur = valeur_alea(2,10)
    while (abs(numerateur*pgcdNumerateurDenominateur)>100 or abs(denominateur*pgcdNumerateurDenominateur)>100) and (pgcdNumerateurDenominateur==6 or pgcdNumerateurDenominateur==7 or pgcdNumerateurDenominateur==8):
        pgcdNumerateurDenominateur = valeur_alea(2,10)
    fraction = Fractions(numerateur*pgcdNumerateurDenominateur, denominateur*pgcdNumerateurDenominateur)
    return fraction


def valeur_decimal(nombre_min, nombre_max):
    n = valeur_alea( nombre_min, nombre_max)
    longueur_n = len(str(n))
    d = 10 ** randrange(longueur_n-1, longueur_n+3)
    while pgcd( n , d ) == 1:
        n = valeur_alea( nombre_min, nombre_max)
        longueur_n = len(str(n))
        d = 10 ** randrange(longueur_n-1, longueur_n+3)
    fr = Fractions(n, d)
    return float(n)/d, fr

########################Construction#############################

def SimplifierFraction(parametre):
    question = u"Simplifier au maximum :"
    exo = []
    cor = []
    fraction = valeur_fraction(parametre[0], parametre[1])
    exo.append("$$ A = %s $$" % Fractions.TeX(fraction))
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("A & = %s \\\\" % Fractions.TeX(fraction))
    cor.append("A & = %s \\\\" %Fractions.TeXSimplifie(fraction))
    cor.append("A & = \\boxed{%s} \\\\" %Fractions.simplifie(fraction))
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def SimplifierDecimal(parametre):
    question = u"Converti en fraction et simplifie :"
    exo = []
    cor = []
    (decimal, fraction) = valeur_decimal(parametre[0], parametre[1])
    exo.append("$$ A = %s $$" % decimal)
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("A & = %s \\\\" % decimal)
    cor.append("A & = %s \\\\" % Fractions.TeX(fraction))
    cor.append("A & = %s \\\\" % Fractions.TeXSimplifie(fraction))
    cor.append("A & = \\boxed{%s} \\\\" % Fractions.simplifie(fraction))
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def FractionEgale(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    #Génération des nombres
    n = d = 1
    while n == d:
        n = valeur_alea(parametre[0], parametre[1])
        d = valeur_alea(parametre[0], parametre[1])
    c = randrange(2, 11)
    #Construction
    cas = randrange(2)
    if cas:
        enonce = [n, d, n * c, d * c]
        solution = [n, d, n * c, d * c]
    else:
        enonce = [n * c, d * c, n, d]
        solution = [n * c, d * c, n, d]
    trou = randrange(4)
    enonce[trou] = "\\ldots"
    solution[trou] = "\\boxed{%s}" % solution[trou]
    if cas:
        solution.insert(2, c)
        solution.insert(1, c)
    else:
        solution.insert(4, c)
        solution.insert(3, c)
    #Affichage
    exo.append("$$\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$$" % tuple(enonce))
    if cas:
        cor.append("$$\\dfrac{%s_{(\\times %s)}}{%s_{(\\times %s)}}=\\dfrac{%s}{%s}$$" % tuple(solution))
    else:
        cor.append("$$\\dfrac{%s}{%s}=\\dfrac{%s_{(\\times %s)}}{%s_{(\\times %s)}}$$" % tuple(solution))
    return (exo, cor, question)
