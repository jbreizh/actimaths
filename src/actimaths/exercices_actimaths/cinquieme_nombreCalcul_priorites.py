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
import string

################## Renvoie les 2 listes contenant les opérateurs et les opérandes.
def valeurs(nombre_min, nombre_max, nb, entier, parenthese):  # renvoie les 2 listes contenant les opérateurs et les opérandes.
    ## Initialisation
    operateurs = ['+', '-', '*', '/']
    liste_operateurs = []
    liste_operandes = []
    operateur_cree = 0
    parenthese_ouverte = 0
    position_parenthese = random.randrange(1,nb - 1)
    if parenthese:
        nombre_multiplication_division = 1
    else:
        nombre_multiplication_division = 0
    ## Création des opérateurs
    while operateur_cree < nb - 1:
        # Creation de l'opérateur
        if parenthese_ouverte:
            # + ou - dans la parenthese
            if liste_operateurs[-1] == '(':
                operateur = operateurs[random.randrange(2)]
                operateur_cree += 1
            # on ferme la parenthèse
            else:
                operateur = ')'
                parenthese_ouverte -= 1
        else:
            # à position_parenthese-1, * ou /
            if parenthese and operateur_cree==position_parenthese-1:
                operateur = operateurs[random.randrange(2,4)]
                operateur_cree += 1
            # à position_parenthese, on ouvre la parenthèse
            elif parenthese and operateur_cree==position_parenthese:
                operateur = '('
                parenthese_ouverte += 1
            # sinon on choisit un opérateur
            else:
                # nombre_multiplication_division plus petit que 2, +,-,*,/
                if nombre_multiplication_division < 2:
                    operateur = operateurs[random.randrange(4)]
                    # si c'est un * ou / on incremente nombre_multiplication_division
                    if ('*/').find(operateur) >= 0:
                        nombre_multiplication_division += 1
                # sinon + ou -
                else:
                    operateur = operateurs[random.randrange(2)]
                operateur_cree += 1
        # Ajout de l'opérateur
        liste_operateurs.append(operateur)
    ## On ferme les parentheses qui restent ouverte
    while parenthese_ouverte > 0:
        liste_operateurs.append(')')
        parenthese_ouverte -= 1
    ## Création des opérandes
    if entier:
        liste_operandes = random.sample(xrange(nombre_min, nombre_max),nb)
    else:
        liste_operandes = random.sample([x / 10.0 for x in range(nombre_min * 10, nombre_max * 10)],nb)
    return (liste_operateurs, liste_operandes)

##################
def affichage(loperateurs, loperandes):
    j = 0  #compteur des operateurs
    calcul = '%s' % nb_decimal((loperandes[0], ))
    for i in range(len(loperandes) - 1):
        if loperateurs[j] == ')':  #Il reste une opération mais je ferme d'abord une ou plusieurs parenthèses
            cpt = 1
            while loperateurs[j + cpt] == ')':
                cpt = cpt + 1  #j+cpt est la position de l'opération qui suit
        else:
            cpt = 0
        if j + cpt < len(loperateurs) - 1:  #Il reste au moins une opération, donc peut-etre une parenthèse ouvrante
            while loperateurs[j + cpt + 1] == '(':  #j+cpt est la position de la dernière parenthèse (
                cpt = cpt + 1
        for k in range(cpt + 1):
            calcul = calcul + '%s' % loperateurs[j + k]
        calcul = calcul + '%s' % nb_decimal((loperandes[i + 1], ))
        j = j + cpt + 1
    while j < len(loperateurs):
        calcul = calcul + '%s' % loperateurs[j]
        j = j + 1
    calcul = ('\\times ').join(calcul.split('*', 2))
    calcul = ('\\div ').join(calcul.split('/', 2))
    return calcul

################## Verifie si des nombres décimaux dans le tuple a sont en fait des nombres entiers et change leur type
def nb_decimal(a):
    liste = []
    for i in range(len(a)):
        if str(a[i]).endswith('.0'):
            liste.append(int(a[i] + .1))
        else:
            liste.append(('{,}').join(str(a[i]).split('.', 2)))
    return tuple(liste)

