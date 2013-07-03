# Pyromaths
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
# along with this program; if notPopen, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

import random
from outils.Affichage import decimaux


#
##---------------------------VALEURS-----------------------------------
def noms_sommets(nb):   #Renvoie nb noms de sommets
    (listenb, listepts) = ([], [])
    for i in range(26):
        listenb.append(i + 65)
    for i in range(nb):
        listepts.append(str(chr(listenb.pop(random.randrange(26 - i)))))
    listepts.sort()
    return tuple(listepts)

def angle(coordo):    #Angle pour placer le nom du point en fonction du quadrant
    l=[]
    for coord in coordo:
        if coord[0]>=0 and coord[1]>=0:
            ang='45'
        if coord[0]>=0 and coord[1]<0:
            ang='-45'
        if coord[0]<0 and coord[1]<0:
            ang='-135'
        if coord[0]<0 and coord[1]>=0:
            ang='135'
        l.append(ang)
    return l

def valide(coord,liste_coord):  #Évite deux points trop proches l'un de l'autre
    rep=True
    for c in liste_coord:
        if abs(coord[0]-c[0])<=0.5 and abs(coord[1]-c[1])<=0.5:
            rep=False
            break
    return rep

def quadrant(coord,liste_coord):   #Évite 2 points dans le même quadrant
    rep= True
    for c in liste_coord:
        if coord[0]*c[0]>=0 and coord[1]*c[1]>=0:
            rep=False
            break
    return rep

def coordo_pts(nb):  #Génère une liste de nb coordonnées. Je m'arrange pour avoir des points sur les 4 quadrants et sur les deux axes
    j=0
    k=0
    l=[]
    i=0
    while i<4 and i<nb:
        j=j+1
        if j==600:
            break
        a=float(random.randrange(-9,10))/2
        b=float(random.randrange(-9,10))/2
        if ((a,b) not in l) and valide((a,b),l)and quadrant((a,b),l):
            l.append((a,b))
            i=i+1
    if nb>=4:
        a=float(random.randrange(-9,10))/2
        while not valide((0,a),l):
            a=float(random.randrange(-9,10))/2
        rg=random.randrange(0,len(l)-1)
        l[rg:rg]=[(0,a)]
        i=i+1

    if nb>=5:
        b=float(random.randrange(-9,10))/2
        while not valide((b,0),l):
            b=float(random.randrange(-9,10))/2
        rg=random.randrange(0,len(l)-1)
        l[rg:rg]=[(b,0)]
        i=i+1

    while i>=6 and i<nb and i<10:
        a=float(random.randrange(-9,10))/2
        b=float(random.randrange(-9,10))/2
        j=j+1
        if j==600:
            break
        if ((a,b) not in l) and valide((a,b),l)and quadrant((a,b),l[6:i]):
            l.append((a,b))
            i=i+1
    if nb>=11 and len(l)==10:
        a=float(random.randrange(-9,10))/2
        while not valide((0,a),l):
            a=float(random.randrange(-9,10))/2
        rg=random.randrange(6,len(l)-1)
        l[rg:rg]=[(0,a)]
        i=i+1
    if nb>=11 and len(l)==11:
        b=float(random.randrange(-9,10))/2
        while not valide((b,0),l):
            b=float(random.randrange(-9,10))/2
        rg=random.randrange(6,len(l)-1)
        l[rg:rg]=[(b,0)]
        i=i+1

    while i>=12 and i<nb :
        a=float(random.randrange(-9,10))/2
        b=float(random.randrange(-9,10))/2
        k=k+1
        if k==600:
            break
        if ((a,b) not in l) and valide((a,b),l):
            l.append((a,b))
            i=i+1
    return l

#
##---------------------------AFFICHAGE-----------------------------------
def tex_points(coordo,points):  #coordo: liste de coordonnées ; points : noms des points associés ; génère le code latex pour placer tous les points
    l= angle(coordo)
    text="\\pstGeonode[PointSymbol=x,PosAngle={"
    for ang in l :
        text=text+ang+','
    text=text+"},PointNameSep=0.4]"
    i=0
    while i<len(coordo):
        text=text+str(coordo[i])+"{"+str(points[i])+"}"
        i=i+1
    return text

def tex_coord(coord):  #Affiche les coordonnées des points au format LaTeX
    return '\\hbox{$('+decimaux(str(coord[0]), 1) + '~;~' + decimaux(str(coord[1]), 1)+')$}'

def tex_repere(enonce, coord_pts, noms_pts):  #Affiche le repère avecles points au format LaTeX
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-5)(5,6)")
    enonce.append("\\psgrid[ gridcolor=lightgray, subgriddiv=2, subgriddots=4,subgridcolor=lightgray, gridlabels=6pt](0,0)(-5,-5)(5,5)")
    enonce.append("\\psline[linewidth=1.2pt]{->}(-5,0)(5,0)")
    enonce.append("\\psline[linewidth=1.2pt]{->}(0,-5)(0,5)")
    enonce.append(tex_points(coord_pts,noms_pts))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

#
##---------------------------CONSTRUCTION-----------------------------------
def Lire( parametre ):
    question = u"Donner les coordonnées :"
    exo = []
    cor = []
    nb_pts = 6
    noms_pts = random.sample(noms_sommets(nb_pts),4)
    coord_pts = random.sample(coordo_pts(nb_pts),4)
    question_pts = random.sample(range(4),1)
    tex_repere(exo, coord_pts, noms_pts)
    tex_repere(cor, coord_pts, noms_pts)
    exo.append("\\begin{center}")
    exo.append(u"du point %s" % noms_pts[question_pts[0]])
    exo.append("\\end{center}")
    cor.append("\\begin{center}")
    cor.append(u"\\boxed{%s %s} "% (noms_pts[question_pts[0]],tex_coord(coord_pts[question_pts[0]])))
    cor.append("\\end{center}")
    return(exo, cor, question)
