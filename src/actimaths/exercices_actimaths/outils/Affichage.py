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

import re
from .decimaux import decimaux
import Racine, Fractions
from .Arithmetique import  signe, pgcd

def is_int(a):
    # Return true if a is an interger
    try:
        int (a)
        return True
    except:
        return False

def tex_coef(coef, var, bplus=0, bpn=0, bpc=0):

    # coef est le coefficient à écrire devant la variable var
    # bplus est un booleen : s'il est vrai, il faut ecrire le signe +
    # bpn est un booleen : s'il est vrai, il faut mettre des parentheses autour de l'ecriture si coef est negatif.
    # bpc est un booleen : s'il est vrai, il faut mettre des parentheses autour de l'ecriture si coef =! 0 ou 1 et var est non vide

    if abs(coef) >= 1000:
        coefficient = '\\nombre{%s}' % coef
    else:
        coefficient = '%s' % coef

    if is_int(var) and abs(var) >= 1000:
        variable = '\\nombre{%s}' % var
    else:
        variable = '%s' % var

    if coef != 0 and abs(coef) != 1:
        if not var:
            a = '%s' % coefficient
        else:
            if is_int(var):
                a = '%s \\times %s' % (coefficient, variable)
            else:
                a = '%s \\, %s' % (coefficient, variable)
        if bplus and coef > 0:
            a = '+' + a

    elif coef == 1:
        if not var:
            a = '1'
        else:
            a = '%s' % variable
        if bplus:
            a = '+' + a

    elif coef == 0:
        a = ''

    elif coef == -1:
        if not var:
            a = '-1'
        else:
            a = '-%s' % variable

    if bpn and coef < 0 or bpc and coef != 0 and coef != 1 and var:
        a = '\\left( ' + a + '\\right)'
    return a

def tex_binome(a, var, bplus=0, bpar=0):  # renvoi le binome ax+b

    # bplus est un booleen : s'il est vrai, le premier terme est precede d'un signe + si son coefficient est positif.
    # bpar est un booleen : s'il est vrai, ecrit des parentheses autour du binome si les deux coef ne sont pas nuls ou si le seul coef est -

    texte = '%s%s' % (tex_coef(a[0], var, bplus=bplus), tex_coef(a[1],'', bplus=bplus or a[0] != 0))
    if bpar:
        if (a[0] != 0 or a[1] < 0) and (a[1] != 0 or a[0] < 0):
            texte = '(' + texte + ')'
    return texte

def tex_trinome(a, var, bplus=0, bpar=0):  # renvoi le trinome ax²+bx+c

    # bplus est un booleen : s'il est vrai, le premier terme est precede d'un signe + si son coefficient est positif.
    # bpar est un booleen : s'il est vrai, ecrit des parentheses autour du trinome si deux valeurs au moins ne sont pas nulles ou si la valeur est -

    texte = '%s%s%s' % (tex_coef(a[0], '%s^{2}' % var, bplus=bplus), tex_coef(a[1], var, bplus=bplus or a[0] != 0), tex_coef(a[2],'', bplus=bplus or a[0] != 0 or a[1] != 0))
    if bpar:
        v0 = 0
        for i in range(3):  # compte le nombre de valeurs nulles
            if a[i] == 0:
                v0 = v0 + 1
        if v0 == 2:  # une seule valeur non nulle (on suppose que les trois coef ne sont pas nuls)
            if a[0] < 0 or a[1] < 0 or a[2] < 0:  # le coefficient non nul est negatif, il faut donc des parentheses
                return '(' + texte + ')'
            else:
                return texte
        else:
            return '(' + texte + ')'
    else:
        return texte

