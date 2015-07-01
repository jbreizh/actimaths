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
import copy

#---------------methode--------------------------------
def creation_tableau(parametre,structure):
    ## ---Calcul des paramètres---
    nombreColonne = random.randrange(3,5)
    #caractere
    caractere = [u"Caractère"]
    caractereTemp = random.sample(range(parametre[0],parametre[1]), nombreColonne)
    caractereTemp.sort()
    caractere.extend(caractereTemp)
    caractere.append("Total")
    #effectif
    effectif = ["Effectif"]
    effectifTemp = random.sample(range(parametre[0],parametre[1]), nombreColonne)
    effectifTotal = 0
    for i in range(len(effectifTemp)):
        effectifTotal += effectifTemp[i]
    effectif.extend(effectifTemp)
    effectif.append(effectifTotal)
    #frequence
    frequence = [u"Fréquence"]
    frequenceTemp = [round(float(i)/effectifTotal,2) for i in effectifTemp]
    frequence.extend(frequenceTemp)
    frequence.append(1)
    #angle
    angle = ["Angle"]
    angleTemp = [round(float(i)/effectifTotal*360,1) for i in effectifTemp]
    angle.extend(angleTemp)
    angle.append(360)
    ## ---remplissage du tableau---
    tableau = []
    for i in range(len(caractere)):
        ligne = []
        if structure[0]:
            ligne.append(caractere[i])
        if structure[1]:
            ligne.append(effectif[i])
        if structure[2]:
            ligne.append(frequence[i])
        if structure[3]:
            ligne.append(angle[i])
        tableau.append(ligne)
    return tableau

def tex_tableau(tex, contenu):
    nombreColonne = len(contenu)
    if nombreColonne != 0:
        nombreLigne = len(contenu[0])
        # entete du tableau
        tex.append("\\begin{tiny}")
        tex.append("\\begin{center}")
        ligne = "\\begin{tabular}{|"
        for i in range(len(contenu)):
            ligne += "c|"
        ligne += "}"
        tex.append(ligne)
        # corps du tableau
        for i in range(nombreLigne):
            tex.append("\\hline")
            ligne = ""
            for j in range(nombreColonne):
                ligne += "%s" % contenu[j][i]
                if j != nombreColonne - 1:
                   ligne += "&"
            ligne += "\\\\"
            tex.append(ligne)
        tex.append("\\hline")
        # fin du tableau
        tex.append("\\end{tabular}")
        tex.append("\\end{center}")
        tex.append("\\end{tiny}")

#---------------Construction--------------------------------
def CalculEffectifSerie(parametre):
    ## ---Initialisation---
    question = u"Compléter le tableau :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    tableau = creation_tableau(parametre,[True,True,False,False])
    manquant = random.randrange(1,len(tableau)-1)
    ## ---serie brute---
    serie = []
    for i in range(1,len(tableau) - 1):
        for j in range(tableau[i][1]):
            serie.append(tableau[i][0])
    ## ---serie pour le sujet---
    serieSujet = copy.deepcopy(serie)
    random.shuffle(serieSujet)
    #tableau pour le sujet
    tableauSujet = copy.deepcopy(tableau)
    tableauSujet[manquant][1] = "$\\ldots$"
    ## ---Redaction---
    exo.append(u"Série statistique :")
    cor.append(u"Série statistique :")
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    ligne = ""
    for i in range(len(serieSujet)):
        ligne += "%s" %serieSujet[i]
        if i != len(serieSujet) - 1:
            ligne += " ; "
    exo.append(ligne)
    cor.append(ligne)
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    exo.append(u"Tableau caractère - effectif :")
    cor.append(u"Tableau caractère - effectif :")
    tex_tableau(exo, tableauSujet)
    tex_tableau(cor, tableauSujet)
    cor.append(u"On compte un effectif de \\fbox{%s} pour le caractère %s dans la série." %(tableau[manquant][1],tableau[manquant][0]))
    return (exo, cor, question)

def CalculEffectifTableau(parametre):
    ## ---Initialisation---
    question = u"Calculer l'effectif manquant :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    tableau = creation_tableau(parametre, [True,True,False,False])
    effectifTotal = tableau[len(tableau)-1][1]
    manquant = random.randrange(1,len(tableau)-1)
    #tableau pour le sujet
    tableauSujet = copy.deepcopy(tableau)
    tableauSujet[manquant][1] = "$\\ldots$"
    # somme des effectifs
    somme = 0
    for i in range(1, len(tableau)-1):
        if i != manquant:
            somme += tableau[i][1]
    ## ---Redaction---
    tex_tableau(exo, tableauSujet)
    tex_tableau(cor, tableauSujet)
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    ligne1 = ""
    for i in range(1, len(tableau)-1):
        if i == manquant:
            ligne1 += "\\ldots"
        else:
            ligne1 += "%s" % tableau[i][1]
        if i != len(tableau)-2:
            ligne1 += "+"
    ligne1 += "& = %s \\\\" % effectifTotal
    cor.append(ligne1)
    cor.append("\\ldots + %s & = %s \\\\" %(somme, effectifTotal))
    cor.append("\\ldots & = %s - %s \\\\" %(effectifTotal, somme))
    cor.append("\\ldots & = \\boxed{%s} \\\\" %(effectifTotal- somme))
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def CalculEffectifTotal(parametre):
     ## ---Initialisation---
    question = u"Calculer l'effectif total :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    tableau = creation_tableau(parametre,[True,True,False,False])
    #tableau pour le sujet
    tableauSujet = copy.deepcopy(tableau)
    tableauSujet[len(tableau)-1][1] = "$\\ldots$"
    ## ---Redaction---
    tex_tableau(exo, tableauSujet)
    tex_tableau(cor, tableauSujet)
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    ligne1 = "\\ldots & = "
    for i in range(1, len(tableau)-1):
        ligne1 += "%s" % tableau[i][1]
        if i != len(tableau)-2:
            ligne1 += "+"
        else:
            ligne1 += "\\\\"
    cor.append(ligne1)
    cor.append("\\ldots & = \\boxed{%s} \\\\" %tableau[len(tableau)-1][1])
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def CalculFrequence(parametre):
     ## ---Initialisation---
    question = u"Calculer la frequence manquante :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    tableau = creation_tableau(parametre,[True,True,True,False])
    manquant = random.randrange(1,len(tableau)-1)
    #tableau pour le sujet
    tableauSujet = copy.deepcopy(tableau)
    tableauSujet[manquant][2] = "$\\ldots$"
    ## ---Redaction---
    tex_tableau(exo, tableauSujet)
    tex_tableau(cor, tableauSujet)
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("\\ldots & = %s \\div %s \\\\" %(tableau[manquant][1],tableau[len(tableau)-1][1]))
    cor.append("\\ldots & \\approx \\boxed{%s} \\\\" %tableau[manquant][2])
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def CalculAngleDiagramme(parametre):
     ## ---Initialisation---
    question = u"Calculer l'angle manquant :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    tableau = creation_tableau(parametre,[True,True,False,True])
    manquant = random.randrange(1,len(tableau)-1)
    #tableau pour le sujet
    tableauSujet = copy.deepcopy(tableau)
    tableauSujet[manquant][2] = "$\\ldots$"
    ## ---Redaction---
    tex_tableau(exo, tableauSujet)
    tex_tableau(cor, tableauSujet)
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("\\ldots & = %s \\div %s \\times 360 \\\\" %(tableau[manquant][1],tableau[len(tableau)-1][1]))
    cor.append("\\ldots & \\approx \\boxed{%s} \\\\" %tableau[manquant][2])
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)
