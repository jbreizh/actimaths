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
from outils import Affichage, Arithmetique

nom_rang = [u"cent-millionièmes", u"dix-millionièmes", u"millionièmes", u"cent-millièmes", u"dix-millièmes", u"millièmes", u"centièmes", u"dixièmes",
             u"unités",
             "dizaines", "centaines", "milliers", "dizaines de milliers", "centaines de milliers", "millions", "dizaines de millions", "centaines de millions"]

pronom = [u"d\'", "de "]

#
##------------------VALEURS--------------------------------------------------
def valeurs(rang_partie_decimal, rang_partie_entier):
    chiffres = [ '1', '1', '1', '2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '8', '8', '8', '9', '9', '9'] # un même chiffre peut apparaitre 3 fois
    nombre_list = []
    for i in range(0,rang_partie_entier - rang_partie_decimal):
        nombre_list.append(chiffres.pop(random.randrange(len(chiffres))))
    return nombre_list

#
##------------------AFFICHAGE--------------------------------------------------

def tex_nombre_list(nombre_list, rang_partie_decimal, rang_partie_entier):
    nombre_sans_virgule = ''.join([num for num in reversed(nombre_list)])
    if rang_partie_entier == 0:
        nombre_list.insert(abs(rang_partie_decimal),'0,')
        nombre = ''.join([num for num in reversed(nombre_list)])
        nombre_list.remove('0,')
    elif rang_partie_decimal == 0:
        nombre = ''.join([num for num in reversed(nombre_list)])
    else:
        nombre_list.insert(abs(rang_partie_decimal),',')
        nombre = ''.join([num for num in reversed(nombre_list)])
        nombre_list.remove(',')
    return nombre, nombre_sans_virgule

#
##---------------------CONSTRUCTION----------------------------------------------

def Chiffre(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    # generation d'un nombre
    nombre_list = valeurs(parametre[0], parametre[1])
    (nombre, nombre_sans_virgule) = tex_nombre_list(nombre_list, parametre[0], parametre[1])
    # choix d'un rang
    rang = random.randint(8 + parametre[0], 7 + parametre[1])
    rang_nombre = rang - 8 - parametre[0]
    # affichage
    exo.append("Pour le nombre $%s$ \\newline" % nombre)
    exo.append("Le chiffre des %s est $\\ldots$" % nom_rang[rang])
    cor.append("Pour le nombre $%s$ \\newline" % nombre)
    cor.append("Le chiffre des %s est $ \\boxed{%s} $" % (nom_rang[rang],nombre_list[rang_nombre]))
    return (exo, cor, question)

def Nombre(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    # generation d'un nombre
    nombre_list = valeurs(parametre[0], parametre[1])
    (nombre, nombre_sans_virgule) = tex_nombre_list(nombre_list, parametre[0], parametre[1])
    # choix d'un rang
    rang = random.randint(8 + parametre[0], 7 + parametre[1])
    rang_nombre = rang - 8 - parametre[0]
    # affichage
    exo.append("Pour le nombre $%s$ \\newline" % nombre)
    exo.append("Le nombre %s%s est $\\ldots$" % (pronom[min(abs(rang- 8),1)], nom_rang[rang]))
    cor.append("Pour le nombre $%s$ \\newline" % nombre)
    cor.append("Le nombre %s%s est $ \\boxed{%s} $" % (pronom[min(abs(rang- 8),1)], nom_rang[rang], nombre_sans_virgule[0:len(nombre_sans_virgule)-rang_nombre]))
    return (exo, cor, question)

def EntierNom(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    # generation d'un nombre
    nombre_list = valeurs(parametre[0], parametre[1])
    (nombre, nombre_sans_virgule) = tex_nombre_list(nombre_list, parametre[0], parametre[1])
    # choix d'un rang et on compte combien de fois le chiffre à ce rang apparait dans le nombre
    rang_list = []
    rang_nombre_list = []
    rang_list.append(random.randint(8 + parametre[0], 7 + parametre[1]))
    rang_nombre_list.append(rang_list[0] - 8 - parametre[0])
    for i in range(len(nombre_list)):
        if nombre_list[i] == nombre_list[rang_nombre_list[0]] and i != rang_nombre_list[0]:
            rang_list.append(i + 8 + parametre[0])
            rang_nombre_list.append(i)
    rang_list.sort()
    rang_nombre_list.sort()
    # affichage
    exo.append("Pour le nombre $%s$ \\newline" % nombre)
    exo.append("%s est le chiffre des $\\ldots$" % nombre_list[rang_nombre_list[0]])
    cor.append("Pour le nombre $%s$ \\newline" % nombre)
    cor.append("%s est le chiffre des :" % nombre_list[rang_nombre_list[0]])
    cor.append("\\begin{itemize}")
    for rang in rang_list:
      cor.append("\\item %s" % nom_rang[rang])
    cor.append("\\end{itemize}")
    return (exo, cor, question)
