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
def tex_rapporteur(enonce):
    enonce.append("\\psarc(0,0){5}{0}{180}")
    enonce.append("\\psarc(0,0){4.5}{0}{180}")
    enonce.append("\\psarc(0,0){3}{0}{180}")
    enonce.append("\\psarc(0,0){0.5}{0}{180}")
    enonce.append("\\SpecialCoor")
    enonce.append("\\multido{\\i=0+1}{181}{\\psline[linewidth=0.01](4.5;\\i)(5;\\i)}")
    enonce.append("\\multido{\\i=0+10}{19}{\\psline(4;\\i)(5;\\i)}")
    enonce.append("\\psframe(-5,-1)(5,0)")
    enonce.append("\\multido{\\i=5+10}{18}{\\psline(4.25;\\i)(5;\\i)}")
    enonce.append("\\tiny")
    enonce.append("\\multido{\\i=0+10}{19}{\\rput(3.75;\\i){\\i }}")
    enonce.append("\\pscircle[fillstyle=solid, fillcolor=white]{0.1} ")
    enonce.append("\\NormalCoor")


def tex_angle(enonce, angle, nom_angle):
    enonce.append("\\SpecialCoor")
    enonce.append("\\psline[linewidth=0.05](0;0)(5.2;%s)" % angle)
    enonce.append("\\rput(5.5;%s){$%s$}" % (angle, nom_angle))
    enonce.append("\\NormalCoor")

def tex_mesure(enonce, angle, nom_angle):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-1)(5,5.5)")
    tex_rapporteur(enonce)
    for i in range(len(angle)):
        tex_angle(enonce,angle[i],nom_angle[i])
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_nature(enonce, angle):
    angle_rotation = random.randrange(5,175,5)
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-5)(5,5)")
    enonce.append("\\SpecialCoor")
    enonce.append("\\pstGeonode[PointName=none,PointSymbol=x](0;0){O}")
    enonce.append("\\pstGeonode[PointName=none,PointSymbol=none](5.2;%s){A}(5.2;%s){B}" %(angle_rotation,angle_rotation+angle))
    enonce.append("\\pstLineAB{O}{A}")
    enonce.append("\\pstLineAB{O}{B}")
    enonce.append("\\pstMarkAngle[MarkAngleRadius=1]{A}{O}{B}")
    enonce.append("\\NormalCoor")
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def MesureSimple(parametre):
    choix = random.randrange(2)
    if choix:
        nom_angle = "\\widehat{xOy}"
    else:
        nom_angle = "\\widehat{yOz}"
    question = "Donner la mesure de l'angle $%s$ :" % nom_angle 
    exo = []
    cor = []
    angle = random.randrange(5,175,5)
    tex_mesure(exo, [0,angle,180],["x","y","z"])
    tex_mesure(cor, [0,angle,180],["x","y","z"])
    if choix:
        cor.append("$$ %s= %s^\\circ$$ " %(nom_angle, angle))
        cor.append("\\begin{center}")
        cor.append("La mesure de $%s$ est $\\boxed{%s^\\circ}$ " %(nom_angle, angle))
        cor.append("\\end{center}")
    else:
        cor.append("\\begin{center}")
        cor.append("$\\begin{aligned}")
        cor.append("%s & = %s^\\circ - %s^\\circ \\\\" %(nom_angle, 180, angle))
        cor.append("%s & = %s^\\circ \\\\" %(nom_angle, 180 - angle))
        cor.append("\\end{aligned}$")
        cor.append("\\end{center}")
        cor.append("\\begin{center}")
        cor.append("La mesure de $%s$ est $\\boxed{%s^\\circ}$" %(nom_angle, 180 - angle))
        cor.append("\\end{center}")
    return (exo, cor, question)

