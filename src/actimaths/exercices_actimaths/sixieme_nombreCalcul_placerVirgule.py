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

#===============================================================================
# Placer une virgule
#===============================================================================

valeurs = ["milliers", "centaines", "dizaines", u"unités", u"dixièmes", u"centièmes", u"millièmes"]

def valeurs_decimaux(nombre_min, nombre_max):
    rang_max = random.randint(nombre_min, nombre_max)
    nb = 0
    chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(rang_max):
        nb = nb + chiffres.pop(random.randrange(len(chiffres))) * 10 ** i
    return nb

def ecrit_nombre_decimal(dec, index):
    """
    Renvoie une chaine de caractère représentant le nombre dec avec la virgule à la place index. Ajoute les zéros nécessaires.
    @param dec: décomposition d'un nombre entier
    @param index: place de la virgule dans la liste dec
    """

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

def PlaceVirgule(parametre):
    nombre = valeurs_decimaux(parametre[0], parametre[1])
    question = u"Déplacer la virgule de %s pour que:" % nombre
    exo = []
    cor = []
    longueur_nombre = len(str(nombre))
    nombre_list = [str(nombre)[i] for i in range(longueur_nombre)]
    index_nombre_list = random.randrange(longueur_nombre)
    index_valeurs = random.randrange(len(valeurs))
    exo.append(u"%s soit le chiffre des %s" % (nombre_list[index_nombre_list], valeurs[index_valeurs]))
    resultat = ecrit_nombre_decimal(nombre_list, (index_nombre_list + 4) - index_valeurs)
    cor.append(Affichage.decimaux(resultat, 0) + '')
    return (exo, cor, question)
