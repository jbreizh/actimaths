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

#------------------methode---------------------------------------------
def nom_point(nb):
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

def tex_itemize(enonce,listCaracteristique):
    enonce.append("\\begin{itemize}")
    for caracteristique in listCaracteristique:
        enonce.append("\\item %s"  % caracteristique)
    enonce.append("\\end{itemize}")

#------------------construction-----------------------------------------


def SommeQuelconque(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    question = u"%s est un triangle :" % nomAngle[0]
    exo = []
    cor = []
    a=random.randrange(20,80,5)
    b=random.randrange(20,80,5)
    c=180-a-b
    angle=random.sample(range(3),3)
    listCaracteristique = ["Quelconque",
                           "$\\widehat{%s}=%s^\\circ$" %(nomAngle[angle[0]],a),
                           "$\\widehat{%s}=%s^\\circ$" %(nomAngle[angle[1]],b)]
    tex_itemize(exo,listCaracteristique)
    exo.append("Calculer $\\widehat{%s}$" % (nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}=180^\\circ$$" % (nomAngle[angle[0]],nomAngle[angle[1]],nomAngle[angle[2]]))
    cor.append("$$%s^\\circ+%s^\\circ+\\widehat{%s}=180^\\circ$$" % (a,b,nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}=180^\\circ-%s^\\circ-%s^\\circ$$" % (nomAngle[angle[2]],a,b))
    cor.append("$$\\boxed{\\widehat{%s}=%s^\\circ}$$" % (nomAngle[angle[2]],c))
    return (exo, cor, question)

def SommeIsoceleBase(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    question = u"%s est un triangle :" % nomAngle[0]
    exo = []
    cor = []
    a=random.randrange(20,100,10)
    b=(180-a)/2
    c=(180-a)/2
    angle=random.sample(range(3),3)
    listCaracteristique = [u"Isocèle en %s" % nomSommet[angle[0]],
                           "$\\widehat{%s}=%s^\\circ$" % (nomAngle[angle[0]],a)]
    tex_itemize(exo,listCaracteristique)
    exo.append("Calculer $\\widehat{%s}$" % (nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}=180^\\circ$$" % (nomAngle[angle[0]],nomAngle[angle[1]],nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}=180^\\circ$$" % (nomAngle[angle[0]],nomAngle[angle[2]],nomAngle[angle[2]]))
    cor.append("$$%s^\\circ+2\\times\\widehat{%s}=180^\\circ$$" % (a,nomAngle[angle[2]]))
    cor.append("$$2\\times\\widehat{%s}=180^\\circ-%s^\\circ=%s^\\circ$$" % (nomAngle[angle[2]],a,2*b))
    cor.append("$$\\widehat{%s}=%s^\\circ \\div 2$$" % (nomAngle[angle[2]],2*b))
    cor.append("$$\\boxed{\\widehat{%s}=%s^\\circ}$$" % (nomAngle[angle[2]],b))
    return (exo, cor, question)

def SommeIsoceleSommet(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    question = u"%s est un triangle :" % nomAngle[0]
    exo = []
    cor = []
    a=random.randrange(20,100,10)
    b=(180-a)/2
    c=(180-a)/2
    angle=random.sample(range(3),3)
    listCaracteristique = [u"Isocèle en %s" % nomSommet[angle[0]],
                           "$\\widehat{%s}=%s^\\circ$" % (nomAngle[angle[2]],b)]
    tex_itemize(exo,listCaracteristique)
    exo.append("Calculer $\\widehat{%s}$" % (nomAngle[angle[0]]))
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}=180^\\circ$$" % (nomAngle[angle[0]],nomAngle[angle[1]],nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}=180^\\circ$$" % (nomAngle[angle[0]],nomAngle[angle[2]],nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}+%s^\\circ+%s^\\circ=180^\\circ$$" % (nomAngle[angle[0]],b,b))
    cor.append("$$\\widehat{%s}+%s^\\circ=180^\\circ$$" % (nomAngle[angle[0]],2*b))
    cor.append("$$\\widehat{%s}=180^\\circ-%s^\\circ$$" % (nomAngle[angle[0]],2*b))
    cor.append("$$\\boxed{\\widehat{%s}=%s^\\circ}$$" % (nomAngle[angle[0]],a))
    return (exo, cor, question)

def SommeRectangle(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    question = u"%s est un triangle :" % nomAngle[0]
    exo = []
    cor = []
    a = 90
    b = random.randrange(20,60,5)
    c = 90 - b
    angle=random.sample(range(3),3)
    listCaracteristique = ["Rectangle en %s" % nomSommet[angle[0]],
                           "$\\widehat{%s}=%s^\\circ$" %(nomAngle[angle[1]],b)]
    tex_itemize(exo,listCaracteristique)
    exo.append("Calculer $\\widehat{%s}$" % (nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}=180^\\circ$$" % (nomAngle[angle[0]],nomAngle[angle[1]],nomAngle[angle[2]]))
    cor.append("$$%s^\\circ+%s^\\circ+\\widehat{%s}=180^\\circ$$" % (a,b,nomAngle[angle[2]]))
    cor.append("$$\\widehat{%s}=180^\\circ-%s^\\circ-%s^\\circ$$" % (nomAngle[angle[2]],a,b))
    cor.append("$$\\boxed{\\widehat{%s}=%s^\\circ}$$" % (nomAngle[angle[2]],c))
    return (exo, cor, question)


def ConstruireQuelconque(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    question = u"Peut-on construire %s :" % nomAngle[0]
    exo = []
    cor = []
    a=random.randrange(20,80,5)
    b=random.randrange(20,80,5)
    c=180 - a - b
    possible = random.randrange(2)
    if possible == 0:
        c= c + random.randrange(5,25,5)
    angle=random.sample(range(3),3)
    listCaracteristique = ["$\\widehat{%s} = %s^\\circ$" %(nomAngle[angle[0]],a),
                           "$\\widehat{%s} = %s^\\circ$" %(nomAngle[angle[1]],b),
                           "$\\widehat{%s} = %s^\\circ$" %(nomAngle[angle[2]],c)]
    tex_itemize(exo,listCaracteristique)
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}$$" % (nomAngle[angle[0]],nomAngle[angle[1]],nomAngle[angle[2]]))
    cor.append("$$= %s^\\circ+%s^\\circ+%s^\\circ$$" % (a,b,c))
    if possible:
        cor.append("$$= %s^\\circ $$" % (a+b+c))
        cor.append("Un triangle %s est donc constructible." % nomAngle[0])
    else:
        cor.append("$$= %s^\\circ \\neq 180^\\circ $$" % (a+b+c))
        cor.append("Un triangle %s n'est pas donc constructible." % nomAngle[0])  
    return (exo, cor, question)

def ConstruireRectangle(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    question = u"Peut-on construire %s :" % nomAngle[0]
    exo = []
    cor = []
    a = 90
    b = random.randrange(20,60,5)
    c = 90 - b
    possible = random.randrange(2)
    if possible == 0:
        c= c + random.randrange(5,25,5)
    angle=random.sample(range(3),3)
    listCaracteristique = ["Rectangle en %s" % nomSommet[angle[0]],
                           "$\\widehat{%s} = %s^\\circ$" %(nomAngle[angle[1]],b),
                           "$\\widehat{%s} = %s^\\circ$" %(nomAngle[angle[2]],c)]
    tex_itemize(exo,listCaracteristique)
    cor.append("$$\\widehat{%s}+\\widehat{%s}+\\widehat{%s}$$" % (nomAngle[angle[0]],nomAngle[angle[1]],nomAngle[angle[2]]))
    cor.append("$$= %s^\\circ+%s^\\circ+%s^\\circ$$" % (a,b,c))
    if possible:
        cor.append("$$= %s^\\circ $$" % (a+b+c))
        cor.append("Un triangle %s est donc constructible." % nomAngle[0])
    else:
        cor.append("$$= %s^\\circ \\neq 180^\\circ $$" % (a+b+c))
        cor.append("Un triangle %s n'est pas donc constructible." % nomAngle[0])  
    return (exo, cor, question)

def InequaliteTriangulaire(parametre):
    nomSommet=nom_point(3)
    nomAngle=nom_angle(nomSommet)
    nomCote=nom_cote(nomSommet)
    question = u"Peut-on construire %s :" % nomAngle[0]
    exo = []
    cor = []
    a = random.randrange(2,6)
    b = a + random.randrange(2,5)
    possible = random.randrange(3)
    if possible == 0:
        c= random.randrange( a + b + 1, a + b + a )
    elif possible == 1:
        c= a + b
    else:
        c= random.randrange( a + b - a, a + b )
    cote = random.sample(range(3),3)
    listCaracteristique = ["$ %s =  \\unit[%s]{%s} $" %(nomCote[cote[0]],a,'cm'),
                           "$ %s =  \\unit[%s]{%s} $" %(nomCote[cote[1]],b,'cm'),
                           "$ %s =  \\unit[%s]{%s} $" %(nomCote[cote[2]],c,'cm')]
    tex_itemize(exo,listCaracteristique)
    cor.append("$$ %s + %s = %s + %s = \\unit[%s]{%s} $$" % (nomCote[cote[0]],nomCote[cote[1]],a,b,a+b,'cm'))
    cor.append("$$ %s = \\unit[%s]{%s} $$" % (nomCote[cote[2]],c,'cm'))
    if possible == 0:
        cor.append("$$ %s + %s < %s $$" % (nomCote[cote[0]],nomCote[cote[1]],nomCote[cote[2]]))
        cor.append("%s n'est pas constructible" % nomAngle[0])
    elif possible == 1:
        cor.append("$$ %s + %s = %s $$" % (nomCote[cote[0]],nomCote[cote[1]],nomCote[cote[2]]))
        cor.append("%s n'est pas constructible \\newline" % nomAngle[0])
        cor.append(u"Les points %s, %s et %s sont alignés" % (nomSommet[0],nomSommet[1],nomSommet[2]))
    else:
        cor.append("$$ %s + %s > %s $$" % (nomCote[cote[0]],nomCote[cote[1]],nomCote[cote[2]]))
        cor.append("%s est constructible" % nomAngle[0])
    return (exo, cor, question)
