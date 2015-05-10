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

import math
import random
import string
from outils import Arithmetique

#===============================================================================
# Calcul mental
#===============================================================================

def plus(nombre_min, nombre_max):
    (a, b) = (Arithmetique.valeur_alea(nombre_min, nombre_max), Arithmetique.valeur_alea(nombre_min, nombre_max))
    return (a, b)

def plus_cinq(nombre_min, nombre_max):
    choix = random.randrange(2)
    if choix:
        (a, b) = (Arithmetique.valeur_alea(nombre_min, nombre_max), 5)
    else:
        (a, b) = (5, Arithmetique.valeur_alea(nombre_min, nombre_max))
    return (a, b)

def plus_neuf(nombre_min, nombre_max):
    choix = random.randrange(2)
    if choix:
        (a, b) = (Arithmetique.valeur_alea(nombre_min, nombre_max), 9)
    else:
        (a, b) = (9, Arithmetique.valeur_alea(nombre_min, nombre_max))
    return (a, b)

def plus_dec(nombre_min, nombre_max):
    (a, b) = (Arithmetique.valeur_alea(nombre_min*10, nombre_max*10), Arithmetique.valeur_alea(nombre_min*10, nombre_max*10))
    return (a/10.0, b/10.0)

def moins(nombre_min, nombre_max):
    b = Arithmetique.valeur_alea(nombre_min, nombre_max)
    a = Arithmetique.valeur_alea(nombre_min, nombre_max)
    if a >=b:
        return (a, b)
    else:
        return (b, a)

def moins_dec(nombre_min, nombre_max):
    b = Arithmetique.valeur_alea(nombre_min*10, nombre_max*10)
    a = Arithmetique.valeur_alea(nombre_min*10, nombre_max*10)
    if a >=b:
        return (a/10.0, b/10.0)
    else:
        return (b/10.0, a/10.0)

def moins_neuf(nombre_min, nombre_max):
    a = Arithmetique.valeur_alea(nombre_min, nombre_max)
    b = 9
    if a >=b:
        return (a, b)
    else:
        return (b, a)

def div(nombre_min, nombre_max):
    a = 2
    while Arithmetique.premier(a):
        a = Arithmetique.valeur_alea(nombre_min, nombre_max)

    decomposition_a = Arithmetique.factor(a)
    nbre_facteur_a = len(decomposition_a)
    
    decomposition_b = random.sample(decomposition_a,random.randrange(1,len(decomposition_a)))
    b = 1
    for facteur in  decomposition_b:
        b = b * facteur
    return (a, b)

def div_dec(nombre_min, nombre_max):
    a = 2
    while Arithmetique.premier(a):
        a = Arithmetique.valeur_alea(nombre_min*10, nombre_max*10)

    decomposition_a = Arithmetique.factor(a)
    nbre_facteur_a = len(decomposition_a)
    
    decomposition_b = random.sample(decomposition_a,random.randrange(1,len(decomposition_a)))
    b = 1
    for facteur in  decomposition_b:
        b = b * facteur
    return (a/10.0, b/10.0)

def tex_calcul_mental(operation, nombre_min, nombre_max):
    question = "Calculer :"
    exo = [ ]
    cor = [ ]
    if operation == 0:
        (a, b) = plus(nombre_min, nombre_max)
        choix_trou(a, b, a + b, '+', exo, cor)
    if operation == 1:
        (a, b) = moins(nombre_min, nombre_max)
        choix_trou(a, b, a - b, '-', exo, cor)
    if operation == 2:
        (a, b) = plus(nombre_min, nombre_max)
        choix_trou(a, b, a * b, '\\times', exo, cor)
    if operation == 3:
        (a, b) = div(nombre_min, nombre_max)
        choix_trou(a, b, a // b, '\\div', exo, cor)
    if operation == 4:
        (a, b) = plus_dec(nombre_min, nombre_max)
        choix_trou(a, b, a + b, '+', exo, cor)
    if operation == 5:
        (a, b) = moins_dec(nombre_min, nombre_max)
        choix_trou(a, b, a - b, '-', exo, cor)
    if operation == 6:
        (a, b) = plus_dec(nombre_min, nombre_max)
        choix_trou(a, b, a * b, '\\times', exo, cor)
    if operation == 7:
        (a, b) = div_dec(nombre_min, nombre_max)
        choix_trou(a, b, a // b, '\\div', exo, cor)
    if operation == 8:
        (a, b) = plus_neuf(nombre_min, nombre_max)
        choix_trou(a, b, a + b, '+', exo, cor)
    if operation == 9:
        (a, b) = moins_neuf(nombre_min, nombre_max)
        choix_trou(a, b, a - b, '-', exo, cor)
    if operation == 10:
        (a, b) = plus_cinq(nombre_min, nombre_max)
        choix_trou(a, b, a * b, '\\times', exo, cor)
    return (exo, cor, question)

def choix_trou(nb1, nb2, tot, operateur, exo, cor):
    exo.append('$$%s %s %s = \\ldots\\ldots$$' % (nb1, operateur, nb2))
    cor.append('$$%s %s %s = \\boxed{%s}$$' % (nb1, operateur, nb2, tot))

#-----------------------Construction-----------------------

def AdditionEntier(parametre):
    (exo, cor, question) = tex_calcul_mental(0, parametre[0], parametre[1])
    return (exo, cor, question)

def SoustractionEntier(parametre):
    (exo, cor, question) = tex_calcul_mental(1, parametre[0], parametre[1])
    return (exo, cor, question)

def MultiplicationEntier(parametre):
    (exo, cor, question) = tex_calcul_mental(2, parametre[0], parametre[1])
    return (exo, cor, question)

def DivisionEntier(parametre):
    (exo, cor, question) = tex_calcul_mental(3, parametre[0], parametre[1])
    return (exo, cor, question)

def AdditionDecimal(parametre):
    (exo, cor, question) = tex_calcul_mental(4, parametre[0], parametre[1])
    return (exo, cor, question)

def SoustractionDecimal(parametre):
    (exo, cor, question) = tex_calcul_mental(5, parametre[0], parametre[1])
    return (exo, cor, question)

def MultiplicationDecimal(parametre):
    (exo, cor, question) = tex_calcul_mental(6, parametre[0], parametre[1])
    return (exo, cor, question)

def DivisionDecimal(parametre):
    (exo, cor, question) = tex_calcul_mental(7, parametre[0], parametre[1])
    return (exo, cor, question)

def AdditionNeuf(parametre):
    (exo, cor, question) = tex_calcul_mental(8, parametre[0], parametre[1])
    return (exo, cor, question)

def SoustractionNeuf(parametre):
    (exo, cor, question) = tex_calcul_mental(9, parametre[0], parametre[1])
    return (exo, cor, question)

def MultiplicationCinq(parametre):
    (exo, cor, question) = tex_calcul_mental(10, parametre[0], parametre[1])
    return (exo, cor, question)
