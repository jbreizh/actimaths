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

#valeurs = ["milliers", "centaines", "dizaines", u"unités", u"dixièmes", u"centièmes", u"millièmes"]
rang = [u"cent-millionièmes", u"dix-millionièmes", u"millionièmes", u"cent-millièmes", u"dix-millièmes", u"millièmes", u"centièmes", u"dixièmes",
        u"unités",
        u"dizaines", u"centaines", u"milliers", u"dizaines de milliers", u"centaines de milliers", u"millions", u"dizaines de millions", u"centaines de millions"]

def ecrit_nombre_decimal(dec, index):
    if index < 1:
        dec.insert(0, '0')
        dec.insert(1, '.')
        for i in range(-index):
            dec.insert(2, '0')
    elif index < len(dec):
        dec.insert(index, '.')
    else:
        for i in range(index - len(dec)):
            dec.append('0')
    strnb = ""
    for i in range(len(dec)):
        strnb = strnb + dec[i]
    return strnb

def valeurs_decimaux():
    chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    longueur_nombre = random.randrange(1,4)
    nombre = 0
    for i in range(longueur_nombre):
        nombre = nombre + chiffres.pop(random.randrange(len(chiffres))) * 10 ** i
    nombre_list = [str(nombre)[i] for i in range(len(str(nombre)))]
    return (nombre, longueur_nombre, nombre_list)

def PlaceVirgule(parametre):
    # Parametres
    while True:
        (nombre, longueur_nombre, nombre_list) = valeurs_decimaux()
        index_chiffre = random.randrange(longueur_nombre)
        index_rang = random.randrange(parametre[0]+8, parametre[1]+8)
        decallage = index_chiffre+index_rang-7
        if longueur_nombre - decallage != 0:
            break
    # initialisa
    question = u"Modifie %s pour que:" % nombre
    exo = []
    cor = []
    exo.append("\\begin{center}")
    exo.append(u"%s soit le chiffre des %s" % (nombre_list[index_chiffre], rang[index_rang]))
    exo.append("\\end{center}")
    cor.append(u"\\textbf{%s est le chiffre des %s de :}" % (nombre_list[index_chiffre], rang[index_rang]))
    resultat = ecrit_nombre_decimal(nombre_list, decallage)
    cor.append("$$%s$$" %Affichage.decimaux(resultat, 0))
    return (exo, cor, question)
