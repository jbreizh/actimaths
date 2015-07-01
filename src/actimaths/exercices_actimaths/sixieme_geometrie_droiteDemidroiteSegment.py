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
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
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
    enonce.append("\\end{pspicture*}")
    enonce.append("\\end{center}")

def tex_perpendiculaire(enonce,angle,corrige):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
    # point statique
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,0){A}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,1){B}")
    # droite de depart
    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{A}{B}[C]" %angle[0])
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{A}{C}")
    # droite "perpendiculaire"
    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{A}{C}[D]" %angle[1])
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{A}{D}")
    # Affichage du corrige
    if corrige:
        enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{A}{C}[E]")
        enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6,linecolor=red]{A}{E}")
        enonce.append("\\pstRightAngle[linecolor=red]{C}{A}{E}")

    enonce.append("\\end{pspicture*}")
    enonce.append("\\end{center}")

def tex_parallele(enonce,angle,corrige):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
    # point statique
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,0){O}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,-1){A}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,1){B}")

    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{O}{A}[C]" %angle[0])
    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{O}{B}[D]" %angle[0])

    enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{C}{D}[E]")
    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{D}{C}[F]" %angle[1])
    #tracer des droites
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{C}{E}")
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{D}{F}")
    # Affichage du corrige
    if corrige:
        enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{D}{C}[G]")
        enonce.append("\\pstLineAB[nodesepA=-6, nodesepB=-6,linecolor=red]{D}{G}")
    enonce.append("\\end{pspicture*}")
    enonce.append("\\end{center}")

def tex_parallele_propriete(enonce,angle,angle_droit):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
    # point statique
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,0){O}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,-1){A}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,1){B}")

    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{O}{A}[C]" %angle)
    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{O}{B}[D]" %angle)

    enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{C}{D}[E]")
    enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{D}{C}[F]")
    #tracer des droites
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{C}{D}")
    enonce.append(" \\naput[npos=0.8]{$(d_3)$}")
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{C}{E}")
    enonce.append(" \\nbput[npos=0.75]{$(d_1)$}")
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{D}{F}")
    enonce.append(" \\nbput[npos=0.75]{$(d_2)$}")
    #tracer des codes d'angles droits
    if angle_droit[0]:
        enonce.append("\\pstRightAngle{D}{C}{E}")
    if angle_droit[1]:
        enonce.append("\\pstRightAngle{C}{D}{F}")
    enonce.append("\\end{pspicture*}")
    enonce.append("\\end{center}")

def tex_perpendiculaire_propriete(enonce,angle,angle_droit):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-5)(5,5)")
    # point statique
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,0){O}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,-1){A}")
    enonce.append("\\pstGeonode[PointSymbol=none,PointName=none](0,1){B}")

    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{O}{A}[C]" %angle)
    enonce.append("\\pstRotation[RotAngle=%s,PointSymbol=none,PointName=none]{O}{B}[D]" %angle)

    enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{C}{D}[E]")
    enonce.append("\\pstRotation[RotAngle=90,PointSymbol=none,PointName=none]{D}{C}[F]")
    #tracer des droites
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{C}{D}")
    enonce.append(" \\naput[npos=0.8]{$(d_3)$}")
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{C}{E}")
    enonce.append(" \\nbput[npos=0.75]{$(d_1)$}")
    enonce.append("\\pstLineAB[nodesepA=-6,nodesepB=-6]{D}{F}")
    enonce.append(" \\nbput[npos=0.75]{$(d_2)$}")
    #tracer des codes d'angles droits
    if angle_droit[0]:
        enonce.append("\\rput*(-3,4){\\psframebox[linewidth=0.04,fillstyle=solid]{$(d_1)//(d_2)$}}")
    if angle_droit[1]:
        enonce.append("\\pstRightAngle{C}{D}{F}")
    enonce.append("\\end{pspicture*}")
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

def Perpendiculaire(parametre):
    ## ---Initialisation---
    question = u"Les droites sont elles perpendiculaires :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    perpendiculaire = random.randrange(2)
    angle=[]
    angle.append(random.randrange(90))
    if perpendiculaire:
        angle.append(90)
        reponse = "Les droites sont perpendiculaires"
    else:
        angle.append(80)
        reponse = "Les droites ne sont pas perpendiculaires"
    ## ---Redaction---
    tex_perpendiculaire(exo, angle, False)
    tex_perpendiculaire(cor, angle, True)
    cor.append("\\begin{center}")
    cor.append("\\fbox{%s}" %reponse)
    cor.append("\\end{center}")
    return (exo, cor, question)

def Parallele(parametre):
    ## ---Initialisation---
    question = u"Les droites sont elles parallèles :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    parallele = random.randrange(2)
    angle=[]
    angle.append(random.randrange(90))
    if parallele:
        angle.append(90)
        reponse = u"Les droites sont parallèles"
    else:
        angle.append(85)
        reponse = u"Les droites ne sont pas parallèles"
    ## ---Redaction---
    tex_parallele(exo, angle, False)
    tex_parallele(cor, angle, True)
    cor.append("\\begin{center}")
    cor.append("\\fbox{%s}" %reponse)
    cor.append("\\end{center}")
    return (exo, cor, question)

def ParallelePropriete(parametre):
    ## ---Initialisation---
    question = u"$(d_1)$ et $(d_2)$ sont elles parallèles :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    angle = random.randrange(90)
    parallele = random.randrange(2)
    if parallele:
        angle_droit = [ True , True ]
        reponse = u"$(d_1)$ et $(d_2)$ sont parallèles"
    else:
        angle_droit_manquant = random.randrange(3)
        if angle_droit_manquant == 0:
            angle_droit = [ True , False ]  
        elif angle_droit_manquant == 1:
            angle_droit = [ False , True ]  
        else:
            angle_droit = [ False , False ]  
        reponse = u"$(d_1)$ et $(d_2)$ ne sont pas parallèles"
    ## ---Redaction---
    tex_parallele_propriete(exo, angle, angle_droit)
    tex_parallele_propriete(cor, angle, angle_droit)
    cor.append("\\begin{center}")
    cor.append("\\fbox{%s}" %reponse)
    cor.append("\\end{center}")
    return (exo, cor, question)

def PerpendiculairePropriete(parametre):
    ## ---Initialisation---
    question = u"$(d_2)$ et $(d_3)$ sont elles perpendiculaires :"
    exo = []
    cor = []
    ## ---Calcul des paramètres---
    angle = random.randrange(90)
    perpendiculaire = random.randrange(2)
    if perpendiculaire:
        angle_droit = [ True , True ]
        reponse = u"$(d_2)$ et $(d_3)$ sont perpendiculaires"
    else:
        angle_droit_manquant = random.randrange(3)
        if angle_droit_manquant == 0:
            angle_droit = [ True , False ]  
        elif angle_droit_manquant == 1:
            angle_droit = [ False , True ]  
        else:
            angle_droit = [ False , False ]  
        reponse = u"$(d_2)$ et $(d_3)$ ne sont pas perpendiculaires"
    ## ---Redaction---
    tex_perpendiculaire_propriete(exo, angle, angle_droit)
    tex_perpendiculaire_propriete(cor, angle, angle_droit)
    cor.append("\\begin{center}")
    cor.append("\\fbox{%s}" %reponse)
    cor.append("\\end{center}")
    return (exo, cor, question)
