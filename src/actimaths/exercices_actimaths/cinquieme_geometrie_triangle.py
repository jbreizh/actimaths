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

import random, math

#------------------methode---------------------------------------------
def nom_sommet(nb):
    (listenb, listepts) = ([], [])
    for i in range(26):
        listenb.append(i + 65)
    for i in range(nb):
        listepts.append(str(chr(listenb.pop(random.randrange(26 - i)))))
    listepts.sort()
    return tuple(listepts)

def nom_angle(nomPoint):
    nomAngle = []
    nomAngle.append("%s%s%s" % (nomPoint[2],nomPoint[0],nomPoint[1]))
    nomAngle.append("%s%s%s" % (nomPoint[0],nomPoint[1],nomPoint[2]))
    nomAngle.append("%s%s%s" % (nomPoint[1],nomPoint[2],nomPoint[0]))
    return nomAngle

def nom_cote(nomPoint):
    nomCote = []
    nomCote.append("%s%s" % (nomPoint[0],nomPoint[1]))
    nomCote.append("%s%s" % (nomPoint[1],nomPoint[2]))
    nomCote.append("%s%s" % (nomPoint[2],nomPoint[0]))
    return nomCote

def mesure_angle(type):
    if type == 'isocele':
        while True:
            a = random.randrange(20,100,10)
            if a != 60 and a != 90:
                break
        mesure = [(180-a)/2, (180-a)/2, a]
    elif type == 'rectangle':
        while True:
            a = random.randrange(20,60,5)
            if a != 45:
                break
        mesure = [a, 90 - a, 90]
    elif type == 'quelconque':
        while True:
            a = random.randrange(20,80,5)
            b = random.randrange(20,80,5)
            c = 180 - a - b
            if a != 90 and b != 90 and c != 90 and a != b and b != c and c != a :
                break
        mesure = [a, b, c]
    return mesure

def choix_angle(type):
    if type == 'isocele':
        while True:
            choix = random.sample(range(3),3)
            if choix[2] != 1:
                break
    elif type == 'rectangle':
        while True:
            choix = random.sample(range(3),3)
            if choix[2] != 2:
                break
    elif type == 'quelconque':
        choix = random.sample(range(3),3)
    return choix

def tex_mesure_angle(mesure, choix):
    tex_mesure_enonce = []
    tex_mesure_corrige = []
    for i in range(len(mesure)):
        if i == choix[2]:
            tex_mesure_enonce.append("?^\\circ")
            tex_mesure_corrige.append("\\boxed{%s^\\circ}" % mesure[i])
        else:
            tex_mesure_enonce.append("%s^\\circ" % mesure[i])
            tex_mesure_corrige.append("%s^\\circ" % mesure[i])
    return tex_mesure_enonce, tex_mesure_corrige

