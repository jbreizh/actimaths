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

from outils.Arithmetique import valeur_alea, signe, pgcd, ppcm
from outils.Affichage import tex_trinome, tex_coef
import random

variable_list = ['x', 'y', 'a', 'b', 'k', 'm', 'p']

#
# ------------------- METHODE -------------------
def tex_frac(a):  #renvoie l'ecriture au format tex de la fraction a
    if not isinstance(a, tuple):
        return ''
    else:
        a = ((a[0] * a[1]) // abs(a[1]), abs(a[1]))
        if a[1] == 1:
            if abs(a[1]) >= 1000:
                return '\\nombre{%i}' % a[0]
            else:
                return '%i' % a[0]
        else:
            if abs(a[0]) >= 1000:
                if abs(a[1]) >= 1000:
                    return '\\dfrac{\\nombre{%s}}{\\nombre{%s}}' % a
                else:
                    return '\\dfrac{\\nombre{%s}}{%s}' % a
            elif abs(a[1]) >= 1000:
                return '\\dfrac{%s}{\\nombre{%s}}' % a
            else:
                return '\\dfrac{%s}{%s}' % a

def simplifie(a):  #renvoie la fraction a simplifiee
    b = pgcd(a[0], a[1])
    if b != 1:
        return (a[0] // b, a[1] // b)
    else:
        return ''

def decomp_prod(a, b):  #renvoie un tuple contenant les deux fractions apres simplification et un tuple contenant les nb par lesquels on simplifie le produit de fractions
    c = pgcd(a[0], b[1])
    d = pgcd(a[1], b[0])
    sgn1 = signe(a[1])
    sgn2 = signe(b[1])
    if c == d == 1:
        return (((sgn1 * a[0]) // c, (sgn1 * a[1]) // d), ((sgn2 * b[0]) // d, (sgn2 * b[1]) // c), '')
    else:
        return (((sgn1 * a[0]) // c, (sgn1 * a[1]) // d), ((sgn2 * b[0]) // d, (sgn2 * b[1]) // c), (c, d))

def tex_decomp_prod(a):  #renvoie l'ecriture au format tex de la decomposition d'un produit
    if not isinstance(a[2], tuple):  # pas de decomposition possible
        return ''
    elif a[2][0] == 1:
        b = (a[0][0], a[0][1], a[2][1], a[1][0], a[2][1], a[1][1]) # decomposition que du denominateur
        return '\\dfrac{%s}{%s\\times\\bcancel{%s}}\\times\\dfrac{%s\\times\\bcancel{%s}}{%s}' % b
    elif a[2][1] == 1:
        b = (a[0][0], a[2][0], a[0][1], a[1][0], a[1][1], a[2][0])  # decomposition que du numerateur
        return '\\dfrac{%s\\times\\cancel{%s}}{%s}\\times\\dfrac{%s}{%s\\times\\cancel{%s}}' % b
    else:
        b = (a[0][0], a[2][0], a[0][1], a[2][1], a[1][0], a[2][1], a[1][1], a[2][0]) # decomposition du numerateur et du denominateur
        return '\\dfrac{%s\\times\\cancel{%s}}{%s\\times\\bcancel{%s}}\\times\\dfrac{%s\\times\\bcancel{%s}}{%s\\times\\cancel{%s}}' % b

def produit(a, b):  #renvoie un tuple contenant le produit des fractions a et b
    sgn1 = signe(a[1] * b[1])
    return ((sgn1 * a[0]) * b[0], (sgn1 * a[1]) * b[1])

def den_com0(a, b):  #renvoie un tuple contenant les 2 nombres par lesquels multiplier les deux denominateurs pour obtenir leur ppcm
    c = ppcm(a[1], b[1])
    return (abs(c // a[1]), abs(c // b[1]))

#
# ------------------- AFFICHAGE -------------------
def tex_valeur(a, nb, cor):  # repond a la question sur la valeur de x
    cor.append(u'$$ A = ' + tex_valeurx0(a, nb) + '$$')
    if nb == (0, 1):
        cor.append(u'$$ \\boxed{A = ' + tex_valeurx1(a, nb) + '} $$')
    else:
        cor.append(u'$$ A = ' + tex_valeurx1(a, nb) + '$$')
        b = decomp_prod((a[0], 1), (nb[0] ** 2, nb[1] ** 2))[0:2]
        c = decomp_prod((a[1], 1), (nb[0], nb[1]))[0:2]
        a = (produit(b[0], b[1]), produit(c[0], c[1]), (a[2], 1))
        if a[0][1] == a[1][1] == 1:
            cor.append(u'$$ \\boxed{A = ' + tex_valeurx2(a, nb) + '} $$')
        else:
            cor.append(u'$$ A = ' + tex_valeurx2(a, nb) + '$$')
            cor.append(u'$$ \\boxed{A = ' + tex_valeurx3(a, nb) + '} $$')

def tex_valeurx0(a, nb):
    if nb == (0, 1):
        return '%s%s%s' % (tex_coef(a[0], '%s^2' % tex_frac(nb)), tex_coef(a[1], '%s' % tex_frac(nb),bplus=a[0]), tex_coef(a[2], '', bplus=a[0] or a[1]))
    else:
        return '%s%s%s' % (tex_coef(a[0], '\\left(%s\\right)^2' % tex_frac(nb)), tex_coef(a[1], '\\left(%s\\right)' % tex_frac(nb), bplus=a[0]), tex_coef(a[2], '', bplus=a[0] or a[1]))  

def tex_valeurx1(a, nb):
    if nb == (0, 1):
        return tex_coef(a[2], '')
    elif nb[1] == 1:
        return tex_coef(a[0] * nb[0] ** 2, '') + tex_coef(a[1] * nb[0], '', bplus=a[0]) + tex_coef(a[2], '', bplus=a[0] or a[1])
    else:
        texte = ''
        if a[0] != 0:
            a0 = ((a[0], 1), (nb[0] ** 2, nb[1] ** 2))
            if isinstance(decomp_prod(a0[0], a0[1])[2], tuple):
                texte = tex_coef(1, tex_decomp_prod(decomp_prod(a0[0], a0[1])))
            else:
                texte = tex_coef(1, tex_frac(produit(a0[0], a0[1])))
        if a[1] != 0:
            a1 = ((a[1], 1), (nb[0], nb[1]))
            if isinstance(decomp_prod(a1[0], a1[1])[2], tuple):
                texte = texte + tex_coef(1, tex_decomp_prod(decomp_prod(a1[0], a1[1])), bplus=a[0])
            else:
                texte = texte + tex_coef(1, tex_frac(produit(a1[0], a1[1])), bplus=a[0])
        texte = texte + tex_coef(a[2], '', bplus=1)
        return texte

def tex_valeurx2(a, nb):
    if nb == (0, 1):
        return ''
    else:
        if a[0][1] == a[1][1] == 1:
            return tex_coef(a[0][0] + a[1][0] + a[2][0], '')
        else:
            c = den_com0(a[0], a[1])
            texte = ''
            if a[0][0] != 0:
                texte = tex_coef(1, tex_frac((a[0][0] * c[0], a[0][1] * c[0])))
            if a[1][0] != 0:
                texte = texte + tex_coef(1, tex_frac((a[1][0] * c[1], a[1][1] * c[1])), bplus=texte)
            if a[2][0] != 0:
                texte = texte + tex_coef(1, tex_frac(((a[2][0] * a[0][1]) * c[0], a[0][1] * c[0])), bplus=texte)
            return texte

def tex_valeurx3(a, nb):
    if nb == (0, 1) or a[0][1] == a[1][1] == 1:
        return ''
    else:
        c = den_com0(a[0], a[1])
        b = (a[0][0] * c[0] + a[1][0] * c[1] + (a[2][0] * a[0][1]) * c[0], a[0][1] * c[0])
        if simplifie(b):
            return tex_frac(b) + '=' + tex_frac(simplifie(b))
        else:
            return tex_frac(b)

#
# ------------------- GENERATION DES VALEURS -------------------
def valeur_expression_binome(nombre_min, nombre_max):
    (b, c) = (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max))
    return ((0, b, c))

def valeur_expression_trinome(nombre_min, nombre_max): 
    (a, b, c) = (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max))
    return ((a, b, c))

def valeur_relatif(nombre_min, nombre_max):
    (a, b) = (valeur_alea(nombre_min, nombre_max), 1 )
    return (a, b)

def valeur_quotient(nombre_min, nombre_max):
    (a, b) = (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max))
    while pgcd(a, b) == b:
        (a, b) = (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max))
    return (a // pgcd(a, b), b // pgcd(a, b))

#
# ------------------- CONSTRUCTION EXERCICE -------------------
def tex_exercice(expression, valeurs):
    question = "Calculer :"
    exo = []
    cor = []
    variable = variable_list[ random.randrange(7) ]
    exo.append("$ A = %s $ pour $ %s = %s $" % (tex_trinome(expression, variable), variable, tex_frac(valeurs)))
    cor.append("$ A = %s $ pour $ %s = %s $" % (tex_trinome(expression, variable), variable, tex_frac(valeurs)))
    tex_valeur(expression, valeurs, cor)
    return (exo, cor, question)

def RelatifBinome(parametre):
    valeurs = valeur_relatif(parametre[0], parametre[1])
    expression = valeur_expression_binome(parametre[0], parametre[1])
    (exo, cor, question) = tex_exercice(expression, valeurs)
    return (exo, cor, question)

def FractionBinome(parametre):
    valeurs = valeur_quotient(parametre[0], parametre[1])
    expression = valeur_expression_binome(parametre[0], parametre[1])
    (exo, cor, question) = tex_exercice(expression, valeurs)
    return (exo, cor, question)

def RelatifTrinome(parametre):
    valeurs = valeur_relatif(parametre[0], parametre[1])
    expression = valeur_expression_trinome(parametre[0], parametre[1])
    (exo, cor, question) = tex_exercice(expression, valeurs)
    return (exo, cor, question)

def FractionTrinome(parametre):
    valeurs = valeur_quotient(parametre[0], parametre[1])
    expression = valeur_expression_trinome(parametre[0], parametre[1])
    (exo, cor, question) = tex_exercice(expression, valeurs)
    return (exo, cor, question)
