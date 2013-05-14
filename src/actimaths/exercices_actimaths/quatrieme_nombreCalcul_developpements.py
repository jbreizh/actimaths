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

from outils.Arithmetique import valeur_alea, signe, pgcd
from outils.Affichage import  tex_dev0, tex_dev1, tex_trinome
import random

variable_list = ['x', 'y', 'a', 'b', 'k', 'm', 'p']

def dev(a):  # renvoi un tuple avec les 3 coefficients du developpement
    return (a[0][0] * a[1][0], a[0][0] * a[1][1] + a[0][1] * a[1][0], a[0][1] * a[1][1])


#
# ------------------- GENERATION DES VALEURS -------------------

def valeurs_distr(nombre_min, nombre_max):  # renvoie in tuple contenant ((a,b),(c,d)) avec a != c ou b != d (en valeur absolue) et a, b, c ou d nul.
    while True:
        a = valeur_alea(nombre_min, nombre_max)
        b = valeur_alea(nombre_min, nombre_max)
        c = valeur_alea(nombre_min, nombre_max)
        l = [a, b, c]
        l.insert(random.randrange(4), 0)
        if abs(l[1]) != 1 and abs(l[3]) != 1:
            break  #Pour qu'il y ait quelque chose à développer.
    return ((l[0], l[1]), (l[2], l[3]))

def valeurs_dbldistr(nombre_min, nombre_max):  # renvoie in tuple contenant ((a,b),(c,d)) avec a != c ou b != d (en valeur absolue)
    a = valeur_alea(nombre_min, nombre_max)
    b = valeur_alea(nombre_min, nombre_max)
    c = valeur_alea(nombre_min, nombre_max)
    d = valeur_alea(nombre_min, nombre_max)
    while abs(a) == abs(c) and abs(b) == abs(d):
        c = valeur_alea(nombre_min, nombre_max)
        d = valeur_alea(nombre_min, nombre_max)
    return ((a, b), (c, d))

#
# ------------------- CONSTRUCTION -------------------

def construction(valeur):
    question = u"Développer et réduire :"
    exo = []
    cor = []
    variable = variable_list[ random.randrange(7) ]
    exo.append(u'$$ A = ' + tex_dev0(valeur, variable) + '$$')
    cor.append(u'$$ A = ' + tex_dev0(valeur, variable) + '$$')
    cor.append(u'$$ A = ' + tex_dev1(valeur, variable) + '$$')
    cor.append(u'$$ A = ' + tex_trinome(dev(valeur), variable) + '$$')
    return (exo, cor, question)

def DistributiviteSimple(parametre):
    (exo, cor, question) = construction(valeurs_distr(parametre[0], parametre[1]))
    return (exo, cor, question)

def DistributiviteDouble(parametre):
    (exo, cor, question) = construction(valeurs_dbldistr(parametre[0], parametre[1]))
    return (exo, cor, question)