################## Vérifie que l'opération proposée est réalisable sans division décimale ni nombre négatif
def verifie_calcul(listoperateurs, listoperandes, entier=1):
    p = 0
    loperateurs = listoperateurs[-1]
    loperandes = listoperandes[-1]
    if len(loperandes) == 1:
        return (listoperateurs, listoperandes)
    else:
        nbpar = loperateurs.count('(')
        nbmul = loperateurs.count('*')
        nbdiv = loperateurs.count('/')
        if nbpar:
            index = -1
            while p < nbpar:
                index = loperateurs[index + 1:].index('(') + index + 1
                p = p + 1
                if p < nbpar and loperateurs[index + 1:].index('(') > \
                    loperateurs[index + 1:].index(')'):
                    nbpar = p
            if loperateurs[index + 2] == ')':
                a = calcul(loperandes[(index + 1) - nbpar], loperateurs[index +
                           1], loperandes[(index + 2) - nbpar], entier)
                if a != 'hp':
                    al = loperateurs[:index]
                    al.extend(loperateurs[index + 3:])
                    loperateurs = al
                    al = loperandes[:(index + 1) - nbpar]
                    al.append(a)
                    al.extend(loperandes[index - nbpar + 3:])
                    loperandes = al
                    listoperateurs.append(loperateurs)
                    listoperandes.append(loperandes)
                    return verifie_calcul(listoperateurs, listoperandes)
        elif nbmul or nbdiv:
            (indexm, indexd) = (100, 100)
            if nbmul:
                indexm = loperateurs.index('*')
            if nbdiv:
                indexd = loperateurs.index('/')
            index = min(indexm, indexd)
            a = calcul(loperandes[index], loperateurs[index], loperandes[index +
                       1], entier)
            if a != 'hp':
                al = loperateurs[:index]
                al.extend(loperateurs[index + 1:])
                loperateurs = al
                al = loperandes[:index]
                al.append(a)
                al.extend(loperandes[index + 2:])
                loperandes = al
                listoperateurs.append(loperateurs)
                listoperandes.append(loperandes)
                return verifie_calcul(listoperateurs, listoperandes)
        else:
            a = calcul(loperandes[0], loperateurs[0], loperandes[1],
                       entier)
            if a != 'hp':
                loperateurs = loperateurs[1:]
                al = [a]
                al.extend(loperandes[2:])
                loperandes = al
                listoperateurs.append(loperateurs)
                listoperandes.append(loperandes)
                return verifie_calcul(listoperateurs, listoperandes)

################## Retourne 'hp' (hors programme) ou le résultat de l'opération
def calcul(a, op, b, entier):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '-':
        if a > b:
            return a - b
        else:
            return 'hp'
    else:
        if (a * 100) % (b * 100) and entier:
            return 'hp'
        elif not entier and (a * 1000) % (b * 100):
            return 'hp'
        else:
            return a / b

################## Construit l'exercice
def construction(nombre_min, nombre_max, nbre_operande, entier, parenthese):
    question = "Calculer :"
    exo = []
    cor = []
    i = True
    while i:
        (loperateurs, loperandes) = valeurs(nombre_min, nombre_max, nbre_operande, entier, parenthese)
        liste = verifie_calcul([loperateurs], [loperandes], entier)
        if liste:
            i = False
            cor.append("\\begin{center}")
            cor.append("$\\begin{aligned}")
            for j in range(len(liste[0])):
                if j == 0:
                    exo.append("$$A = %s$$" % affichage(liste[0][j], liste[1][j]))
                if j == len(liste[0]) - 1:
                    cor.append("A & = \\boxed{%s} \\\\" % affichage(liste[0][j], liste[1][j]))
                else:
                    cor.append("A & = %s \\\\" % affichage(liste[0][j], liste[1][j]))
            cor.append("\\end{aligned}$")
            cor.append("\\end{center}")
    return (exo, cor, question)

def Operande3Entiere(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 3, 1, 0)
    return (exo, cor, question)

def Operande3EntiereParenthese(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 3, 1, 1)
    return (exo, cor, question)

def Operande3Decimale(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 3, 0, 0)
    return (exo, cor, question)

def Operande3DecimaleParenthese(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 3, 0, 1)
    return (exo, cor, question)

def Operande4Entiere(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 4, 1, 0)
    return (exo, cor, question)

def Operande4EntiereParenthese(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 4, 1, 1)
    return (exo, cor, question)

def Operande4Decimale(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 4, 0, 0)
    return (exo, cor, question)

def Operande4DecimaleParenthese(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 4, 0, 1)
    return (exo, cor, question)

def Operande5Entiere(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 5, 1, 0)
    return (exo, cor, question)

def Operande5EntiereParenthese(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 5, 1, 1)
    return (exo, cor, question)

def Operande5Decimale(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 5, 0, 0)
    return (exo, cor, question)

def Operande5DecimaleParenthese(parametre):
    (exo, cor, question) = construction(parametre[0], parametre[1], 5, 0, 1)
    return (exo, cor, question)
