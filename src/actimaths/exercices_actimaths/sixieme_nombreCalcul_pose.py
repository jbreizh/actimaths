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

import math
import random
import string
from outils import Arithmetique, Affichage


def mon_int(t):  # retourne un entier texte sous la forme d'un nombre, zéro sinon
    if t == '':
        t = 0
    elif ('1234567890').count(t):
        t = int(t)
    else:
        t = 0
    return t

def valeurs(nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2):
    while 1:
        nba = Arithmetique.valeur_alea(nbre_min*10**nbre_decimal_1, nbre_max*10**nbre_decimal_1)
        if nba - (nba // 10) * 10:
            break
    while 1:
        nbb = Arithmetique.valeur_alea(nbre_min*10**nbre_decimal_2, nbre_max*10**nbre_decimal_2)
        if nbb - (nbb // 10) * 10:
            break
    nba = nba * 10 ** -nbre_decimal_1
    nbb = nbb * 10 ** -nbre_decimal_2
    deca = [str(nba)[i] for i in range(len(str(nba)))]
    decb = [str(nbb)[i] for i in range(len(str(nbb)))]
    if deca.count('.'):
        posa = deca.index('.')
    else:
        posa = len(deca)
    if decb.count('.'):
        posb = decb.index('.')
    else:
        posb = len(decb)

    lavtvirg = max(posa, posb)
    laprvirg = max(len(deca) - posa, len(decb) - posb)
    return (nba, nbb, deca, decb, lavtvirg, laprvirg)



def lignes(ligne, deca, lavtvirg, laprvirg):
    if deca.count('.'):
        posa = deca.index('.')
    else:
        posa = len(deca)
    if posa < lavtvirg:
        for i in range(lavtvirg - posa):
            ligne.append('')
    for i in range(len(deca)):
        if deca[i] == '.':
            ligne.append(',')
        else:
            ligne.append(str(deca[i]))
    for i in range(laprvirg - (len(deca) - posa)):
        if ligne.count(','):
            ligne.append('0')
        else:
            ligne.append(',')
    return ligne

#---------------methode pour la somme--------------------------------

def retenues_somme(ligne1, ligne2):
    lg = len(ligne1)
    ligne0 = ['' for i in range(lg)]
    for i in range(lg - 1):

        #on déplace la retenue pour qu'elle ne soit pas au-dessus de la virgule

        if ligne1[(lg - i) - 1] == ',' and ligne0[(lg - i) - 1] == '1':
            ligne0[(lg - i) - 1] = ''
            ligne0[(lg - i) - 2] = '1'
        elif mon_int(ligne1[(lg - i) - 1]) + mon_int(ligne2[(lg - i) - 1]) + mon_int(ligne0[(lg - i) - 1]) > 9:
            ligne0[(lg - i) - 2] = '1'
    return ligne0

def tex_somme(exo, cor,nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2):
    (ligne1, ligne2) = ([''], ['+'])
    (nba, nbb, deca, decb, lavtvirg, laprvirg) = valeurs(nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2)
    total = nba + nbb
    dectotal = [str(total)[i] for i in range(len(str(total)))]
    if dectotal.count('.'):
        postotal = dectotal.index('.')
    else:
        postotal = len(dectotal)
    if postotal <= lavtvirg:
        ligne3 = ['']
    else:
        ligne3 = []
    ligne1 = lignes(ligne1, deca, lavtvirg, laprvirg)
    ligne2 = lignes(ligne2, decb, lavtvirg, laprvirg)
    ligne3 = lignes(ligne3, dectotal, lavtvirg, laprvirg)
    ligne0 = retenues_somme(ligne1, ligne2)
    if ligne0[0] == '1':
        ligne0[0] = '\\tiny 1'
    exo.append('$$ %s + %s = \\ldots $$' % (Affichage.decimaux(nba), Affichage.decimaux(nbb)))
    cor.append('\\begin{footnotesize}')
    cor.append('\\begin{tabular}[t]{*{%s}{c}}' % (lavtvirg + laprvirg + 1))
    cor.append('%s \\\\' % ' & \\tiny '.join(ligne0))
    cor.append('%s \\\\' % ' & '.join(ligne1))
    cor.append('%s \\\\\n\\hline' % ' & '.join(ligne2))
    cor.append('%s \\\\' % ' & '.join(ligne3))
    cor.append('\\end{tabular}\\par')
    cor.append('\\end{footnotesize}')
    formule = '%s+%s = %s' % (Affichage.decimaux(nba, 1), Affichage.decimaux(nbb, 1), Affichage.decimaux(nba + nbb, 1))
    cor.append((u'\\[ \\boxed{%s} \\] ').expandtabs(2 * 3) % (formule))

#---------------methode pour la difference--------------------------------

def retenues_diff(ligne1, ligne2):
    lg = len(ligne1)
    ret = 0
    for i in range(lg - 1):
        if not (ligne1[(lg - i) - 1] == ',' and ret):
            if mon_int(ligne1[(lg - i) - 1]) < mon_int(ligne2[(lg - i) -
                    1]) + ret:
                ligne1[(lg - i) - 1] = '$_1$%s' % ligne1[(lg - i) - 1]
                tmpret = 1
            else:
                tmpret = 0
            if ret:
                ligne2[(lg - i) - 1] = '%s$_1$' % ligne2[(lg - i) - 1]
            ret = tmpret
    return (ligne1, ligne2)

def tex_difference(exo, cor, nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2):
    (ligne1, ligne2) = ([''], ['-'])
    (nba, nbb, deca, decb, lavtvirg, laprvirg) = valeurs(nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2)
    if nba < nbb:
        (nba, nbb, deca, decb) = (nbb, nba, decb, deca)
    total = nba - nbb
    dectotal = [str(total)[i] for i in range(len(str(total)))]
    if dectotal.count('.'):
        postotal = dectotal.index('.')
    else:
        postotal = len(dectotal)
    if postotal <= lavtvirg:
        ligne3 = ['']
    else:
        ligne3 = []

    ligne1 = lignes(ligne1, deca, lavtvirg, laprvirg)
    ligne2 = lignes(ligne2, decb, lavtvirg, laprvirg)
    ligne3 = lignes(ligne3, dectotal, lavtvirg, laprvirg)
    (ligne1, ligne2) = retenues_diff(ligne1, ligne2)
    exo.append('$$ %s - %s = \\ldots $$' % (Affichage.decimaux(nba), Affichage.decimaux(nbb)))
    cor.append('\\begin{footnotesize}')
    cor.append('\\begin{tabular}[t]{*{%s}{c}}' % (lavtvirg + laprvirg + 1))
    cor.append('%s \\\\' % ' & '.join(ligne1))
    cor.append('%s \\\\\n\\hline' % ' & '.join(ligne2))
    cor.append('%s \\\\' % ' & '.join(ligne3))
    cor.append('\\end{tabular}\\par')
    cor.append('\\end{footnotesize}')
    formule = '%s-%s = %s' % (Affichage.decimaux(nba, 1), Affichage.decimaux(nbb, 1), Affichage.decimaux(nba - nbb, 1))
    cor.append((u'\\[ \\boxed{%s} \\] ').expandtabs(2 * 3) % (formule))

#---------------methode pour le produit--------------------------------

def valeurs_prod(nbre_min, nbre_max, nbre_decimal_1 , nbre_decimal_2):
    while 1:
        nba = Arithmetique.valeur_alea(nbre_min*10**nbre_decimal_1, nbre_max*10**nbre_decimal_1)
        if nba - (nba // 10) * 10:
            break
    puisa = - nbre_decimal_1
    while 1:
        nbb = Arithmetique.valeur_alea(nbre_min*10**nbre_decimal_2, nbre_max*10**nbre_decimal_2)
        if nbb - (nbb // 10) * 10:
            break
    puisb = - nbre_decimal_2
    return (nba, nbb, puisa, puisb)

def pose_mult(nba, nbb):
    (ligne, total) = ([], 0)
    for i in range(int(math.log10(nbb)) + 1):
        sstotal = ((nbb - (nbb // 10) * 10) * nba) * 10 ** i
        total = total + sstotal
        ligne.append(sstotal)
        nbb = nbb // 10
    return (ligne, total)

def ligneprod(ligne, dec, lg):
    ligne.extend(['' for i in range((lg - len(dec)) - len(ligne))])
    ligne.extend(dec)
    return ligne

def tex_produit(exo, cor, nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2):
    (nba, nbb, puisa, puisb) = valeurs_prod(nbre_min, nbre_max, nbre_decimal_1, nbre_decimal_2)
    deca = [str(nba * 10 ** puisa)[i] for i in range(len(str(nba * 10 ** puisa)))]
    decb = [str(nbb * 10 ** puisb)[i] for i in range(len(str(nbb * 10 ** puisb)))]
    if deca.count('.'):
        i = deca.index('.')
        deca.pop(i)
        deca[i - 1] = '%s ,' % deca[i - 1]
    if decb.count('.'):
        i = decb.index('.')
        decb.pop(i)
        decb[i - 1] = '%s ,' % decb[i - 1] 
    (dec3, total) = pose_mult(nba, nbb)
    total = ((nba * 10 ** puisa) * nbb) * 10 ** puisb
    dec4 = [str(total)[i] for i in range(len(str(total)))]
    if dec4.count('.'):
        i = dec4.index('.')
        if (len(dec4) - i) - 1 < -(puisa + puisb):
            for j in range(-(puisa + puisb) - len(dec4) + i + 1):
                dec4.append('0')  #ajoute les 0 inutiles au produit
        dec4.pop(i)  # supprime le point décimal
        dec4[i - 1] = '%s ,' % dec4[i - 1]  # et ajoute une virgule au chiffre des unités
    lg = max(len(dec4), len(deca), len(decb)+1)  # nombre de colonnes dans le tableau
    exo.append('$$ %s \\times %s = \\ldots $$' % (Affichage.decimaux(nba *10 ** puisa), Affichage.decimaux(nbb * 10 ** puisb)))
    cor.append('\\begin{tabular}[t]{*{%s}{c}}' % lg)
    cor.append('%s \\\\' % ' & '.join(ligneprod([], deca,lg)))
    cor.append('%s \\\\\n\\hline' % ' & '.join(ligneprod(['$\\times$'], decb, lg)))

    if len(dec3) > 1:
        for i in range(len(dec3)):
            dec = [str(dec3[i])[j] for j in range(len(str(dec3[i])))]
            cor.append('%s \\\\' % ' & '.join(ligneprod([], dec, lg)))
        cor.append('\\hline')

    cor.append('%s \\\\' % ' & '.join(ligneprod([], dec4, lg)))
    cor.append('\\end{tabular}')

    formule = '%s\\times%s = %s' % (Affichage.decimaux(nba *10 ** puisa, 1), Affichage.decimaux(nbb * 10 **puisb, 1), Affichage.decimaux((nba * nbb) * 10 ** (puisa + puisb), 1))
    cor.append((u'\\[ \\boxed{%s} \\] ').expandtabs(2 * 3) % (formule))

#---------------methode pour le quotient--------------------------------
def valeurs_quot(nbre_min, nbre_max, nbre_decimal):
    while 1:
        nba = Arithmetique.valeur_alea(nbre_min*10**nbre_decimal, nbre_max*10**nbre_decimal)
        if nba - (nba // 10) * 10:
            break
    puisa = - nbre_decimal
    nbb = Arithmetique.valeur_alea(nbre_min, nbre_max)

    return (nba, nbb, puisa)



#--------------Construction des exercices-----------------------

def AdditionEntier(parametre):
    question = "Poser l'addition suivante :"
    exo = [ ]
    cor = [ ]
    tex_somme(exo, cor, parametre[0], parametre[1], 0, 0)
    return (exo, cor, question)
    
def AdditionDecimal(parametre):
    question = "Poser l'addition suivante :"
    exo = [ ]
    cor = [ ]
    tex_somme(exo, cor, parametre[0], parametre[1], random.randint(1,2), random.randint(1,2))
    return exo, cor, question

def SoustractionEntier(parametre):
    question = "Poser la soustraction suivante :"
    exo = [ ]
    cor = [ ]
    tex_difference(exo, cor,parametre[0], parametre[1], 0, 0)
    return exo, cor, question

def SoustractionDecimal(parametre):
    question = "Poser la soustraction suivante :"
    exo = [ ]
    cor = [ ]
    tex_difference(exo, cor, parametre[0], parametre[1], random.randint(1,2), random.randint(1,2))
    return exo, cor, question

def MultiplicationEntier(parametre):
    question = "Poser la multiplication suivante :"
    exo = [ ]
    cor = [ ]
    tex_produit(exo, cor, parametre[0], parametre[1], 0, 0)
    return exo, cor, question

def MultiplicationDecimal(parametre):
    question = "Poser la multiplication suivante :"
    exo = [ ]
    cor = [ ]
    tex_produit(exo, cor, parametre[0], parametre[1], random.randint(1,2), random.randint(1,2))
    return exo, cor, question
