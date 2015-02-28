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
import math
from outils.Geometrie import choix_points
from outils.Arithmetique import liste_combinaison

#------------------methode---------------------------------------------
def coordonnees_points():
    coordonnee_point = []
    coordonnee_point.append([random.uniform(-4,-1),random.uniform(1,4)])
    coordonnee_point.append([random.uniform(1,4),random.uniform(1,4)])
    coordonnee_point.append([random.uniform(1,4),random.uniform(-4,-1)])
    coordonnee_point.append([random.uniform(-4,-1),random.uniform(-4,-1)])
    return coordonnee_point

def carateristique_duo_point(nom_point):
    #liste des combinaisons de 2 points
    duo_point = liste_combinaison(nom_point,2)
    #nature et noms des combinaisons de 2 points
    nom_duo_point = []
    nature_duo_point = []
    for i in range(len(duo_point)):
        temp = random.randrange(3)
        if temp == 0:
            nom_duo_point.append("(%s%s)" %(duo_point[i][0],duo_point[i][1]))
            nature_duo_point.append("une droite")
        elif temp == 1:
            nom_duo_point.append("[%s%s)" %(duo_point[i][0],duo_point[i][1]))
            nature_duo_point.append("une demi-droite")
        else:
            nom_duo_point.append("[%s%s]" %(duo_point[i][0],duo_point[i][1]))
            nature_duo_point.append("un segment")
    return (duo_point,nom_duo_point,nature_duo_point)

def tex_figure(enonce,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append('\\begin{pspicture*}(-5,-5)(5,5)')
    for i in range(len(nom_point)-1):
        enonce.append("\\pstGeonode(%s,%s){%s}" %(coordonnee_point[i][0],coordonnee_point[i][1],nom_point[i]))
    for i in range(len(duo_point)):
        ligne = "\\pstLineAB["
        if nature_duo_point[i] == "une droite":
            ligne += "nodesepA=-3, nodesepB=-3"
        elif nature_duo_point[i] == "une demi-droite":
                ligne += "nodesepB=-3"
        if i == choix_duo_point:
                ligne += ",linecolor=red]"
        else:
                ligne += "]"
        ligne +="{%s}{%s}" %(duo_point[i][0],duo_point[i][1])
        enonce.append(ligne)
    enonce.append("\\pstInterLL{%s}{%s}{%s}{%s}{%s}" %(nom_point[0],nom_point[2],nom_point[1],nom_point[3],nom_point[4]))
    enonce.append('\\end{pspicture*}')
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def Nature(parametre):
    ## ---Initialisation---
    question = u"Donner la nature de l'objet rouge :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    nom_point = choix_points(5)
    coordonnee_point = coordonnees_points()
    (duo_point,nom_duo_point,nature_duo_point) = carateristique_duo_point(nom_point[0:4])
    choix_duo_point = random.randrange(len(duo_point))
    ## ---Redaction---
    tex_figure(exo,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point)
    tex_figure(cor,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point)
    cor.append("\\begin{center}")
    cor.append(u"L'objet rouge est \\fbox{%s}" % nature_duo_point[choix_duo_point])
    cor.append("\\end{center}")
    return (exo, cor, question)

def Nommer(parametre):
    ## ---Initialisation---
    question = u"Donner l'écriture de l'objet rouge :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    nom_point = choix_points(5)
    coordonnee_point = coordonnees_points()
    (duo_point,nom_duo_point,nature_duo_point) = carateristique_duo_point(nom_point[0:4])
    choix_duo_point = random.randrange(len(duo_point))
    ## ---Redaction---
    tex_figure(exo,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point)
    tex_figure(cor,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point)
    cor.append("\\begin{center}")
    cor.append(u"L'objet rouge s'écrit \\fbox{%s}" % nom_duo_point[choix_duo_point])
    cor.append("\\end{center}")
    return (exo, cor, question)

def Appartient(parametre):
    ## ---Initialisation---
    question = u"Compléter en utilisant $\\in$ ou $\\notin$ :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    nom_point = choix_points(5)
    coordonnee_point = coordonnees_points()
    #liste des combinaisons de 2 points
    duo_point = liste_combinaison(nom_point[0:4],2)
    #nature et noms des combinaisons de 2 points
    nom_duo_point = []
    nature_duo_point = []
    for i in range(len(duo_point)):
        nom_duo_point.append("(%s%s)" %(duo_point[i][0],duo_point[i][1]))
        nature_duo_point.append("une droite")
    choix_duo_point = len(duo_point)+1
    #
    diagonale = [[nom_point[0],nom_point[2]],[nom_point[1],nom_point[3]]]
    choix_diagonale = random.randrange(2)
    choix_type = random.randrange(5)
    ## ---Redaction---
    tex_figure(exo,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point)
    tex_figure(cor,nom_point,coordonnee_point,duo_point,nature_duo_point,choix_duo_point)
    if choix_type== 0:
         exo.append("$$ %s \\ldots (%s%s) $$" %(diagonale[choix_diagonale][0],nom_point[4],diagonale[choix_diagonale][1]))
         cor.append("$$ %s \\boxed{\\in} (%s%s) $$" %(diagonale[choix_diagonale][0],nom_point[4],diagonale[choix_diagonale][1]))
    elif choix_type == 1:
         exo.append("$$ %s \\ldots [%s%s) $$" %(diagonale[choix_diagonale][0],nom_point[4],diagonale[choix_diagonale][1]))
         cor.append("$$ %s \\boxed{\\notin} [%s%s) $$" %(diagonale[choix_diagonale][0],nom_point[4],diagonale[choix_diagonale][1]))
    elif choix_type == 2:
         exo.append("$$ %s \\ldots [%s%s) $$" %(diagonale[choix_diagonale][0],diagonale[choix_diagonale][1],nom_point[4]))
         cor.append("$$ %s \\boxed{\\in} [%s%s) $$" %(diagonale[choix_diagonale][0],diagonale[choix_diagonale][1],nom_point[4]))
    elif choix_type == 3:
         exo.append("$$ %s \\ldots [%s%s] $$" %(diagonale[choix_diagonale][0],nom_point[4],diagonale[choix_diagonale][1]))
         cor.append("$$ %s \\boxed{\\notin} [%s%s] $$" %(diagonale[choix_diagonale][0],nom_point[4],diagonale[choix_diagonale][1]))
    else:
         exo.append("$$ %s \\ldots [%s%s] $$" %(nom_point[4],diagonale[choix_diagonale][0],diagonale[choix_diagonale][1]))
         cor.append("$$ %s \\boxed{\\in} [%s%s] $$" %(nom_point[4],diagonale[choix_diagonale][0],diagonale[choix_diagonale][1]))
    return (exo, cor, question)