def tex_triangle(tex, sommet, mesure, tex_mesure):
    # Coefficient tel que hauteur = gamma * base
    gamma = math.tan(math.radians(mesure[0]))*math.tan(math.radians(mesure[1]))/(math.tan(math.radians(mesure[0]))+math.tan(math.radians(mesure[1])))
    # Coordonnée des sommets pour que la base ou la hauteur mesure (max-min) cm
    min = -4
    max = 4
    if gamma < 1:
        coordonnee = [min, min, max, min, round((max-min)*gamma/math.tan(math.radians(mesure[0]))+min, 4),round((max-min)*gamma+min,4)]
    else:
        coordonnee = [min, min, round((max-min)/gamma+min, 4), min, round((max-min)/math.tan(math.radians(mesure[0])) +min, 4) ,max]
    # Angle des symboles des angles
    angle = [0, mesure[0], 180 - mesure[1], 180, 180 + mesure[0], 180 + mesure[0] + mesure[2]]
    ## Construction
    tex.append("\\begin{center}")
    tex.append("\\psset{unit=0.5cm}")
    tex.append("\\begin{pspicture}(%s,%s)(%s,%s)" %(coordonnee[0]-1, coordonnee[1]-1, coordonnee[2]+1, coordonnee[5]+1))
    # Triangle
    tex.append("\\pstTriangle(%s,%s){%s}(%s,%s){%s}(%s,%s){%s}" %(coordonnee[0], coordonnee[1], sommet[0], coordonnee[2], coordonnee[3], sommet[1], coordonnee[4], coordonnee[5], sommet[2]))
    # Symbole et légende de chaque angle
    for i in range(len(mesure)):
        if mesure[i] == 90:
           tex.append("\\pstRightAngle{%s}{%s}{%s}" % ( sommet[(i+1)%3], sommet[i], sommet[(i-1)%3]))
        elif mesure[0] == mesure[1] and i < 2:
           tex.append("\\pstMarkAngle{%s}{%s}{%s}{}" % ( sommet[(i+1)%3], sommet[i], sommet[(i-1)%3]))
           tex.append("\\uput{0.75}[%s]{%s}(%s,%s){\\psline(0,0)(0.5,0)}" % ((angle[2*i]+angle[2*i+1])/2, (angle[2*i]+angle[2*i+1])/2, coordonnee[2*i], coordonnee[2*i+1]))
           if i == 0:
               tex.append("\\pstMarkAngle{%s}{%s}{%s}{$%s$}" % ( sommet[(i+1)%3], sommet[i], sommet[(i-1)%3], tex_mesure[i]))
        else:
           tex.append("\\pstMarkAngle{%s}{%s}{%s}{$%s$}" % ( sommet[(i+1)%3], sommet[i], sommet[(i-1)%3], tex_mesure[i]))
    tex.append("\\end{pspicture}")
    tex.append("\\end{center}")

def tex_itemize(enonce,liste):
    enonce.append("\\begin{itemize}")
    for element in liste:
        enonce.append("\\item %s"  % element)
    enonce.append("\\end{itemize}")

#------------------construction-----------------------------------------
def SommeQuelconque(parametre):
    ## Choix des variables
    sommet = nom_sommet(3)
    mesure = mesure_angle('quelconque')
    choix = choix_angle('quelconque')
    (tex_mesure_enonce, tex_mesure_corrige) = tex_mesure_angle(mesure, choix)
    ## Initialisation
    question = "Calculer $\\widehat{%s}$" % (sommet[choix[2]])
    exo = []
    cor = []
    exo.append(u"%s%s%s est un triangle tel que:" % (sommet[0], sommet[1], sommet[2]))
    cor.append(u"%s%s%s est un triangle tel que:" % (sommet[0], sommet[1], sommet[2]))
    ## Enonce
    liste_caracteristique_enonce = []
    liste_caracteristique_corrige = []
    for i in range(len(mesure)):
        liste_caracteristique_enonce.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure_enonce[i]))
        liste_caracteristique_corrige.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure_corrige[i]))
    tex_itemize(exo,liste_caracteristique_enonce)
    tex_itemize(cor,liste_caracteristique_corrige)
    ## Corrigé
    cor.append("$$%s+%s+%s=180^\\circ$$" % (tex_mesure_enonce[choix[2]],tex_mesure_enonce[choix[0]], tex_mesure_enonce[choix[1]]))
    cor.append("$$\\widehat{%s}=180^\\circ - %s - %s = %s$$" % (sommet[choix[2]],tex_mesure_corrige[choix[0]],tex_mesure_corrige[choix[1]], tex_mesure_corrige[choix[2]]))
    return (exo, cor, question)

def SommeQuelconqueSchema(parametre):
    ## Choix des variables
    sommet = nom_sommet(3)
    mesure = mesure_angle('quelconque')
    choix = choix_angle('quelconque')
    (tex_mesure_enonce, tex_mesure_corrige) = tex_mesure_angle(mesure, choix)
    ## Initialisation
    question = "Calculer $\\widehat{%s}$" % sommet[choix[2]]
    exo = []
    cor = []
    ## Figure
    tex_triangle(exo, sommet, mesure, tex_mesure_enonce)
    tex_triangle(cor, sommet, mesure, tex_mesure_corrige)
    ## Corrigé
    cor.append("$$%s+%s+%s=180^\\circ$$" % (tex_mesure_enonce[choix[2]],tex_mesure_enonce[choix[0]], tex_mesure_enonce[choix[1]]))
    cor.append("$$\\widehat{%s}=180^\\circ - %s - %s = %s$$" % (sommet[choix[2]],tex_mesure_corrige[choix[0]],tex_mesure_corrige[choix[1]], tex_mesure_corrige[choix[2]]))
    return (exo, cor, question)

