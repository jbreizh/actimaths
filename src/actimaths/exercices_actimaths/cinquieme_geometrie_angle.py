#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Actimaths
# Un programme en Python qui permet de créer des presentation de
# mathématiques niveau collège ainsi que leur corrigé en LaTeX.
# Copyright (C) 2013 -- Jean-Baptiste Le Coz (jb.lecoz@gmail.com)
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
def tex_schema(enonce, mesure, tex_mesure, choix):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-1)(5,5.5)")
    # Affichage des 3 côtés
    enonce.append("\\SpecialCoor")
    enonce.append("\\psline[linewidth=0.05](0;0)(5.2;0)")
    enonce.append("\\rput(5.5;0){$x$}")
    enonce.append("\\psline[linewidth=0.05](0;0)(5.2;%s)" % mesure[0])
    enonce.append("\\rput(5.5;%s){$y$}" % mesure[0])
    enonce.append("\\psline[linewidth=0.05](0;0)(5.2;%s)" % mesure[2])
    enonce.append("\\rput(5.5;%s){$z$}" % mesure[2])
    enonce.append("\\rput(0.5;-90){$O$}")
    # symbole de l'angle
    enonce.append("\\psarc(0,0){1}{%s}{%s}" % (0,mesure[2]))
    enonce.append("\\psarc(0,0){1.2}{%s}{%s}" % (0,mesure[0]))
    # affichage de la valeur de l'angle connue et d'un ? sinon
    if choix:
        enonce.append("\\rput(2;%s){$%s$}" % (mesure[0]/2, tex_mesure[0]))
        enonce.append("\\rput(2;%s){$?$}" % ((mesure[2]+ mesure[0])/2))
    else:
        enonce.append("\\rput(2;%s){$?$}" % (mesure[0]/2))
        enonce.append("\\rput(2;%s){$%s$}" % ((mesure[2]+ mesure[0])/2, tex_mesure[1])) 
    enonce.append("\\NormalCoor") 
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_paire_angle(enonce):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    # tracé des droites
    enonce.append("\\psline[linewidth=0.05](-5,1)(5,1)")
    enonce.append("\\psline[linewidth=0.05](-5,-1)(5,-1)")
    enonce.append("\\psline[linewidth=0.05](-3,-3)(3,3)")
    # angles du haut
    enonce.append("\\psarc(1,1){0.4}{45}{180}")
    enonce.append("\\psarc(1,1){0.5}{0}{45}")
    enonce.append("\\psarc(1,1){0.4}{225}{360}")
    enonce.append("\\psarc(1,1){0.5}{180}{225}")
    enonce.append("\\uput{0.5}[112.5](1,1){0}")
    enonce.append("\\uput{0.6}[22.5](1,1){1}")
    enonce.append("\\uput{0.5}[-62.5](1,1){2}")
    enonce.append("\\uput{0.6}[-157.5](1,1){3}")
    # angles du bas
    enonce.append("\\psarc(-1,-1){0.4}{45}{180}")
    enonce.append("\\psarc(-1,-1){0.5}{0}{45}")
    enonce.append("\\psarc(-1,-1){0.4}{225}{360}")
    enonce.append("\\psarc(-1,-1){0.5}{180}{225}")
    enonce.append("\\uput{0.5}[112.5](-1,-1){4}")
    enonce.append("\\uput{0.6}[22.5](-1,-1){5}")
    enonce.append("\\uput{0.5}[-62.5](-1,-1){6}")
    enonce.append("\\uput{0.6}[-157.5](-1,-1){7}")
    #
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

#------------------construction-----------------------------------------
def Supplementaire(parametre):
    # choix des variables
    choix = random.randrange(2)
    angle = random.randrange(20,160,5)
    tex_nom = ["\\widehat{xOy}", "\\widehat{yOz}", "\\widehat{xOz}"]
    mesure = [angle, 180 - angle, 180]
    tex_mesure = [ "%s^\\circ" % mesure[0], "%s^\\circ" % mesure[1], "%s^\\circ" % mesure[2] ]
    # initialisation
    question = u"Calculer la mesure de $ %s $ " % tex_nom[choix]
    exo = []
    cor = []
    tex_schema(exo, mesure, tex_mesure, choix)
    tex_schema(cor, mesure, tex_mesure, choix)
    # affichage
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("%s + %s & = %s \\\\" % (tex_nom[choix],tex_nom[1 - choix], tex_nom[2]))
    cor.append("%s + %s & = %s \\\\" % (tex_nom[choix],tex_mesure[1 - choix], tex_mesure[2]))
    cor.append("%s & = %s - %s \\\\" % (tex_nom[choix], tex_mesure[2],tex_mesure[1 - choix]))
    cor.append("%s & = \\boxed{%s} \\\\" % (tex_nom[choix],tex_mesure[choix]))
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def Complementaire(parametre):
    # choix des variables
    choix = random.randrange(2)
    angle = random.randrange(20,80,5)
    tex_nom = ["\\widehat{xOy}", "\\widehat{yOz}", "\\widehat{xOz}"]
    mesure = [angle, 90 - angle, 90]
    tex_mesure = [ "%s^\\circ" % mesure[0], "%s^\\circ" % mesure[1], "%s^\\circ" % mesure[2] ]
    # initialisation
    question = u"Calculer la mesure de $ %s $ " % tex_nom[choix]
    exo = []
    cor = []
    tex_schema(exo, mesure, tex_mesure, choix)
    tex_schema(cor, mesure, tex_mesure, choix)
    # affichage
    cor.append("\\begin{center}")
    cor.append("$\\begin{aligned}")
    cor.append("%s + %s & = %s \\\\" % (tex_nom[choix],tex_nom[1 - choix], tex_nom[2]))
    cor.append("%s + %s & = %s \\\\" % (tex_nom[choix],tex_mesure[1 - choix], tex_mesure[2]))
    cor.append("%s & = %s - %s \\\\" % (tex_nom[choix], tex_mesure[2],tex_mesure[1 - choix]))
    cor.append("%s & = \\boxed{%s} \\\\" % (tex_nom[choix],tex_mesure[choix]))
    cor.append("\\end{aligned}$")
    cor.append("\\end{center}")
    return (exo, cor, question)

def PaireAngle(parametre):
    # choix des angles
    angle1 = random.randrange(8)
    angle2 = random.randrange(8)
    while angle2 == angle1:
        angle2 = random.randrange(8)
    # reponse
    opposeSommet = [(0,2),(1,3),(4,6),(5,7)]
    supplementaire = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,1)]
    correspondant = [(0,4),(3,7),(1,5),(2,6)]
    alterneInterne = [(3,5),(2,4)]
    if ((angle1,angle2) in opposeSommet) or ((angle2,angle1) in opposeSommet):
        reponse = u"opposés par le sommet"
    elif((angle1,angle2) in supplementaire) or ((angle2,angle1) in supplementaire):
        reponse = u"supplémentaires"
    elif((angle1,angle2) in correspondant) or ((angle2,angle1) in correspondant):
        reponse = u"correspondants"
    elif((angle1,angle2) in alterneInterne) or ((angle2,angle1) in alterneInterne):
        reponse = u"alternes-internes"
    else:
        reponse = u"rien du tout"
    # initialisation
    question = u"Observe et répond :"
    exo = []
    cor = []
    # affichage
    tex_paire_angle(exo)
    tex_paire_angle(cor)
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("%s et %s sont ..." %(angle1,angle2))
    cor.append("%s et %s sont \\fbox{%s}" %(angle1,angle2,reponse))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor, question)