def MesureComplique(parametre):
    choix = random.randrange(3)
    if choix == 0:
        nom_angle = "\\widehat{xOy}"
    elif choix == 1:
        nom_angle = "\\widehat{yOz}"
    else:
        nom_angle = "\\widehat{xOz}"
    
    question = "Donner la mesure de l'angle $%s$ :" % nom_angle 
    exo = []
    cor = []
    angle = random.sample(range(5,175,15),3)
    angle.sort()
    tex_mesure(exo, angle ,["x","y","z"])
    tex_mesure(cor, angle ,["x","y","z"])
    if choix == 0:
        cor.append("\\begin{center}")
        cor.append("$\\begin{aligned}")
        cor.append("%s & = %s^\\circ-%s^\\circ \\\\" %(nom_angle, angle[1], angle[0]))
        cor.append("%s & = %s^\\circ \\\\" %(nom_angle, angle[1]-angle[0]))
        cor.append("\\end{aligned}$")
        cor.append("\\end{center}")
        cor.append("\\begin{center}")
        cor.append("La mesure de $%s$ est $\\boxed{%s^\\circ}$ " %(nom_angle, angle[1]-angle[0]))
        cor.append("\\end{center}")
    elif choix == 1:
        cor.append("\\begin{center}")
        cor.append("$\\begin{aligned}")
        cor.append("%s & = %s^\\circ-%s^\\circ \\\\" %(nom_angle, angle[2], angle[1]))
        cor.append("%s & = %s^\\circ \\\\" %(nom_angle, angle[2]-angle[1]))
        cor.append("\\end{aligned}$")
        cor.append("\\end{center}")
        cor.append("\\begin{center}")
        cor.append("La mesure de $%s$ est $\\boxed{%s^\\circ}$ " %(nom_angle, angle[2]-angle[1]))
        cor.append("\\end{center}")
    else:
        cor.append("\\begin{center}")
        cor.append("$\\begin{aligned}")
        cor.append("%s & = %s^\\circ-%s^\\circ \\\\" %(nom_angle, angle[2], angle[0]))
        cor.append("%s & = %s^\\circ \\\\" %(nom_angle, angle[2]-angle[0]))
        cor.append("\\end{aligned}$")
        cor.append("\\end{center}")
        cor.append("\\begin{center}")
        cor.append("La mesure de $%s$ est $\\boxed{%s^\\circ}$ " %(nom_angle, angle[2]-angle[0]))
        cor.append("\\end{center}")
    return (exo, cor, question)

def NatureQuestion(parametre):
    #choix du type d'angle
    choix = random.randrange(5)
    if choix == 0:
        angle = 90
        nature = "droit"
    elif choix == 1:
        angle = 180
        nature = "plat"
    elif choix == 2:
        angle = 0
        nature = "nul"
    elif choix == 3:
        angle = random.randrange(1,90)
        nature = "aigu"
    else:
        angle = random.randrange(91,180)
        nature = "obtus"
    #initialisation
    question = "Quelle est la nature de l'angle :"
    exo = []
    cor = []
    # Sujet
    exo.append("\\begin{center}")
    exo.append("de mesure $%s^\\circ$" %angle)
    exo.append("\\end{center}")
    # Corrigé
    if choix <= 2:
        cor.append("\\begin{center}")
        cor.append("Un angle de mesure $%s^\\circ$ est un \\fbox{angle %s}" %(angle, nature))
        cor.append("\\end{center}")
    elif choix == 3:
        cor.append("$$ 0^\\circ < %s^\\circ <  90^\\circ $$" %angle)
        cor.append("\\begin{center}")
        cor.append("Un angle dont la mesure est entre $0^\\circ$ et $90^\\circ$ est un \\fbox{angle aigu}")
        cor.append("\\end{center}")
    else:
        cor.append("$$ 90^\\circ < %s^\\circ <  180^\\circ\ $$" %angle)
        cor.append("\\begin{center}")
        cor.append("Un angle dont la mesure est entre $90^\\circ$ et $180^\\circ$ est un \\fbox{angle obtus}")
        cor.append("\\end{center}")
    return (exo, cor, question)

def NatureSchema(parametre):
    #choix du type d'angle
    choix = random.randrange(5)
    if choix == 0:
        angle = 90
        nature = "droit"
    elif choix == 1:
        angle = 180
        nature = "plat"
    elif choix == 2:
        angle = 0
        nature = "nul"
    elif choix == 3:
        angle = random.randrange(1,70)
        nature = "aigu"
    else:
        angle = random.randrange(110,160)
        nature = "obtus"
    #initialisation
    question = "Quelle est la nature de l'angle :"
    exo = []
    cor = []
    # Sujet
    tex_nature(exo, angle)
    # Corrigé
    tex_nature(cor, angle)
    cor.append("\\begin{center}")
    cor.append("C'est un \\fbox{angle %s}" %nature)
    cor.append("\\end{center}")
    return (exo, cor, question)

