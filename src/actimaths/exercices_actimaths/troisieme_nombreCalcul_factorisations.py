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

from outils.Arithmetique import valeur_alea
from outils.Affichage import tex_dev0, tex_dev1, tex_trinome, tex_binome
import random

variable_list = ['x', 'y', 'a', 'b', 'k', 'm', 'p']
#
# ------------------- FACTORISATIONS -------------------

def coef_opposes(a):  # renvoie un tuple dont les valeurs sont les opposees de celles de a
    l = []
    for i in range(len(a)):
        l.append(-a[i])
    return tuple(l)


def dev(a):  # renvoi un tuple avec les 3 coefficients du developpement
    return (a[0][0] * a[1][0], a[0][0] * a[1][1] + a[0][1] * a[1][0], a[0][1] * a[1][1])


def somme_polynomes(a, b):  # renvoie un tuple dont les valeurs sont les sommes des valeurs correspondantes dans a et b
    l = []
    if len(a) > len(b):
        long = len(a)
    else:
        long = len(b)
    for i in range(long):
        if (len(a) - i) - 1 < 0:
            l.append(b[(len(b) - 1) - i])
        elif (len(b) - i) - 1 < 0:
            l.append(a[(len(a) - 1) - i])
        else:
            l.append(a[(len(a) - 1) - i] + b[(len(b) - 1) - i])
    l.reverse()
    return tuple(l)

def facteur_commun(a, b):  #renvoie le facteur commun et les les deux autres binomes
    if a[0] == b[0]:  # recherche le facteur commun et le nomme f0, f1 et f2 etant les deux autres facteurs
        (f0, f1, f2) = (a[0], a[1], b[1])
    elif a[0] == b[1]:
        (f0, f1, f2) = (a[0], a[1], b[0])
    elif a[1] == b[0]:
        (f0, f1, f2) = (a[1], a[0], b[1])
    elif a[1] == b[1]:
        (f0, f1, f2) = (a[1], a[0], b[0])
    return (f0, f1, f2)


def facteur_commun2(f, nega, negb):  # renvoie (2x+3)(4x+5+6x+7) sous la forme ((2,3),(4,5),(6,7))
    if nega:
        if negb:
            return (f[0], coef_opposes(f[1]), coef_opposes(f[2]))
        else:
            return (f[0], coef_opposes(f[1]), f[2])
    elif negb:
        return (f[0], f[1], coef_opposes(f[2]))
    else:
        return (f[0], f[1], f[2])


def facteur_commun3(f, nega, negb):  # renvoie un tuple contenant les deux binomes finaux de la mise en facteur
    if nega and negb:
        return (f[0], somme_polynomes(coef_opposes(f[1]), coef_opposes(f[2])))
    elif nega:
        return (f[0], somme_polynomes(coef_opposes(f[1]), f[2]))
    elif negb:
        return (f[0], somme_polynomes(f[1], coef_opposes(f[2])))
    else:
        return (f[0], somme_polynomes(f[1], f[2]))


#
# ------------------- AFFICHAGE -------------------
#Type 0

def tex_type0(valeurs, variable, cor, exo=None):  # ecrit toutes les etapes de la factorisation
    (a, b, nega, negb) = valeurs
    f = facteur_commun(a, b)
    if exo:
        exo.append(u'$$ A = ' + tex_type0_0(valeurs, variable) + '$$')
    cor.append(u'$$ A = ' + tex_type0_0(valeurs, variable) + '$$')
    cor.append(u'$$ A = ' + tex_type123_1(f, variable, nega, negb) + '$$')
    f2 = facteur_commun2(f, nega, negb)
    if nega and f2[1][0] != 0 and f2[1][1] != 0 or negb and f2[2][0] != 0 and f2[2][0] != 0:
        cor.append(u'$$ A = ' + tex_type123_2(f2, variable) + '$$')
    cor.append(u'$$ \\boxed{A = ' + tex_dev0((f2[0], somme_polynomes(f2[1], f2[2])), variable) + '} $$')

