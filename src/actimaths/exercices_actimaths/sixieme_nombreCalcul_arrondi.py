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

from random import randint, sample, randrange
from outils.Affichage import decimaux

nom_precision = [u"au cent-millionième", u"au dix-millionième", u"au millionième", u"au cent-millième", u"au dix-millième", u"au millième", u"au centième", u"au dixième",
                 u"à l\'unité",
                 u"à la dizaine", u"à la centaine", u"au millier", u"à la dizaines de millier", u"à la centaines de millier", u"au million", u"à la dizaines de million", u"à la centaines de million"]

nom_type = ['au plus proche', u'par défaut', u'par excès']

#
##----------------Fonction--------------------------------
def valeurs(rang_partie_decimal, rang_partie_entier):
    nombre = 0
    for rang in range(rang_partie_decimal, rang_partie_entier):
        # On génère le chiffre
        chiffre = randint(1,9)
        # On regénère le chiffre pour ne pas avoir un 5 en dernier 
        while chiffre == 5 and rang == rang_partie_decimal:
            chiffre = randint(1,9)
        # On place le chiffre au rang donné
        nombre += chiffre * 10 ** rang     
    return nombre

def encadrement(nombres, precision):
    arrondi = round(nombres, precision)
    if (arrondi > nombres):
        defaut = arrondi - 10 ** -precision
        exces = arrondi
    else:
        defaut = arrondi
        exces = arrondi + 10 ** -precision
    return defaut, exces, arrondi
#
##----------------Construction--------------------------------

def ArrondirDecimal(parametre):
    question = "Arrondir :"
    exo = []
    cor = []
    # choix d'une precision
    precision = randint(8 + parametre[0], 7 + parametre[1])
    precision_nombre = 8 - precision
    # Génération des variables
    nombre = valeurs(parametre[0], parametre[1])
    (defaut, exces, arrondi) = encadrement(nombre, precision_nombre)
    # Choix du type d'arrondi
    type = randrange(3)
    if type == 0:
        solution = arrondi
    elif type == 1:
        solution = defaut
    elif type == 2:
        solution = exces
    # Affichage
    exo.append("%s %s %s" % (decimaux(nombre),nom_precision[precision],nom_type[type]))
    cor.append("$$ %s < %s < %s $$" % (decimaux(defaut),decimaux(nombre),decimaux(exces)))
    cor.append("L\'arrondi %s %s est $ \\boxed{%s} $" % (nom_precision[precision], nom_type[type], decimaux(solution)))
    return (exo, cor, question)

def EncadrerDecimal(parametre):
    question = u"Compléter l\'encadrement de :"
    exo = []
    cor = []
    # choix d'une precision
    precision = randint(8 + parametre[0], 7 + parametre[1])
    precision_nombre = 8 - precision
    # Génération des variables
    nombre = valeurs(parametre[0], parametre[1])
    (defaut, exces, arrondi) = encadrement(nombre, precision_nombre)
    # Affichage
    exo.append("%s %s" % (decimaux(nombre),nom_precision[precision]))
    if randrange(2):
        exo.append("$$ \\ldots < %s < %s $$" % (decimaux(nombre),decimaux(exces)))
        cor.append("$$ \\boxed{%s} < %s < %s $$" % (decimaux(defaut),decimaux(nombre),decimaux(exces)))
    else:
        exo.append("$$ %s < %s <  \\ldots $$" % (decimaux(defaut),decimaux(nombre)))
        cor.append("$$ %s < %s < \\boxed{%s} $$" % (decimaux(defaut),decimaux(nombre),decimaux(exces)))
    return (exo, cor, question)

def IntercalerDecimal(parametre):
    question = "Intercaler un nombre entre :"
    exo = []
    cor = []
    # choix d'une precision
    precision = randint(8 + parametre[0], 7 + parametre[1])
    precision_nombre = 8 - precision
    # Génération des variables
    nombre = valeurs(parametre[0], parametre[1])
    (defaut, exces, arrondi) = encadrement(nombre, precision_nombre)
    # Affichage
    exo.append("%s et %s" % (decimaux(defaut),decimaux(exces)))
    exo.append("$$ %s < \\ldots < %s $$" % (decimaux(defaut),decimaux(exces)))
    cor.append("$$ %s < \\boxed{%s} < %s $$" % (decimaux(defaut),decimaux(nombre),decimaux(exces)))
    return (exo, cor, question)