def tex_dev0(a, var, bplus=0):  # renvoi (a+b)², (a-b)² ou (a+b)(c+d) ou a(c+d) ou (a+b)*c

    # a est de la forme ((3, 2), (3, 2)) pour (3x+2)(3x+2)
    # var est de la forme 'x' ou 'y' ou '3'

    (ca, cb, cc, cd) = (a[0][0], a[0][1], a[1][0], a[1][1])  # coefficients a, b, c et d
    if ca == 0 and cb == 0 or cc == 0 and cd == 0:
        return '0'
    elif a[0] == a[1]:

                        # (a+b)² ou (a-b)²

        if ca == 0:
            return '%s^2' % tex_coef(cb, '', bpn=1)
        elif cb == 0:
            return '%s^2' % tex_coef(ca, var, bpc=1)
        else:
            return '(%s%s)^2' % (tex_coef(ca, var), tex_coef(cb, '', bplus=1))
    else:

        # (a+b)(c+d)

        if ca == 0 or cb == 0:
            if cc == 0 or cd == 0:
                return '%s%s\\times %s%s' % (tex_coef(ca, var), tex_coef(cb, '', bplus=ca != 0), tex_coef(cc, var, bpn=1), tex_coef(cd, '', bplus=cc != 0, bpn=1))
            else:
                return '%s%s\\,(%s%s)' % (tex_coef(ca, var), tex_coef(cb,'', bplus=ca != 0), tex_coef(cc, var), tex_coef(cd,'', bplus=cc != 0))
        elif cc == 0 or cd == 0:
            if cc == 0 and cd == 1:
                return '%s%s' % (tex_coef(ca, var, bplus=bplus),tex_coef(cb, '', bplus=ca != 0))
            else:
                return '(%s%s)\\times %s%s' % (tex_coef(ca, var), tex_coef(cb, '', bplus=ca != 0), tex_coef(cc,var, bpn=1), tex_coef(cd, '', bplus=cc != 0, bpn=1))
        else:
            return '(%s%s)\\,(%s%s)' % (tex_coef(ca, var), tex_coef(cb,'', bplus=1), tex_coef(cc, var), tex_coef(cd, '', bplus=1))


def tex_dev1(a, var, bplus=0, bpar=0, bpn=0):  # renvoi le developpement (a)²+2*a*b+(b)², (a)²-2*a*b+(b)², (a)²-(b)² ou a*c+a*d+b*c+b*d

    # a est de la forme ((3, 2)(3, 2)) pour (3x+2)(3x+2)

    (ca, cb, cc, cd) = (a[0][0], a[0][1], a[1][0], a[1][1])  # coefficients a, b, c et d
    if a[0] == a[1]:  # (a+b)² ou (a-b)²
        if signe(ca) == signe(cb):  # (a+b)²
            (ca, cb) = (abs(ca), abs(cb))
            texte = '%s^2+2\\times %s\\times %s+%s^2' % (tex_coef(ca, var, bpc=1), tex_coef(ca, var, bpn=1), tex_coef(cb,'', bpn=1), tex_coef(cb, '', bpn=1, bpc=1))
            if bpar:
                return '(' + texte + ')'
            else:
                return texte
        else:

            # (a-b)²

            (ca, cb) = (abs(ca), abs(cb))
            texte = '%s^2-2\\times %s\\times %s+%s^2' % (tex_coef(ca, var, bpc=1), tex_coef(ca, var, bpn=1), tex_coef(cb,'', bpn=1), tex_coef(cb, '', bpn=1, bpc=1))
            if bpar:
                return '(' + texte + ')'
            else:
                return texte
    if abs(ca) == abs(cc) and abs(cb) == abs(cd):  # (a+b)(a-b) ou (a+b)(-a+b)
        if ca == cc:  # (a+b)(a-b)
            texte = '%s^2-%s^2' % (tex_coef(ca, var, bpc=1), tex_coef(abs(cb), ''))
            if bpar:
                return '(' + texte + ')'
            else:
                return texte
        else:

            # (a+b)(-a+b)

            texte = '%s^2-%s^2' % (tex_coef(cb, '', bpn=1), tex_coef(abs(ca), var, bpc=1))
            if bpar:
                return '(' + texte + ')'
            else:
                return texte
    else:

        # (a+b)(c+d)

        if cc == 0 and cd == 1:
            texte = '%s%s' % (tex_coef(ca, var, bplus=bplus), tex_coef(cb, '', bplus=ca != 0))
            if bpar:
                return '(' + texte + ')'
            else:
                return texte
        elif ca == 0 or cb == 0 or cc == 0 or cd == 0:
            if ca == 0:
                texte = '%s\\times %s+%s\\times %s' % (tex_coef(cb, '', bpn=bpn), tex_coef(cc, var, bpn=1), tex_coef(cb, '', bpn=1), tex_coef(cd, '', bpn=1))
            elif cb == 0:
                texte = '%s\\times %s+%s\\times %s' % (tex_coef(ca, var, bpn=bpn), tex_coef(cc, var, bpn=1), tex_coef(ca, var, bpn=1), tex_coef(cd, '', bpn=1))
            elif cc == 0:
                texte = '%s\\times %s+%s\\times %s' % (tex_coef(cd, '', bpn=bpn), tex_coef(ca, var, bpn=1), tex_coef(cd, '', bpn=1), tex_coef(cb, '', bpn=1))
            else:
                texte = '%s\\times %s+%s\\times %s' % (tex_coef(cc, var, bpn=bpn), tex_coef(ca, var, bpn=1), tex_coef(cc, var, bpn=1), tex_coef(cb, '', bpn=1))
            return texte
        else:
            texte = '%s+%s+%s+%s' % (tex_coef(ca * cc, '%s^{2}' % var, bpn=bpn), tex_coef(ca * cd, var, bpn=1), tex_coef(cb * cc, var, bpn=1), tex_coef(cb * cd, '', bpn=1))
            if bpar:
                return '(' + texte + ')'
            else:
                return texte