def tex_type0_0(valeurs, variable):  #renvoie -(2x+3)+(2x+3)(3x+6)
    ligne = ''
    if valeurs[2]:
        ligne += '-'

    if valeurs[0][1][0]== 0:
        ligne += '(' + tex_dev0(valeurs[0], variable)+ ')'
    else:
        ligne += tex_dev0(valeurs[0], variable)

    if valeurs[3]:
        ligne += '-'
    else:
        ligne += '+'

    if valeurs[1][1][0]== 0:
        ligne += '(' + tex_dev0(valeurs[1], variable)+ ')'
    else:
        ligne += tex_dev0(valeurs[1], variable)
    return ligne


#Type 1 ; 2 et 3
def tex_type123(valeurs, variable, cor, exo=None):  # ecrit toutes les etapes de la factorisation
    (a, b, nega, negb) = valeurs
    f = facteur_commun(a, b)
    if exo:
        exo.append(u'$$ A = ' + tex_type123_0(valeurs, variable) + '$$')
    cor.append(u'$$ A = ' + tex_type123_0(valeurs, variable) + '$$')
    cor.append(u'$$ A = ' + tex_type123_1(f, variable, nega, negb) + '$$')
    f2 = facteur_commun2(f, nega, negb)
    if nega and f2[1][0] != 0 and f2[1][1] != 0 or negb and f2[2][0] != 0 and f2[2][0] != 0:
        cor.append(u'$$ A = ' + tex_type123_2(f2, variable) + '$$')
    cor.append(u'$$ \\boxed{A = ' + tex_dev0((f2[0], somme_polynomes(f2[1], f2[2])), variable) + '} $$')

def tex_type123_0(valeurs, variable):  #renvoie -(2x+3)(x+5)+(2x+3)(3x+6)
    if valeurs[2]:
        if valeurs[3]:
            return '-' + tex_dev0(valeurs[0], variable) + '-' + tex_dev0(valeurs[1], variable)
        else:
            return '-' + tex_dev0(valeurs[0], variable) + '+' + tex_dev0(valeurs[1], variable)
    elif valeurs[3]:
        return tex_dev0(valeurs[0], variable) + '-' + tex_dev0(valeurs[1], variable)
    else:
        return tex_dev0(valeurs[0], variable) + '+' + tex_dev0(valeurs[1], variable)

def tex_type123_1(f, variable, nega, negb):  # renvoie (2x+3)(-(x+5)+3x+6)
    texte = tex_binome(f[0], variable, bpar=1)
    if nega or negb:
        texte = texte + '\\,\\big( '
    else:
        texte = texte + '\\,('
    if nega:
        texte = texte + '-' + tex_binome(f[1], variable, bpar=1)
    else:
        texte = texte + tex_binome(f[1], variable, bpar=0)
    if negb:
        texte = texte + '-' + tex_binome(f[2], variable, bpar=1)
    else:
        texte = texte + tex_binome(f[2], variable, bplus=1)
    if nega or negb:
        texte = texte + '\\big)'
    else:
        texte = texte + ')'
    return texte

def tex_type123_2(valeurs, variable):  # renvoie renvoie (2x+3)(-x-5+3x+6)
    return tex_binome(valeurs[0], variable, bpar=1) + '\\,(' + tex_binome(valeurs[1], variable) + tex_binome(valeurs[2], variable, bplus=1) + ')'

#Type5
def tex_type5(valeurs, variable, cor, exo):  # ecrit toutes les etapes de la factorisation
    if exo:
        exo.append(u'$$ A = ' + tex_type5_0(valeurs, variable) + '$$')
    cor.append(u'$$ A = ' + tex_type5_0(valeurs, variable) + '$$')
    cor.append(u'$$ A = ' + '%s^2-%s^2' % (tex_binome(valeurs[0], variable, bpar=1), tex_binome(valeurs[1], variable, bpar=1)) + '$$')
    cor.append(u'$$ A = ' + tex_type5_2(valeurs, variable) + '$$')
    if valeurs[0][0] == 0:
        cor.append(u'$$ A = ' + tex_type5_3(valeurs, variable) + '$$')
    cor.append(u'$$ \\boxed{A = ' + tex_dev0((somme_polynomes(valeurs[0], valeurs[1]), somme_polynomes(valeurs[0], coef_opposes(valeurs[1]))), variable) + '} $$')


