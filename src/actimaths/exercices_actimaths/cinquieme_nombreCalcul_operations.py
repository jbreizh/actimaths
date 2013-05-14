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
#----------------------------------------------------------------------
# Pyromaths : Poser des opérations
#----------------------------------------------------------------------

from outils import Arithmetique
from outils.Affichage import tex_coef
import random

def plus(nombre_min, nombre_max):
    (a, b) = (Arithmetique.valeur_alea(nombre_min, nombre_max), Arithmetique.valeur_alea(nombre_min, nombre_max))
    return (a, b)

def moins(nombre_min, nombre_max):
    (a, b) = (Arithmetique.valeur_alea(nombre_min, nombre_max), Arithmetique.valeur_alea(nombre_min, nombre_max))
    return (a, b)

def div(nombre_min, nombre_max):
    # on trouve a et b en valeur absolue
    a_absolu = 2
    while Arithmetique.premier(a_absolu):
        a_absolu = abs(Arithmetique.valeur_alea(nombre_min, nombre_max))
    decomposition_a_absolu = Arithmetique.factor(a_absolu)
    nbre_facteur_a_absolu = len(decomposition_a_absolu)
    decomposition_b_absolu = random.sample(decomposition_a_absolu,random.randrange(1,len(decomposition_a_absolu)))
    b_absolu = 1
    for facteur in  decomposition_b_absolu:
        b_absolu = b_absolu * facteur
    # on choisit le signe possible pour a et b
    a_possible = [-a_absolu , a_absolu]
    b_possible = [-b_absolu , b_absolu]

    if a_possible[1] < nombre_max:
        if nombre_min < a_possible[0]:
            a = a_possible[random.randrange(2)]
        else:
            a = a_possible[1]
    else:
        a = a_possible[0]

    if b_possible[1] < nombre_max:
        if nombre_min < b_possible[0]:
            b = b_possible[random.randrange(2)]
        else:
            b = b_possible[1]
    else:
        b = b_possible[0]

    return (a, b)

def tex_exercice(nombre_min, nombre_max, operation, style):
    question = "Calculer :"
    exo = []
    cor = []
    if operation == 0:
        (a, b) = plus(nombre_min, nombre_max)
        choix_trou(a, tex_coef(b, '', bpn=1), a + b, '+', exo, cor, style)
    if operation == 1:
        (a, b) = moins(nombre_min, nombre_max)
        choix_trou(a, tex_coef(b, '', bpn=1), a - b, '-', exo, cor, style)
    if operation == 2:
        (a, b) = plus(nombre_min, nombre_max)
        choix_trou(a, tex_coef(b, '', bpn=1), a * b, '\\times', exo, cor, style)
    if operation == 3:
        (a, b) = div(nombre_min, nombre_max)
        choix_trou(a, tex_coef(b, '', bpn=1), a // b, '\\div', exo, cor, style)
    return (exo, cor, question)

def choix_trou(nb1, nb2, tot, operateur, exo, cor, style):
    if style == 1:
        exo.append("$$%s %s %s = \\ldots\\ldots\\ldots$$" % (nb1, operateur, nb2))
        cor.append("$$%s %s %s = \\mathbf{%s}$$" % (nb1, operateur, nb2, tot))
    else:
        nbaleatoire = random.randrange(2)
        if nbaleatoire == 0:
            exo.append("$$%s %s \\ldots\\ldots\\ldots = %s$$" % (nb1, operateur, tot))
            cor.append("$$%s %s \\mathbf{%s} = %s$$" % (nb1, operateur, nb2, tot))
        else:
            exo.append("$$\\ldots\\ldots\\ldots %s %s = %s$$" % (operateur, nb2, tot))
            cor.append("$$\\mathbf{%s} %s %s = %s$$" % (nb1, operateur, nb2, tot))

#-----------------------Construction-----------------------

def Addition(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 0, 1)
    return (exo, cor, question)

def Soustraction(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 1, 1)
    return (exo, cor, question)

def Multiplication(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 2, 1)
    return (exo, cor, question)

def Division(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 3, 1)
    return (exo, cor, question)

def ComplementAddition(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 0, 0)
    return (exo, cor, question)

def ComplementSoustraction(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 1, 0)
    return (exo, cor, question)

def ComplementMultiplication(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 2, 0)
    return (exo, cor, question)

def ComplementDivision(parametre):
    (exo, cor, question) = tex_exercice(parametre[0], parametre[1], 3, 0)
    return (exo, cor, question)
