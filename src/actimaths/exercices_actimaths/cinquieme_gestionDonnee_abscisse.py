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
    question = "Donner les abscisses :"
    exo = []
    cor = []
    points=(noms_sommets(4))
    abscisse=abscissePoint(4,abscisse_min,abscisse_max,pas)
    tex_axe_gradue(exo,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation)
    exo.append(u"\\newline Des points %s et %s" % (points[0],points[1]))
    tex_axe_gradue(cor,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation)
    cor.append("l\'abscisse de %s est %s ou %s(%s) \\newline" % (points[0],abscisse[0],points[0],abscisse[0]))
    cor.append("l\'abscisse de %s est %s ou %s(%s)" % (points[1],abscisse[1],points[1],abscisse[1]))
    return (exo, cor, question)

def tex_distance(abscisse_min,abscisse_max,pas,ecartGraduation):
    question = "Donner la distance :"
    exo = []
    cor = []
    points=(noms_sommets(4))
    abscisse=abscissePoint(4,abscisse_min,abscisse_max,pas)
    tex_axe_gradue(exo,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation)
    exo.append(u"\\newline Entre les points %s et %s" % (points[0],points[1]))
    tex_axe_gradue(cor,abscisse,points,abscisse_min,abscisse_max,pas,ecartGraduation)
    cor.append("Les abscisses de %s et %s sont %s et %s" % (points[0],points[1],abscisse[0],abscisse[1]))
    min_abscisse=min(abscisse[0],abscisse[1])
    max_abscisse=max(abscisse[0],abscisse[1])
    solution = abs(abscisse[1]-abscisse[0])
    if min_abscisse == 0:
        cor.append("$$ d = %s $$" % (max_abscisse))
    elif min_abscisse < 0:
        cor.append("$$ d = %s - ( %s ) $$" % (max_abscisse,min_abscisse))
        cor.append("$$ d = %s + %s = %s $$" % (max_abscisse,abs(min_abscisse),solution))
    else:
        cor.append("$$ d = %s - %s = %s $$" % (max_abscisse,min_abscisse,solution))
    cor.append(u"La distance de %s à %s est %s" % (points[0],points[1],solution))
    return (exo, cor, question)

def LireEntier(parametre):
    pas = 1
    abscisse_min=random.randrange(-10,-5)
    abscisse_max=random.randrange(5,11)
    ecartGraduation = random.randrange(2,5)
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def LireDecimal(parametre):
    pas = randrange_float(0.1, 0.2, 0.1)
    abscisse_min=randrange_float(-3,-1,1)
    abscisse_max=randrange_float(1,3,pas)
    ecartGraduation = 1
    (exo, cor, question) = tex_lire(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def DistanceEntier(parametre):
    pas = 1
    abscisse_min=random.randrange(-10,-5)
    abscisse_max=random.randrange(5,11)
    ecartGraduation = random.randrange(2,5)
    (exo, cor, question) = tex_distance(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)

def DistanceDecimal(parametre):
    pas = randrange_float(0.1, 0.2, 0.1)
    abscisse_min=randrange_float(-3,-1,1)
    abscisse_max=randrange_float(1,3,pas)
    ecartGraduation = 1
    (exo, cor, question) = tex_distance(abscisse_min,abscisse_max,pas,ecartGraduation)
    return (exo, cor, question)
