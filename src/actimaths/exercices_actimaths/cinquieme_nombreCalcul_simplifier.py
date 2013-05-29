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

from outils.Fractions import Fractions #Classe Fractions de pyromaths
import random
from outils.Arithmetique import pgcd, valeur_alea


def valeur_fraction(nombre_min, nombre_max):
    n = valeur_alea( nombre_min, nombre_max)
    d = valeur_alea( nombre_min, nombre_max)
    while pgcd( n , d ) == 1:
        n = valeur_alea( nombre_min, nombre_max)
        d = valeur_alea( nombre_min, nombre_max)
    fr = Fractions(n, d)
    return fr

def valeur_decimal(nombre_min, nombre_max):
    n = valeur_alea( nombre_min, nombre_max)
    longueur_n = len(str(n))
    d = 10 ** random.randrange(longueur_n-1, longueur_n+3)
    while pgcd( n , d ) == 1:
        n = valeur_alea( nombre_min, nombre_max)
        longueur_n = len(str(n))
        d = 10 ** random.randrange(longueur_n-1, longueur_n+3)
    fr = Fractions(n, d)
    return float(n)/d, fr

########################Construction#############################

def Fraction(parametre):
    question = u"Simplifier au maximum :"
    exo = []
    cor = []
    fraction = valeur_fraction(parametre[0], parametre[1])
    exo.append("$$ A = %s $$" % Fractions.TeX(fraction))
    cor.append("$$ A = %s $$" % Fractions.TeX(fraction))
    cor.append("$$ A = %s = %s$$" % (Fractions.TeXSimplifie(fraction), Fractions.simplifie(fraction)))
    return (exo, cor, question)

def Decimal(parametre):
    question = u"Converti en fraction et simplifie :"
    exo = []
    cor = []
    (decimal, fraction) = valeur_decimal(parametre[0], parametre[1])
    exo.append("$$ A = %s $$" % decimal)
    cor.append("$$ A = %s $$" % decimal)
    cor.append("$$ A = %s = %s = %s$$" % (Fractions.TeX(fraction), Fractions.TeXSimplifie(fraction), Fractions.simplifie(fraction)))
    return (exo, cor, question)
