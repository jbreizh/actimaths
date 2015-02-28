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
from math import *
from outils.Affichage import decimaux
from outils.Fractions import Fractions  #fractions pyromaths

def couple (): 
    A=(float(random.randrange(-8,9))/2,float(random.randrange(-8,9))/2)
    B=(float(random.randrange(-8,9))/2,float(random.randrange(-8,9))/2)
    while not validedroite(A,B):
        B=(float(random.randrange(-8,9))/2,float(random.randrange(-8,9))/2)
    return (A,B)

def validedroite(A,B):  #valide le choix du couple A B pour qu'ils ne soient pas "collés", la droite (AB) ne sera ni horizontale ni verticale
    rep=True
    if abs(A[0]-B[0])<=1 and abs(A[1]-B[1])<=1:
        rep=False
    if A[0]==B[0] or A[1]==B[1]:
        rep=False
    if abs(A[0]-B[0])<1 or abs(A[1]-B[1])<1:
        rep=False
    return rep

def extreme(a,b,xmin,xmax,ymin,ymax):  #donne les extremités de la droite passant par a et b (coordonnées)
    res=[]
    x1=float(a[0])
    x2=float(b[0])
    y1=float(a[1])
    y2=float(b[1])
    coef=float((y1-y2)/(x1-x2))
    if coef != 0:
        xsort1=float(x1+(ymin-y1)/coef) #abscisse du point d'ordonnée ymin
        if xsort1 >=xmin and xsort1<=xmax and not(xsort1,ymin) in res:
            res.append((xsort1,ymin))
        xsort2=float(x2+(ymax-y2)/coef) #abscisse du point d'ordonnée ymax
        if xsort2>=xmin and xsort2<=xmax and not(xsort2,ymax) in res:
            res.append((xsort2,ymax))
        ysort1=float(y1+coef*(xmin-x1))  #ordonnée du point d'abscisse xmin
        if ysort1 >=ymin and ysort1<=ymax and not (xmin,ysort1)in res:
            res.append((xmin,ysort1))
        ysort2=float(y2+coef*(xmax-x2))  #ordonnée du point d'abscisse xmax
        if ysort2 >=ymin and ysort2<=ymax and not(xmax,ysort2) in res:
            res.append((xmax,ysort2))
    else:
        res=[(xmin,y1),(xmax,y1)]
    return res

#
##---------------------AFICHAGE-------------------------------
def tracedroite(A,B,xmin,xmax,ymin,ymax): #trace la droite (AB)
    l=extreme(A,B,xmin,xmax,ymin,ymax)
    return "\\psline "+str(l[0])+str(l[1])

def doublefleche(A,B):
    #trace une flèche "double" de justification en pointillés
    mid=(float((A[0]+B[0]))/2,float((A[1]+B[1]))/2)
    res1="\\psline[linestyle=dashed,linewidth=1.1pt]{->}"+str(A)+str(mid)+'\n '
    res2="\\psline[linestyle=dashed,linewidth=1.1pt]{->}"+str(mid)+str(B)
    res=res1+res2
    if A==B:
        res=""
    return res

def nomdroite(i,coordo):
    #place le nom de la droite (d_i) sur le graphique aux coordonnées coordo
    x0=coordo[0]
    y0=coordo[1]
    if x0!=0:
        x=x0/abs(x0)*(abs(x0)+0.5)
    else:
        x=0
    if y0!=0:
        y=y0/abs(y0)*(abs(y0)+0.5)
    else:
        y=0
    return "\\rput"+str((x,y))+"{($d_"+str(i)+"$)}"

def tex_repere(enonce, A, B, nom):
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-5)(5,5)")
    enonce.append("\\psgrid[ gridcolor=lightgray, subgriddiv=2, subgridcolor=lightgray, gridlabels=6pt](0,0)(-5,-5)(5,5)")
    enonce.append("\\psline[linewidth=1.2pt]{->}(-5,0)(5,0)")
    enonce.append("\\psline[linewidth=1.2pt]{->}(0,-5)(0,5)")
    enonce.append(tracedroite(A,B,-5,5,-5,5))
    enonce.append(nom)
    enonce.append("\\end{pspicture}")

def LireImage(parametre):
    question = u"Donner l'image de :"
    exo = []
    cor = []
    (A,B)=couple()
    l1=extreme(A,B,-5,5,-5,5)
    nom= nomdroite(1,l1[0])
    tex_repere(exo, A, B, nom)
    tex_repere(cor, A, B, nom)
    return(exo, cor, question)

