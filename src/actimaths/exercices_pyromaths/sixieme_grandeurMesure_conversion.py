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
# Conversions
#===============================================================================

units = ["L", "m", "g"]
division = ["k", "h", "da", "", "d", "c", "m"]

#paramétrage des flèches : mofifie le paramétrage par défaut de PSTricks  s'il n'est pas limité par un environnement ou {groupe}
## nodesepA = -1.5mm  : décale le départ de la flèche
## linewidth = 0.6pt  : épaisseur de la flèches
## linestyle = dotted : style pointillé
## vref = -0.8mm      : décale la flèche vers le bas, sous les chiffres
PSSET_FLECHE = '\\psset{nodesepA = -1.5mm, linewidth = 0.6pt, linestyle = dotted, vref = -0.8mm}'

def valeurs_units():
    """
    renvoie les valeurs pour les conversions d'unités
    """

    a = Arithmetique.valeur_alea(101, 999)
    p = random.randrange(-2, 0)
    unit = random.randrange(3)
    if unit:
        #mètres ou grammes, on peut utiliser les k
        imax = 7
    else:
        #Litres, donc pas de kL
        imax = 6

    div0 = random.randrange(imax + p)

    while 1:
        div1 = random.randrange(imax)
        if div0 != div1:
            break

    if not unit: #Litres, donc pas de kL donc on décale d'un rang
        div0, div1 = div0 + 1, div1 + 1

    return (a, p, unit, div0, div1)
        #101< a <999 ex a = 245
        #p = {-2,-1} donne 2,45 ou 24,5
        #unit = {0, 1, 2} => {L, m, g}
        #div0 unité 0
        #div1 unité converti

def exo_conversion_longueur(parametre):
    """
    Écrit l'exercice sur les conversions d'unités et le corrigé au format
    LaTeX
    @param exo: fichier exercices
    @param cor: fichier corrige
    """
    question = ""
    exo = ['Effectuer les conversions suivantes :',
            '\\begin{multicols}{3}\\noindent', '\\begin{enumerate}']
    cor = [ #paramétrage des flèches, ce paramétrage est limité à l'exercice
            # et ne modifie pas le paramétrage PSTricks du document car sa portée est limité par le groupe ouvert par "{"
           "{",
            PSSET_FLECHE,
           'Effectuer les conversions suivantes :',
            '\\begin{multicols}{2}\\noindent', '\\begin{enumerate}']

    #Construit les 6 questions de l'exercice
    for i in range(6):
        (a, p, unit, div0, div1) = valeurs_units()
        if unit:
            u = tuple([units[unit] for i in range(7)])
        else:
            u = tuple([units[unit] for i in range(6)])
        nb0 = Affichage.decimaux(a * 10 ** p, 0)
        nb1 = Affichage.decimaux(a * 10 ** ((p + div1) - div0),
                0)
        exo.append("\\item %s~%s%s=\dotfill~%s%s" % (nb0, division[div0],
                 units[unit], division[div1], units[unit]))
        cor.append("\\item %s~%s%s=%s~%s%s\\par" % (nb0, division[div0],
                 units[unit], nb1, division[div1], units[unit]))
        nblist = [nb0[i] for i in range(len(nb0))]
        if nblist.count(','):
            chf_unite = nblist.index(',') - 1
            nblist.pop(chf_unite + 1)
        else:
            chf_unite = len(nblist) - 1

        tex_tableau(cor, div0, div1, u, nblist, chf_unite)

        cor.append("\\end{tabular}")
        cor.append("\\ncline{->}{virg0}{virg1}")

    exo.append('\\end{enumerate}')
    exo.append('\\end{multicols}')
    cor.append('\\end{enumerate}')
    cor.append('\\end{multicols}')
    #ferme le groupe limitant la portée de PSSET_FLECHE
    cor.append('}')
    return (exo, cor, question)