def SommeIsocele(parametre):
    ## Choix des variables
    sommet = nom_sommet(3)
    mesure = mesure_angle('isocele')
    choix = choix_angle('isocele')
    (tex_mesure_enonce, tex_mesure_corrige) = tex_mesure_angle(mesure, choix)
    ## Initialisation
    question = "Calculer $\\widehat{%s}$" % (sommet[choix[2]])
    exo = []
    cor = []
    exo.append(u"%s%s%s est isocèle en %s tel que:" % (sommet[0], sommet[1], sommet[2], sommet[2]))
    cor.append(u"%s%s%s est isocèle en %s tel que:" % (sommet[0], sommet[1], sommet[2], sommet[2]))
    ## Enonce
    liste_caracteristique_enonce = []
    liste_caracteristique_corrige = []
    for i in [0,2]:
        liste_caracteristique_enonce.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure_enonce[i]))
        liste_caracteristique_corrige.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure_corrige[i]))
    tex_itemize(exo,liste_caracteristique_enonce)
    tex_itemize(cor,liste_caracteristique_corrige)
    ## Corrigé
    if choix[2] == 2:
        cor.append("$$%s + 2\\times %s=180^\\circ$$" % (tex_mesure_enonce[choix[2]], tex_mesure_enonce[0]))
        cor.append("$$\\widehat{%s}=180^\\circ - 2\\times %s = %s$$" % (sommet[choix[2]],tex_mesure_corrige[0], tex_mesure_corrige[choix[2]]))
    else:
        cor.append("$$2\\times %s + %s =180^\\circ$$" % (tex_mesure_enonce[choix[2]], tex_mesure_enonce[2]))
        cor.append("$$\\widehat{%s}= (180^\\circ - %s) \\div 2 = %s$$" % (sommet[choix[2]],tex_mesure_corrige[2], tex_mesure_corrige[choix[2]]))
    return (exo, cor, question)

def SommeIsoceleSchema(parametre):
    ## Choix des variables
    sommet = nom_sommet(3)
    mesure = mesure_angle('isocele')
    choix = choix_angle('isocele')
    (tex_mesure_enonce, tex_mesure_corrige) = tex_mesure_angle(mesure, choix)
    ## Initialisation
    question = "Calculer $\\widehat{%s}$" % sommet[choix[2]]
    exo = []
    cor = []
    ## Figure
    tex_triangle(exo, sommet, mesure, tex_mesure_enonce)
    tex_triangle(cor, sommet, mesure, tex_mesure_corrige)
    ## Corrigé
    if choix[2] == 2:
        cor.append("$$%s + 2\\times %s=180^\\circ$$" % (tex_mesure_enonce[choix[2]], tex_mesure_enonce[0]))
        cor.append("$$\\widehat{%s}=180^\\circ -2\\times %s = %s$$" % (sommet[choix[2]],tex_mesure_corrige[0], tex_mesure_corrige[choix[2]]))
    else:
        cor.append("$$2\\times %s + %s =180^\\circ$$" % (tex_mesure_enonce[choix[2]], tex_mesure_enonce[2]))
        cor.append("$$\\widehat{%s}= (180^\\circ - %s) \\div 2 = %s$$" % (sommet[choix[2]],tex_mesure_corrige[2], tex_mesure_corrige[choix[2]]))
    return (exo, cor, question)