def tex_type5_0(valeurs, variable):  # renvoie 16-(2x+3)²
    if valeurs[0][0] == 0:
        return '%s-%s^2' % (valeurs[0][1] ** 2, tex_binome(valeurs[1], variable, bpar=1))
    else:
        return '%s^2-%s' % (tex_binome(valeurs[0], variable, bpar=1), valeurs[1][1] ** 2)


def tex_type5_2(valeurs, variable):  # renvoie (4+2x+3)(4-(2x+3))
    if valeurs[0][0] == 0:
        return '(%s%s)\\,\\big( %s-%s\\big)' % (tex_binome(valeurs[0], variable), tex_binome(valeurs[1], variable, bplus=1), tex_binome(valeurs[0], variable), tex_binome(valeurs[1], variable, bpar=1))
    else:
        return '(%s%s)\\,(%s-%s)' % (tex_binome(valeurs[0], variable), tex_binome(valeurs[1], variable, bplus=1), tex_binome(valeurs[0], variable), tex_binome(valeurs[1], variable, bpar=1))


def tex_type5_3(valeurs, variable):  # renvoie (4+2x+3)(4-2x-3)
    return '(%s%s)\\,(%s%s)' % (tex_binome(valeurs[0], variable), tex_binome(valeurs[1], variable, bplus=1), tex_binome(valeurs[0], variable), tex_binome(coef_opposes(valeurs[1]), variable, bplus=1))

#Type 4; 6 et 7
def tex_type467(valeurs, variable, cor, exo):  # ecrit toutes les etapes de la factorisation
    if exo:
        exo.append(u'$$ A = ' + tex_trinome(dev(valeurs), variable) + '$$')
    cor.append(u'$$ A = ' + tex_trinome(dev(valeurs), variable) + '$$')
    cor.append(u'$$ A = ' + tex_dev1(valeurs, variable) + '$$')
    cor.append(u'$$  \\boxed{A = ' + tex_dev0(valeurs, variable) + '} $$')

#
# ------------------- GENERATION DES VALEURS -------------------

def valeurs_type0(nombre_min, nombre_max):  # renvoie les valeurs pour obtenir un facteur commun et un facteur 1
    a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
    while a[0] == a[1]:  # on refuse un carre
       a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))

    b = (a[random.randrange(2)], (0, 1))
    if random.randrange(2) == 1:  # le 1 est dans le deuxieme terme
        return (a, b, random.randrange(2), random.randrange(2))
    else:
        return (b, a, random.randrange(2), random.randrange(2))

def valeurs_type1(nombre_min, nombre_max):  # renvoie les valeurs pour obtenir un facteur commun et un facteur entier relatif
    a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
    while a[0] == a[1]:  # on refuse un carre
        a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))

    c = valeur_alea(nombre_min, nombre_max)

    while c == 1:
        c = valeur_alea(nombre_min, nombre_max)

    b = (a[random.randrange(2)], (0, c))
    if random.randrange(2) == 1:  # l'entier relatif est dans le deuxieme terme
        return (a, b, random.randrange(2), random.randrange(2))
    else:
        return (b, a, random.randrange(2), random.randrange(2))

def valeurs_type2(nombre_min, nombre_max):  # renvoie les valeurs pour obtenir un facteur commun.
    a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
    while a[0] == a[1]:  # on refuse un carre
        a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
    if random.randrange(2) == 0:
        while True:
            b = (a[random.randrange(2)], (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
            if b[0] != b[1]:
                break
    else:
        while True:
            b = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), a[random.randrange(2)])
            if b[0] != b[1]:
                break
    (nega, negb) = (random.randrange(2), random.randrange(2))
    return (a, b, nega, negb)

def valeurs_type3(nombre_min, nombre_max):  # renvoie les valeurs pour obtenir un facteur commun au carre
    a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
    while a[0] == a[1]:  # on refuse un carre
        a = ((valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)), (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max)))
    if random.randrange(2) == 0:
        b = (a[0], a[0])
    else:
        b = (a[1], a[1])
    if random.randrange(2) == 0:  # le carre est en premier
        return (b, a, 0, random.randrange(2))
    else:
        return (a, b, random.randrange(2), 0)

