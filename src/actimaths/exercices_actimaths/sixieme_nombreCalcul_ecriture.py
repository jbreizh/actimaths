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
# Écrire un nombre en lettres ou en chiffres
#===============================================================================

def nombreATrouver(nombre_min, nombre_max, style):
    if style == 1:
        e = random.randrange(1, 4)
        nombre = random.randrange(nombre_min* 10 ** (e), nombre_max* 10 ** (e))
        nombre = nombre * 10 ** (-e)
    else:
        nombre = random.randrange(nombre_min, nombre_max)
    return nombre

def NombreEnLettres(n, France=True):
    unite = {
        1: "un",
        2: 'deux',
        3: 'trois',
        4: 'quatre',
        5: 'cinq',
        6: 'six',
        7: 'sept',
        8: 'huit',
        9: 'neuf',
        10: 'dix',
        11: 'onze',
        12: 'douze',
        13: 'treize',
        14: 'quatorze',
        15: 'quinze',
        16: 'seize',
        17: 'dix-sept',
        18: 'dix-huit',
        19: 'dix-neuf',
        }
    dizaineF = {2: 'vingt', 3: 'trente', 4: 'quarante', 5: 'cinquante',
                6: 'soixante', 7: "", 8: 'quatre-vingt', 9: ""}
    dizaineB = {2: 'vingt', 3: 'trente', 4: 'quarante', 5: 'cinquante',
                6: 'soixante', 7: 'septante', 8: 'octante', 9: 'nonante'}
    coefs = {0: 'cent', 1: 'mille', 2: 'million', 3: 'milliard'}
    result = ""

  # Cas particulier de zéro
    if n == 0:
        result = u'zéro'
    else:
        coef = 0

        while n > 0:

        # Récupération de l'unité du bloc de trois chiffres en cours

            u = n % 10
            n = n // 10

        # Récupération de la dizaine du bloc de trois chiffres en cours

            d = n % 10
            n = n // 10
        # Traitement des dizaines

            temp = ""

        # Passage sur la dizaine inférieure pour 10 à 19
        # et pour 70-79 90-99 dans le cas de la France

            if d == 1 or (d == 7 or d == 9) and France:
                d = d - 1
                u = u + 10
            if d > 1:
                if France:
                    if n:
                        temp = '-' + dizaineF[d]
                    else:
                        temp = dizaineF[d]

            # Ajout du cas particulier de 'et' entre la dizaine et 1

                    if d < 8 and (u == 1 or u == 11):
                        temp = temp + '-et'
                else:
                    if n:
                        temp = '-' + dizaineB[d]
                    else:
                        temp = dizaineB[d]

              # Ajout du cas particulier de 'et' entre la dizaine et 1

                    if u == 1:
                        temp = temp + '-et'

        # ajout du texte de l'unité

            if u > 0 and (d or n):
                temp = temp + '-' + unite[u]
            elif u > 0:
                temp = unite[u]

        # ajout du 's' à Quatre-vingt si rien ne suit
        #if (result == '') and (d == 8) and (u == 0) and France : result = 's'

            if d == 8 and u == 0 and France:
                temp = temp + 's'
            result = temp + result


        # Récupération de la centaine du bloc de trois chiffres en cours

            c = n % 10
            n = n // 10
            if c > 0:
                temp = ""
                if c > 1 and n:
                    temp = '-' + unite[c]
                elif c > 1:
                    temp = unite[c]
                if c == 1 and not n:
                    temp = coefs[0]
                else:
                    temp = temp + '-' + coefs[0]

          # Traitement du cas particulier du 's' à cent si rien ne suit

                if result == "" and c > 1:
                    result = 's'
                result = temp + result

        # Traitement du prochain groupe de 3 chiffres

            if n > 0:
                coef = coef + 1
                i = n % 1000
                if i > 1 and coef > 1:
                    result = 's' + result

          # Traitement du cas particulier 'mille' ( non pas 'un mille' )

                if i == 1 and coef == 1:
                    n = n - 1
                    result = coefs[coef] + result
                elif i > 0:

                    result = '-' + coefs[coef] + result
    return result

def EcritNombreDecimal(n):
    txt = ""
    if n != int(n):
        #n n'est pas un nombre entier
        (e, d) = str(n).split('.')
        (e, d) = (int(e), int(d))
    else:
        (e, d) = (int(n), 0)
    if not d:
        txt = NombreEnLettres(e)
    elif e:
        txt = NombreEnLettres(e)
    if d:
        partieDec = [u" dixième", u" centième", u" millième"]
        if txt.rfind("un") == len(txt) - 2:

        # le texte se finit par un. On l'accorde en genre avec unité

            txt = txt + "e"
        if e == 1:
            txt = txt + u' unité et '
        if e > 1:
            txt = txt + u' unités et '
        txt = txt + NombreEnLettres(d) + partieDec[len(str(n).split('.')[1]) -
                1]
        if d > 1:
            txt = txt + 's'
    return txt

def EcritEnChiffreEntier(parametre):
    question = u"Écrire en chiffres :"
    exo = []
    cor = []
    lnb = nombreATrouver(parametre[0], parametre[1], 0)
    exo.append(EcritNombreDecimal(lnb))
    cor.append(Affichage.decimaux(lnb, 0) + '')
    return (exo, cor, question)

def EcritEnLettreEntier(parametre):
    question = u"Écrire en lettres :"
    exo = []
    cor = []
    lnb = nombreATrouver(parametre[0], parametre[1], 0 )
    exo.append(Affichage.decimaux(lnb, 0))
    cor.append(EcritNombreDecimal(lnb) + '')
    return (exo, cor, question)

def EcritEnChiffreDecimal(parametre):
    question = u"Écrire en chiffres :"
    exo = []
    cor = []
    lnb = nombreATrouver(parametre[0], parametre[1], 1)
    exo.append(EcritNombreDecimal(lnb))
    cor.append(Affichage.decimaux(lnb, 0) + '')
    return (exo, cor, question)

def EcritEnLettreDecimal(parametre):
    question = u"Écrire en lettres :"
    exo = []
    cor = []
    lnb = nombreATrouver(parametre[0], parametre[1], 1)
    exo.append(Affichage.decimaux(lnb, 0))
    cor.append(EcritNombreDecimal(lnb) + '')
    return (exo, cor, question)