def SommeRectangle(parametre):
    ## Choix des variables
    sommet = nom_sommet(3)
    mesure = mesure_angle('rectangle')
    choix = choix_angle('rectangle')
    (tex_mesure_enonce, tex_mesure_corrige) = tex_mesure_angle(mesure, choix)
    ## Initialisation
    question = "Calculer $\\widehat{%s}$" % (sommet[choix[2]])
    exo = []
    cor = []
    exo.append(u"%s%s%s est rectangle en %s tel que:" % (sommet[0], sommet[1], sommet[2], sommet[2]))
    cor.append(u"%s%s%s est rectangle en %s tel que:" % (sommet[0], sommet[1], sommet[2], sommet[2]))
    ## Enonce
    liste_caracteristique_enonce = []
    liste_caracteristique_corrige = []
    for i in [0,2]:
        liste_caracteristique_enonce.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure_enonce[i]))
        liste_caracteristique_corrige.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure_corrige[i]))
    tex_itemize(exo,liste_caracteristique_enonce)
    tex_itemize(cor,liste_caracteristique_corrige)
    ## Corrigé
    cor.append("$$ %s + %s + %s =180^\\circ$$" % (tex_mesure_enonce[choix[2]],tex_mesure_enonce[choix[0]],tex_mesure_enonce[choix[1]]))
    cor.append("$$\\widehat{%s}=180^\\circ - %s - %s = %s$$" % (sommet[choix[2]],tex_mesure_enonce[choix[0]],tex_mesure_enonce[choix[1]], tex_mesure_corrige[choix[2]]))
    return (exo, cor, question)

def SommeRectangleSchema(parametre):
    ## Choix des variables
    sommet = nom_sommet(3)
    mesure = mesure_angle('rectangle')
    choix = choix_angle('rectangle')
    (tex_mesure_enonce, tex_mesure_corrige) = tex_mesure_angle(mesure, choix)
    ## Initialisation
    question = "Calculer $\\widehat{%s}$" % (sommet[choix[2]])
    exo = []
    cor = []
    ## Figure
    tex_triangle(exo, sommet, mesure, tex_mesure_enonce)
    tex_triangle(cor, sommet, mesure, tex_mesure_corrige)
    ## Corrigé
    cor.append("$$ %s + %s + %s =180^\\circ$$" % (tex_mesure_enonce[choix[2]],tex_mesure_enonce[choix[0]],tex_mesure_enonce[choix[1]]))
    cor.append("$$\\widehat{%s}=180^\\circ - %s - %s = %s$$" % (sommet[choix[2]],tex_mesure_enonce[choix[0]],tex_mesure_enonce[choix[1]], tex_mesure_corrige[choix[2]]))
    return (exo, cor, question)

def ConstruireQuelconque(parametre):
    ## Choix des variables
    sommet= nom_sommet(3)
    mesure = mesure_angle('quelconque')
    if random.randrange(2):
        mesure[2] = mesure[2] + random.randrange(5,25,5)
    somme_angle = mesure[0] + mesure[1] + mesure[2]
    tex_mesure = []
    for i in range(len(mesure)):
        tex_mesure.append("%s^\\circ" % mesure[i])
    ## Initialisation
    question = u"Peut-on construire un triangle %s%s%s tel que:" % (sommet[0], sommet[1], sommet[2])
    exo = []
    cor = []
    ## Enonce
    liste_caracteristique = []
    for i in range(len(mesure)):
        liste_caracteristique.append("$\\widehat{%s}=%s$" %(sommet[i],tex_mesure[i]))
    tex_itemize(exo,liste_caracteristique)
    tex_itemize(cor,liste_caracteristique)
    ## Corrigé
    if somme_angle == 180:
        cor.append("$$ \\widehat{%s} + \\widehat{%s} + \\widehat{%s} = %s + %s + %s = %s^\\circ$$" % (sommet[0], sommet[1], sommet[2], tex_mesure[0], tex_mesure[1], tex_mesure[2], somme_angle))
        cor.append("Un triangle %s%s%s est constructible." % (sommet[0], sommet[1], sommet[2]))
    else:
        cor.append("$$ \\widehat{%s} + \\widehat{%s} + \\widehat{%s} = %s + %s + %s = %s^\\circ \\neq 180^\\circ$$" % (sommet[0], sommet[1], sommet[2], tex_mesure[0], tex_mesure[1], tex_mesure[2], somme_angle))
        cor.append("Un triangle %s%s%s n'est pas constructible." % (sommet[0], sommet[1], sommet[2]))
    return (exo, cor, question)

