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

def randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

def range_float(start, stop, step):
    liste = range(int(start/step),int(stop/step))
    for i in range(len(liste)):
        liste[i] = liste[i]* step
    return liste

def noms_sommets(nb):
    """Renvoie nb noms de sommets"""
    (listenb, listepts) = ([], [])
    for i in range(26):
        listenb.append(i + 65)
    for i in range(nb):
        listepts.append(str(chr(listenb.pop(random.randrange(26 - i)))))
    listepts.sort()
    return tuple(listepts)

def abscissePoint(nbre_point,abscisse_min,abscisse_max,pas):
    abscisse = random.sample(range_float(abscisse_min,abscisse_max,pas), nbre_point)
    return abscisse

def place_points(abscisse,points,hauteur):
    text="\\pstGeonode[PointSymbol=x,PosAngle={90},PointNameSep=%s]" % hauteur
    i=0
    while i<len(abscisse):
        text=text+"("+str(abscisse[i])+",0)"+"{"+str(points[i])+"}"
        i=i+1
    return text

def tex_axe_gradue(enonce,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation):
    unite=float(4.5)/(abscisse_max-abscisse_min)
    hauteur=float(1)/unite
    Graduation= int(ecartGraduation/pas)
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=%scm}" % unite)
    enonce.append("\\begin{pspicture}(%s,%s)(%s,%s)" % (abscisse_min,-hauteur,abscisse_max,hauteur))
    enonce.append("\\psaxes[yAxis=false,Ox=%s,Dx=%s,subticks=%s]{->}(%s,0)(%s,-1)(%s,1)"
                  % (abscisse_min,ecartGraduation,Graduation,abscisse_min,abscisse_min,abscisse_max))
    enonce.append(place_points(abscisse,points,0.3*hauteur))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation):
    question="Donner les abscisses :"
    exo = [ ]
    cor = [ ]
    points=(noms_sommets(4))
    abscisse=abscissePoint(4,abscisse_min,abscisse_max,pas)
    tex_axe_gradue(exo,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation)
    exo.append("\\begin{center}")
    exo.append("du point %s"% points[0])
    exo.append("\\end{center}")
    tex_axe_gradue(cor,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation)
    cor.append("\\begin{center}")
    cor.append("L\'abscisse de %s est %s ou \\boxed{%s(%s)}" % (points[0],abscisse[0],points[0],abscisse[0]))
    cor.append("\\end{center}")
    return (exo, cor, question)

def LireAbscisseEntierOrigine(parametre):
    pas = 1
    abscisse_min=0
    abscisse_max=random.randrange(5, parametre[0] + 1)
    ecartGraduation = random.randrange(2,5)
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def LireAbscisseEntier(parametre):
    pas = 1
    abscisse_min=random.randrange(parametre[0], parametre[0] + 20)
    abscisse_max=abscisse_min+random.randrange(5,15)
    ecartGraduation = random.randrange(2,5)
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def LireAbscisseDecimalOrigine(parametre):
    pas = randrange_float(0.1, 0.2, 0.1)
    abscisse_min=0
    abscisse_max=randrange_float(2, parametre[0], pas)
    ecartGraduation = 1
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def LireAbscisseDecimal(parametre):
    pas = randrange_float(0.1, 0.2, 0.1)
    abscisse_min = randrange_float(parametre[0], parametre[0] + 20,1)
    abscisse_max = abscisse_min + randrange_float(2,5,pas)
    ecartGraduation = 1
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def LireAbscisseFractionOrigine(parametre):
    pas = float(1)/random.randrange(2,10)
    abscisse_min=0
    abscisse_max=randrange_float(2, parametre[0], pas)
    ecartGraduation = 1
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def LireAbscisseFraction(parametre):
    pas = float(1)/random.randrange(2,10)
    abscisse_min = randrange_float(parametre[0], parametre[0] + 20,1)
    abscisse_max = abscisse_min + randrange_float(2,5,pas)
    ecartGraduation = 1
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)