def tex_tableau(cor, div0, div1, u, nblist, chf_unite):
    """tableau de conversion pour les unités simples : L, g ou m"""

    #Si len(u) == 6, on a des Litres, on ne doit pas avoir la colonne kL
    if len(u) == 6:
        cor.append("\\begin{tabular}{c|c|c|c|c|c}")
        cor.append("h%s & da%s & %s & d%s & c%s & m%s \\\\ \\hline" %u )
        #décale d'une colonne pour supprimer kL
        delta = 1
        div0 = div0 - 1
        div1 = div1 - 1

    else:
        cor.append("\\begin{tabular}{c|c|c|c|c|c|c}")
        cor.append("k%s & h%s & da%s & %s & d%s & c%s & m%s \\\\ \\hline" % u)
        #ne supprime pas le kg, km
        delta = 0
    for i in range(-div0 + chf_unite):
        tmp = nblist.pop(0)
        nblist[0] = tmp + nblist[0]

    for i in range(div0 - chf_unite):
        nblist.insert(0, '0')


    for i in range(-len(u) + len(nblist)):
        tmp = nblist.pop(7)
        nblist[6] = nblist[6] + tmp

    #les zéros à droites des chiffres significatifs
    for i in range(len(u) - len(nblist)):
        nblist.append('0')

    #place les \nodes et la virgule dans le tableau
    nblist[div0] =  "%s\\Rnode{virg0}{\\ }"%(nblist[div0])
    nblist[div1] = "{%s\\Rnode{virg1}{\\textcolor{red}{ \\LARGE ,}}}"%(nblist[div1])

    #ajoute au tabular la ligne avec 6 ou 7 colonnes
    cor.append(("%s "+("& %s"*(6-delta))) % tuple(nblist))



def exo_conversion_surface(parametre):
    """construit l'exercice de conversion d'unité d'aire ou de volume
    exposant 2 pour m²"""
    question = ""
    exo = ['Effectuer les conversions suivantes :',
            '\\begin{multicols}{3}\\noindent', '\\begin{enumerate}']
    cor = [#la portée de \psset est par le group ouvert par "{"
            "{",
            PSSET_FLECHE,
            '\\def\\virgule{\\textcolor{red}{ \\LARGE ,}}',
            'Effectuer les conversions suivantes :',
            '\\begin{multicols}{2}\\noindent', '\\begin{enumerate}']

    #ajoute le ² ou ³ si nécessaire
    exposant = 2
    str_exposant=(u"^%s"%(exposant))*(exposant > 1)

    u = tuple([division[i]+"m%s"%str_exposant for i in range(7)])
    entete_tableau = ((" \\multicolumn{%s}{c|}"%exposant +"{$\\rm %s$} &")*6 +"\\multicolumn{%s}{c}"%exposant+"{$\\rm %s$}" )%u
    ligne_tab = []

    for i in range(6):
        #imprime la correction et sauvegarde la ligne et la flèche pour le tableau imprimé ensuite
        ligne_tab += tex_conversion(exo, cor,exposant, u) + ["\\ncline{->}{virg0}{virg1} \\\\"]

    #ferme la correction et l'énoncé
    cor.append('\\end{enumerate}')
    cor.append('\\end{multicols}')
    exo.append('\\end{enumerate}')
    exo.append('\\end{multicols}')

    #impression du tableau et des lignes sauvegardées précédemment
    cor.append("\\begin{tabular}{*{%s}{p{3.5mm}|}p{3.5mm}}"%(exposant*7-1))
    cor.append(entete_tableau + "\\\\ \\hline")
    #ajoute les lignes affichant les conversions
    cor += ligne_tab
    cor.append("\\end{tabular}")
    #ferme le groupe dans lequel PSSET_FLECHE portait
    cor.append("}")
    #C'est fini
    return (exo, cor, question)