def ConstruireQuelconqueSchema(parametre):
    ## Choix des variables
    sommet= nom_sommet(3)
    mesure = mesure_angle('quelconque')

    mesure_2 = []
    for angle in mesure:
        mesure_2.append(angle)
    if random.randrange(2):
        mesure_2[2] = mesure_2[2] + random.randrange(5,25,5)

    somme_angle = mesure_2[0] + mesure_2[1] + mesure_2[2]
    tex_mesure = []
    for i in range(len(mesure)):
        tex_mesure.append("%s^\\circ" % mesure_2[i])
    ## Initialisation
    question = u"Peut-on construire un triangle %s%s%s tel que:" % (sommet[0], sommet[1], sommet[2])
    exo = []
    cor = []
    ## Figure
    tex_triangle(exo, sommet, mesure, tex_mesure)
    tex_triangle(cor, sommet, mesure, tex_mesure)
    ## Corrigé
    if somme_angle == 180:
        cor.append("$$ \\widehat{%s} + \\widehat{%s} + \\widehat{%s} = %s + %s + %s = %s^\\circ$$" % (sommet[0], sommet[1], sommet[2], tex_mesure[0], tex_mesure[1], tex_mesure[2], somme_angle))
        cor.append("Un triangle %s%s%s est constructible." % (sommet[0], sommet[1], sommet[2]))
    else:
        cor.append("$$ \\widehat{%s} + \\widehat{%s} + \\widehat{%s} = %s + %s + %s = %s^\\circ \\neq 180^\\circ$$" % (sommet[0], sommet[1], sommet[2], tex_mesure[0], tex_mesure[1], tex_mesure[2], somme_angle))
        cor.append("Un triangle %s%s%s n'est pas constructible." % (sommet[0], sommet[1], sommet[2]))
    return (exo, cor, question)

def InequaliteTriangulaire(parametre):
    ## Choix des variables
    sommet=nom_sommet(3)
    nomCote=nom_cote(sommet)
    a = random.randrange(2,6)
    b = a + random.randrange(2,5)
    possible = random.randrange(3)
    if possible == 0:
        c= random.randrange( a + b + 1, a + b + a )
    elif possible == 1:
        c= a + b
    else:
        c= random.randrange( a + b - a, a + b )
    mesure = [a, b, c]
    cote = random.sample(range(3),3)
    ## Initialisation
    question = u"Peut-on construire %s%s%s :"  % (sommet[0], sommet[1], sommet[2])
    exo = []
    cor = []
    ## Enonce
    liste_caracteristique = []
    for i in range(len(mesure)):
        liste_caracteristique.append("$ %s =  \\unit[%s]{cm} $" %(nomCote[cote[i]], mesure[i]))
    tex_itemize(exo,liste_caracteristique)
    ## Corrigé
    cor.append("$$ %s + %s = %s + %s = \\unit[%s]{%s} $$" % (nomCote[cote[0]],nomCote[cote[1]],a,b,a+b,'cm'))
    cor.append("$$ %s = \\unit[%s]{%s} $$" % (nomCote[cote[2]],c,'cm'))
    if possible == 0:
        cor.append("$$ %s + %s < %s $$" % (nomCote[cote[0]],nomCote[cote[1]],nomCote[cote[2]]))
        cor.append("%s%s%s n'est pas constructible" % (sommet[0], sommet[1], sommet[2]))
    elif possible == 1:
        cor.append("$$ %s + %s = %s $$" % (nomCote[cote[0]],nomCote[cote[1]],nomCote[cote[2]]))
        cor.append("%s%s%s n'est pas constructible \\newline"  % (sommet[0], sommet[1], sommet[2]))
        cor.append(u"Les points %s, %s et %s sont alignés" % (sommet[0],sommet[1],sommet[2]))
    else:
        cor.append("$$ %s + %s > %s $$" % (nomCote[cote[0]],nomCote[cote[1]],nomCote[cote[2]]))
        cor.append("%s%s%s est constructible" % (sommet[0], sommet[1], sommet[2]))
    return (exo, cor, question)