def TeXz(nombre):
    '''n'affiche pas b si b=0'''
    if nombre==0:
        return ""
    else:
        return TeX(nombre)
def tTeX(nombre):
    '''raccourci pour TeX(nombre,terme=True)'''
    return TeX(nombre,terme=True)
def pTeX(nombre):
    '''raccourci pour TeX(nombre,parenthese=True)'''
    return TeX(nombre,parenthese=True)
def fTeX(nombre):
    '''raccourci pour TeX(nombre,fractex="\\frac")'''
    return TeX(nombre,fractex="\\frac")
    
def TeX(nombre,parenthese=False,terme=False,fractex="\\dfrac"):
    '''renvoie une chaine de caractere pour TeX'''
    strTeX=finTeX=""
    
    #Affichage simplifié des racines ou fractions
    if isinstance(nombre,Racine.RacineDegre2) and nombre.radicande==0:
        #Affiche la RacineDegre2 comme une Fractions
        nombre=Fractions.Fractions(nombre.numerateur,nombre.denominateur)
    if isinstance(nombre,Fractions.Fractions) and nombre.denominateur==1:
        #Affiche la Fractions comme un entier
        nombre=nombre.numerateur
    #parentheses des fractions
    if parenthese and (
        isinstance(nombre,Racine.RacineDegre2)
                       and nombre.denominateur==1 and (nombre.numerateur or nombre.coeff<0 )
        #RacineDegre2 avec radicande nécessairement grâce au tri
        or isinstance(nombre,Fractions.Fractions) and nombre.numerateur<0
        or isinstance(nombre,int) and nombre<0
        or isinstance(nombre,float) and nombre<0):
        strTeX="\\left("
        finTeX="\\right)" 
    elif terme and (isinstance(nombre,Racine.RacineDegre2) and
                        (nombre.denominateur!=1 or (nombre.numerateur >0 or nombre.numerateur==0 and nombre.coeff>=0))
                    or nombre>=0) :
        strTeX="+"
        finTeX=""

    ##Affichage
    if nombre==float("inf"):
        return "+\\infty "
    elif nombre==float("-inf"):
        return "-\\infty "
    elif isinstance(nombre,int) or isinstance(nombre,float):
        return strTeX+decimaux(nombre)+finTeX
    elif isinstance(nombre,Fractions.Fractions):
        if nombre.numerateur < 0:
            strTeX += "-"+fractex+"{"+decimaux(-nombre.numerateur)+"}{"+decimaux(nombre.denominateur)+"} "
        else:
            strTeX += fractex+"{"+decimaux(nombre.numerateur)+"}{"+decimaux(nombre.denominateur)+"} "
        strTeX+=finTeX
        return strTeX
    elif isinstance(nombre,Racine.RacineDegre2):
        return strTeX+str(nombre)+finTeX
    else:
        return strTeX+str(nombre)+finTeX

def radicalTeX(n):
    return "\\sqrt{%s}"%(decimaux(n))
