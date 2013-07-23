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

division = ["k", "h", "da", "", "d", "c", "m"]

#paramétrage des flèches : mofifie le paramétrage par défaut de PSTricks  s'il n'est pas limité par un environnement ou {groupe}
## nodesepA = -1.5mm  : décale le départ de la flèche
## linewidth = 0.6pt  : épaisseur de la flèches
## linestyle = dotted : style pointillé
## vref = -0.8mm      : décale la flèche vers le bas, sous les chiffres
PSSET_FLECHE = '\\psset{nodesepA = -1.5mm, linewidth = 0.6pt, linestyle = dotted, vref = -0.8mm}'

def nbre_to_dict(nbre ,div0,div1,exposant):
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

def tex_ligne_corrige(div0, div1, nb0, exposant):
    nb_dict = nbre_to_dict(nb0,div0,div1,exposant)
    nblist = [str(nb_dict.get(i,"")) for i in range(7*exposant)]
    nblist[exposant*(div0 + 1)-1] =  "%s\\Rnode{virg0}{}"% nb_dict.get(exposant*(div0+1)-1,"0")
    nblist[exposant*(div1 + 1)-1] = "%s\\Rnode{virg1}{,}"% nb_dict.get(exposant*(div1+1)-1,"0")
    return [("%s " + "& %s"*(7*exposant-1)) % tuple(nblist)]

def tex_tableau_conversion(tex, ligne_tab, exposant, unite):
    #ouverture du groupe dans lequel PSSET_FLECHE portait
    tex.append("{")
    tex.append(PSSET_FLECHE)
    # entete du tableau
    tex.append("\\begin{tiny}")
    tex.append("\\tabcolsep=3pt")
    tex.append("\\begin{tabular}{*{%s}{p{%smm}|}p{%smm}}" % (exposant*7-1, 5.0/(exposant*exposant), 5.0/(exposant*exposant)))
    tex.append(((" \\multicolumn{%s}{c|}"%exposant +"{$\\rm %s$} &")*6 +"\\multicolumn{%s}{c}"%exposant+"{$\\rm %s$}" )%unite)
    tex.append("\\\\")
    tex.append("\\hline")
    #ajoute les lignes affichant les conversions
    tex += ligne_tab
    tex.append("\\end{tabular}")
    tex.append("\\end{tiny}")
    #fermeture du groupe dans lequel PSSET_FLECHE portait
    tex.append("}")

##############################Construction###################################
def tex_exercice(exo,cor,exposant):
    # variable
    a = random.randint(101,999)
    p = random.randint(-2,-1)
    while True:
        (div0,div1)=(random.randrange(6),random.randrange(7))
        #Pas de mm³ par ce que ça sort du tableau
        if (div0-div1) in [-2,-1,1,2]:
            #pas trop loin car ça fait de très longs nombres
            break
    nb0 = a * 10 ** p
    nb1 = nb0 * 10 ** ( exposant * ( div1- div0))
    # unité
    str_exposant=(u"^%s"%(exposant))*(exposant > 1) #ajoute le ² ou ³ si nécessaire
    unite = tuple([division[i]+"m%s"%str_exposant for i in range(7)])
    ligne_enonce = [("" + "& "*(7*exposant-1))]
    ligne_corrige = tex_ligne_corrige(div0, div1, nb0, exposant) + ["\\ncline{->}{virg0}{virg1} \\\\"]
    #construction
    exo.append("$$\\unit[%s]{%s}=\\unit[\\ldots]{%s}$$"%(Affichage.decimaux(nb0), unite[div0], unite[div1]))
    cor.append("$$\\unit[%s]{%s}=\\unit[%s]{%s}$$" % (Affichage.decimaux(nb0), unite[div0], Affichage.decimaux(nb1), unite[div1]))
    tex_tableau_conversion(exo, ligne_enonce, exposant, unite)
    tex_tableau_conversion(cor, ligne_corrige, exposant, unite)

def Conversion(parametre):
    question = "Effectuer la conversion :"
    exo = []
    cor = []
    tex_exercice(exo,cor,1)
    return exo, cor, question

def ConversionAire(parametre):
    question = "Effectuer la conversion :"
    exo = []
    cor = []
    tex_exercice(exo,cor,2)
    return exo, cor, question

def ConversionVolume(parametre):
    question = "Effectuer la conversion :"
    exo = []
    cor = []
    tex_exercice(exo,cor,3)
    return exo, cor, question