def exo_conversion_volume(parametre):
    """construit l'exercice de conversion d'unité d'aire ou de volume
    exposant 3 pour m³"""
    question = ""
    exo = ['Effectuer les conversions suivantes :',
            '\\begin{multicols}{3}\\noindent', '\\begin{enumerate}']
    cor = [#la portée de \psset est par le group ouvert par "{"
            "{",
            PSSET_FLECHE,
            '\\def\\virgule{\\textcolor{red}{ \\LARGE ,}}',
            'Effectuer les conversions suivantes :',
            '\\begin{multicols}{2}\\noindent', '\\begin{enumerate}']

    #ajoute le ² ou ³ si nécessaire
    exposant = 3
    str_exposant=(u"^%s"%(exposant))*(exposant > 1)

    u = tuple([division[i]+"m%s"%str_exposant for i in range(7)])
    entete_tableau = ((" \\multicolumn{%s}{c|}"%exposant +"{$\\rm %s$} &")*6 +"\\multicolumn{%s}{c}"%exposant+"{$\\rm %s$}" )%u
    ligne_tab = []

    for i in range(6):
        #imprime la correction et sauvegarde la ligne et la flèche pour le tableau imprimé ensuite
        ligne_tab += tex_conversion(exo, cor,exposant, u) + ["\\ncline{->}{virg0}{virg1} \\\\"]

    #ferme la correction et l'énoncé
    cor.append('\\end{enumerate}')
    cor.append('\\end{multicols}')
    exo.append('\\end{enumerate}')
    exo.append('\\end{multicols}')

    #impression du tableau et des lignes sauvegardées précédemment
    cor.append("\\begin{tabular}{*{%s}{p{3.5mm}|}p{3.5mm}}"%(exposant*7-1))
    cor.append(entete_tableau + "\\\\ \\hline")
    #ajoute les lignes affichant les conversions
    cor += ligne_tab
    cor.append("\\end{tabular}")
    #ferme le groupe dans lequel PSSET_FLECHE portait
    cor.append("}")
    #C'est fini
    return (exo, cor, question)

def tex_conversion(exo, cor, exposant, u):
    """Écrit une question sur les conversions d'unités d'aires ou de volume
    et le corrigé au format LaTeX
    @param exo: fichier exercices
    @param cor: fichier corrige
    exposant = 2 ou 3 pour les aires ou les volumes
    """

    a = random.randint(101,999)
    p = random.randint(-2,-1)
    while True:
        (div0,div1)=(random.randrange(6),random.randrange(7),)
        #Pas de mm³ par ce que ça sort du tableau
        if (div0-div1) in [-2,-1,1,2]:
            #pas trop loin car ça fait de très longs nombres
            break
    nb0 = a * 10 ** p
    nb1 = nb0 * 10 ** ( exposant * ( div1- div0))

    exo.append("\\item $\\unit[%s]{%s}=\\unit[\\dotfill]{%s}$"%
            (Affichage.decimaux(nb0), u[div0], u[div1]))
    cor.append("\\item $\\unit[%s]{%s}=\\unit[%s]{%s}$\\vspace{1ex}\\par" %
            (Affichage.decimaux(nb0), u[div0],
                Affichage.decimaux(nb1), u[div1]))

    return tex_tableau_conversion(div0, div1, nb0, u, exposant)


def tex_tableau_conversion(div0, div1, nb0, u, exposant):
    nb_dict = nbre_to_dict(nb0,div0,div1,exposant)
    nblist = [str(nb_dict.get(i,"")) for i in range(7*exposant)]
    nblist[exposant*(div0 + 1)-1] =  "%s\\Rnode{virg0}{\\ }"% nb_dict.get(exposant*(div0+1)-1,"0")
    nblist[exposant*(div1 + 1)-1] = "{%s\\Rnode{virg1}{\\virgule}}"% nb_dict.get(exposant*(div1+1)-1,"0")
    return [("%s " + "& %s"*(7*exposant-1)) % tuple(nblist)]


def nbre_to_dict(nbre ,div0,div1,exposant):
    #exposant peut être 2 ou 3 pour les m² ou les m³
    nbre = int(round(nbre*100))
    nb_dict = {}
    for i in range(min(exposant*(div0+1),exposant*(div1+1))-1,max(exposant*(div0+1),exposant*(div1+1))):
            nb_dict[i] = "\\textcolor{red}{0}"
    curseur = 1+exposant*(div0+1)
    while nbre % 10 == 0:
        nbre = nbre / 10
        curseur -= 1
    while nbre > 0:
        chiffre = nbre % 10
        nbre = (nbre-chiffre)/10
        nb_dict[curseur] = "\\textcolor{blue}{%s}"%chiffre
        curseur -= 1
    return nb_dict
