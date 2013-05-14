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
from outils.Affichage import tex_coef, tex_dev0, tex_dev1, tex_trinome
import random

def dev(a):  # renvoi un tuple avec les 3 coefficients du developpement
    return (a[0][0] * a[1][0], a[0][0] * a[1][1] + a[0][1] * a[1][0], a[0][1] * a[1][1])

#
# ------------------- GENERATION DES VALEURS -------------------

def valeurs_distr(nombre_min, nombre_max):
    while True:
        a = valeur_alea(nombre_min, nombre_max)
        b = valeur_alea(nombre_min, nombre_max)
        c = valeur_alea(nombre_min, nombre_max)
        l = [a, b, c]
        l.insert(random.randrange(0, 4, 2), 0)
        if abs(l[1]) != 1 and abs(l[3]) != 1:
            break  #Pour qu'il y ait quelque chose à développer.
    return ((l[0], l[1]), (l[2], l[3]))

def valeurs_calcul_distr(nombre_min, nombre_max): 
    cpt = 0
    while True:
        cpt += 1
        # generation de 2 nombres
        nombre1 = valeur_alea(nombre_min, nombre_max)
        nombre2 = valeur_alea(nombre_min, nombre_max)
        # arrondi au premier chiffre et distance à cet arrondi  
        nombre1_arrondi = int(round( nombre1 , min( 1 - len(str(abs(nombre1))), -1) ))
        nombre1_distance = nombre1 - nombre1_arrondi
        nombre2_arrondi = int(round( nombre2 , min( 1 - len(str(abs(nombre2))), -1) ))
        nombre2_distance = nombre2 - nombre2_arrondi
        # on choisit de décomposer le nombre qui à la plus petite distance non nulle 
        if abs(nombre1_distance) <= abs(nombre2_distance) and abs(nombre1_distance)!= 0 and abs(nombre1)>=10 and abs(nombre2)!= 1:
            l = [ nombre1_arrondi, nombre1_distance, 0, nombre2 ]
            break
        elif abs(nombre1_distance) > abs(nombre2_distance) and abs(nombre2_distance)!= 0 and abs(nombre2)>=10 and abs(nombre1)!= 1:
            l = [ 0, nombre1, nombre2_arrondi, nombre2_distance ]
            break
        elif cpt > 50:
            l = [ 0, nombre1, 0, nombre2 ]
            break
    return ((l[0], l[1]), (l[2], l[3]))

def valeurs_facto(nombre_min, nombre_max):
    while True:
        a = valeur_alea(nombre_min, nombre_max)
        b = valeur_alea(nombre_min, nombre_max)
        c = valeur_alea(nombre_min, nombre_max)
        l = [0, a, b, c]
        if abs(l[1]) != 1:
            break  #Pour qu'il y ait quelque chose à développer.
    return ((l[0], l[1]), (l[2], l[3]))

#
# ------------------- CONSTRUCTION -------------------

def DistributiviteSimple(parametre):
    question = u"Développer :"
    exo = []
    cor = []
    valeur = valeurs_distr(parametre[0], parametre[1])
    exo.append(u'$$ A = ' + tex_dev0(valeur, '') + '$$')
    cor.append(u'$$ A = ' + tex_dev0(valeur, '') + '$$')
    cor.append(u'$$ A = \\boxed{' + tex_dev1(valeur, '') + '} $$')
    return (exo, cor, question)

def CalculDistributivite(parametre):
    question = u"Calculer astucieusement :"
    exo = []
    cor = []
    valeur = valeurs_calcul_distr(parametre[0], parametre[1])
    exo.append(u'$$ A = %s \\times %s $$' % (tex_coef(valeur[0][0]+valeur[0][1], ''), tex_coef(valeur[1][0]+valeur[1][1], '', 0, 1)))
    cor.append(u'$$ A = %s \\times %s $$' % (tex_coef(valeur[0][0]+valeur[0][1], ''), tex_coef(valeur[1][0]+valeur[1][1], '', 0, 1)))
    if abs(valeur[0][0])+ abs(valeur[1][0]):
        cor.append(u'$$ A = ' + tex_dev0(valeur, '') + '$$')
        cor.append(u'$$ A = ' + tex_dev1(valeur, '') + '$$')
        cor.append(u'$$ A = ' + tex_trinome(dev(valeur), '') + '$$')
    cor.append(u'$$ \\boxed{ A = %s } $$'% (dev(valeur)[0]+dev(valeur)[1]+dev(valeur)[2]))
    return (exo, cor, question)

def FactorisationSimple(parametre):
    question = u"Factoriser :"
    exo = []
    cor = []
    valeur = valeurs_facto(parametre[0], parametre[1])
    exo.append(u'$$ A = ' + tex_dev1(valeur, '') + '$$')
    cor.append(u'$$ A = ' + tex_dev1(valeur, '') + '$$')
    cor.append(u'$$ A = \\boxed{' + tex_dev0(valeur, '') + '} $$')
    return (exo, cor, question)