def valeurs_type4(nombre_min, nombre_max):  # renvoie un tuple contenant ((3,-5),(3,+5))
    a = valeur_alea(nombre_min, nombre_max)
    b = valeur_alea(nombre_min, nombre_max)
    if random.randrange(2):
        return ((a, -b), (a, b))
    else:
        return ((a, b), (a, -b))

def valeurs_type5(nombre_min, nombre_max):  # renvoie les valeurs pour obtenir a²-(bx+c)²
    a = (0, valeur_alea(nombre_min, nombre_max))
    b = (valeur_alea(nombre_min, nombre_max), valeur_alea(nombre_min, nombre_max))
    if random.randrange(2) == 0:  #  le nombre est en premier
        return (a, b)
    else:
        return (b, a)

def valeurs_type6(nombre_min, nombre_max):  # renvoie un tuple contenant ((3,+5),(3,+5))
    a = valeur_alea(nombre_min, nombre_max)
    b = valeur_alea(nombre_min, nombre_max)
    return ((a, b), (a, b))

def valeurs_type7(nombre_min, nombre_max):  # renvoie un tuple contenant ((3,-5),(3,-5))
    a = valeur_alea(nombre_min, nombre_max)
    b = valeur_alea(nombre_min, nombre_max)
    return ((a, -b), (a, -b))
#
# ------------------- TYPE DE FACTORISATION -------------------


def factorisation0(exo, cor, nombre_min, nombre_max, variable):  # factorise (ax+b)(cx+d)+(ax+b)
    valeurs = valeurs_type0(nombre_min, nombre_max)
    tex_type0(valeurs, variable, cor, exo)

def factorisation1(exo, cor, nombre_min, nombre_max, variable):  # factorise (ax+b)(cx+d)+(ax+b)e
    valeurs = valeurs_type1(nombre_min, nombre_max)
    tex_type123(valeurs, variable, cor, exo)

def factorisation2(exo, cor, nombre_min, nombre_max, variable):  # factorise (ax+b)(cx+d)+(ax+b)(ex+f)
    valeurs = valeurs_type2(nombre_min, nombre_max)
    tex_type123(valeurs, variable, cor, exo)

def factorisation3(exo, cor, nombre_min, nombre_max, variable):  # factorise (ax+b)(cx+d)+(ax+b)²
    valeurs = valeurs_type3(nombre_min, nombre_max)
    tex_type123(valeurs, variable, cor, exo)

def factorisation4(exo, cor, nombre_min, nombre_max, variable):  # factorise a²-b²
    valeurs = valeurs_type4(nombre_min, nombre_max)
    tex_type467(valeurs, variable, cor, exo)

def factorisation5(exo, cor, nombre_min, nombre_max, variable):  #factorise 64-(x-5)²
    valeurs = valeurs_type5(nombre_min, nombre_max)
    tex_type5(valeurs, variable, cor, exo)

def factorisation6(exo, cor, nombre_min, nombre_max, variable):  #factorise ax²+bx+c
    valeurs = valeurs_type6(nombre_min, nombre_max)
    tex_type467(valeurs, variable, cor, exo)   

def factorisation7(exo, cor, nombre_min, nombre_max, variable):  #factorise ax²-bx +c
    valeurs = valeurs_type7(nombre_min, nombre_max)
    tex_type467(valeurs, variable, cor, exo)     

#
# ------------------- CONSTRUCTION EXERCICE -------------------

def construction(nombre_min, nombre_max, style):
    question = "Factoriser :"
    exo = []
    cor = []
    variable = variable_list[ random.randrange(7) ]
    exo.append("\\begin{tiny}")
    cor.append("\\begin{tiny}")
    exec('factorisation' + str(style) + '(exo, cor, nombre_min, nombre_max, variable)')
    exo.append("\\end{tiny}")
    cor.append("\\end{tiny}")
    return (exo, cor, question)

def Type0(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 0)
    return (exo, cor, question)
    
def Type1(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 1)
    return (exo, cor, question)

def Type2(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 2)
    return (exo, cor, question)

def Type3(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 3)
    return (exo, cor, question)

def Type4(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 4)
    return (exo, cor, question)

def Type5(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 5)
    return (exo, cor, question)

def Type6(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 6)
    return (exo, cor, question)

def Type7(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 7)
    return (exo, cor, question)
