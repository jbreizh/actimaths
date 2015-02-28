# Pyromaths
# -*- coding: utf-8 -*-
#
# Pyromaths
# Un programme en Python qui permet de créer des fiches d"exercices types de
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
import math

uniteLongueur = [ "mm", "cm", "dm", "m", "dam", "hm", "km"]
uniteAire = [ "mm^2", "cm^2", "dm^2", "m^2", "dam^2", "hm^2", "km^2"]
uniteVolume = [ "mm^3", "cm^3", "dm^3", "m^3", "dam^3", "hm^3", "km^3"]

def dimension_pyramide(nbre_min,nbre_max):
    i = random.randrange(nbre_min,nbre_max)
    j = random.randrange(nbre_min,nbre_max)
    if i > j:
        longueur = i
        largeur = j
    else:
        longueur = j
        largeur = i 
    hauteur = random.randrange(nbre_min,nbre_max)
    unite = random.randrange(7)
    return longueur,largeur,hauteur,unite

def dimension_cone(nbre_min,nbre_max):
    rayon = random.randrange(nbre_min,nbre_max)
    hauteur = random.randrange(nbre_min,nbre_max)
    unite = random.randrange(7)
    return rayon,hauteur,unite

def tex_debut(enonce):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture*}(-5,-4)(5,4)")

def tex_fin(enonce):
    enonce.append("\\end{pspicture*}")
    enonce.append("\\end{center}")

def tex_pyramide_rectangle(enonce,longueur,largeur,hauteur,unite):
    enonce.append("\\pstGeonode[PointSymbol=x,PointName=none](0,3){S}(-3.5,-3){A}(2,-3){B}(3.5,-1){C}(-2,-1){D}(0,-2){H}")
    enonce.append("\\pstLineAB{A}{B}")
    enonce.append("\\pstLineAB{B}{C}")
    enonce.append("\\pstLineAB{S}{A}")
    enonce.append("\\pstLineAB{S}{B}")
    enonce.append("\\pstLineAB{S}{C}")
    enonce.append("\\pstLineAB[linestyle=dashed]{C}{D}")
    enonce.append("\\pstLineAB[linestyle=dashed]{D}{A}")
    enonce.append("\\pstLineAB[linestyle=dashed]{S}{D}")
    enonce.append("\\pstLineAB[linestyle=dashed]{S}{H}")
    enonce.append("\\pstRightAngle{C}{H}{S}")
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{A}{B} \\mput*{\\unit[%s]{%s}}" %(longueur,uniteLongueur[unite]))
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{B}{C} \\mput*{\\unit[%s]{%s}}" %(largeur,uniteLongueur[unite]))
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{S}{H} \\mput*{\\unit[%s]{%s}}" %(hauteur,uniteLongueur[unite]))

def tex_pyramide_triangle(enonce,base_triangle,hauteur_triangle,hauteur_pyramide,unite):
    enonce.append("\\pstGeonode[PointSymbol=x,PointName=none](0.5,3){S}(-3.5,-3){A}(3,-3){B}(-0.5,-0.5){C}(-1,-3){D}(0.5,-2){H}")
    enonce.append("\\pstLineAB{A}{B}")
    enonce.append("\\pstLineAB{S}{A}")
    enonce.append("\\pstLineAB{S}{B}")
    enonce.append("\\pstLineAB[linestyle=dashed]{B}{C}")
    enonce.append("\\pstLineAB[linestyle=dashed]{C}{A}")
    enonce.append("\\pstLineAB[linestyle=dashed]{C}{D} \\mput*{\\unit[%s]{%s}}" %(hauteur_triangle,uniteLongueur[unite]))
    enonce.append("\\pstLineAB[linestyle=dashed]{S}{C}")
    enonce.append("\\pstLineAB[linestyle=dashed]{S}{H} \\mput*{\\unit[%s]{%s}}" %(hauteur_pyramide,uniteLongueur[unite]))
    enonce.append("\\pstRightAngle{B}{H}{S}")
    enonce.append("\\pstRightAngle{B}{D}{C}")
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{A}{B} \\mput*{\\unit[%s]{%s}}" %(base_triangle,uniteLongueur[unite]))

def tex_cone(enonce,rayon,hauteur,unite):
    enonce.append("\\pstGeonode[PointSymbol=x,PointName=none](0,3){S}(0,-2){H}(3,-2){A}")
    enonce.append("\\pstGeonode[PointSymbol=x,PointName=none](-3,-2){B}")
    enonce.append("\\pstLineAB{S}{A}")
    enonce.append("\\pstLineAB{S}{B}")
    enonce.append("\\pstLineAB[linestyle=dashed]{S}{H}")
    enonce.append("\\pstLineAB[linestyle=dashed]{H}{A}")
    enonce.append("\\pstRightAngle{A}{H}{S}")
    enonce.append("\\psellipse(0,-2)(3,1)")
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{H}{A} \\mput*{\\unit[%s]{%s}}" %(rayon,uniteLongueur[unite]))
    enonce.append("\\pstLineAB[offset=-9pt]{<->}{S}{H} \\mput*{\\unit[%s]{%s}}" %(hauteur,uniteLongueur[unite]))

def PyramideRectangle(parametre):
    #initialisation
    question = "Calculer le volume de la pyramide :"
    exo = []
    cor = []
    # Parametre
    (longueur,largeur,hauteur,unite) = dimension_pyramide(parametre[0],parametre[1])
    # Figure
    tex_debut(exo)
    tex_debut(cor)
    tex_pyramide_rectangle(exo,longueur,largeur,hauteur,unite)
    tex_pyramide_rectangle(cor,longueur,largeur,hauteur,unite)
    tex_fin(exo)
    tex_fin(cor)
    # Corrigé
    cor.append("Volume = ${1 \\over 3} \\times \\text{Base} \\times \\text{hauteur}$ \\newline")
    cor.append("Base = $%s \\times %s =  \\unit[%s]{%s}$\\newline" %(longueur,largeur,longueur*largeur,uniteAire[unite]))
    cor.append("Volume = ${1 \\over 3} \\times %s \\times %s$ \\newline" % (longueur*largeur,hauteur))
    cor.append("Volume $\\approx \\boxed{\\unit[%s]{%s}}$" % (round(float(longueur*largeur*hauteur)/3,2),uniteVolume[unite]))
    return (exo, cor, question)

def PyramideTriangle(parametre):
    #initialisation
    question = "Calculer le volume de la pyramide :"
    exo = []
    cor = []
    # Parametre
    (base_triangle,hauteur_triangle,hauteur_pyramide,unite) = dimension_pyramide(parametre[0],parametre[1])
    # Figure
    tex_debut(exo)
    tex_debut(cor)
    tex_pyramide_triangle(exo,base_triangle,hauteur_triangle,hauteur_pyramide,unite)
    tex_pyramide_triangle(cor,base_triangle,hauteur_triangle,hauteur_pyramide,unite)
    tex_fin(exo)
    tex_fin(cor)
    # Corrigé
    cor.append("Volume = ${1 \\over 3} \\times \\text{Base} \\times \\text{hauteur}$ \\newline")
    cor.append("Base = $%s \\times %s \\div 2 =  \\unit[%s]{%s}$\\newline" %(base_triangle,hauteur_triangle,float(base_triangle*hauteur_triangle)/2,uniteAire[unite]))
    cor.append("Volume = ${1 \\over 3} \\times %s \\times %s$ \\newline" % (float(base_triangle*hauteur_triangle)/2,hauteur_pyramide))
    cor.append("Volume $\\approx \\boxed{\\unit[%s]{%s}}$" % (round(float(base_triangle*hauteur_triangle*hauteur_pyramide)/6,2),uniteVolume[unite]))
    return (exo, cor, question)

def Cone(parametre):
    #initialisation
    question = u"Calculer le volume du cône ($\\pi \\approx 3$) :"
    exo = []
    cor = []
    # Parametre
    (rayon,hauteur,unite) = dimension_cone(parametre[0],parametre[1])
    # Figure
    tex_debut(exo)
    tex_debut(cor)
    tex_cone(exo,rayon,hauteur,unite)
    tex_cone(cor,rayon,hauteur,unite)
    tex_fin(exo)
    tex_fin(cor)
    # Corrigé
    cor.append("Volume = ${1 \\over 3} \\times \\text{Base} \\times \\text{hauteur}$ \\newline")
    cor.append("Base = $\\pi \\times %s^2 \\approx \\unit[%s]{%s}$\\newline" %(rayon,3*rayon*rayon,uniteAire[unite]))
    cor.append("Volume $\\approx {1 \\over 3} \\times %s \\times %s$ \\newline" % (3*rayon*rayon,hauteur))
    cor.append("Volume $\\approx \\boxed{\\unit[%s]{%s}}$" % (3*rayon*rayon*hauteur,uniteVolume[unite]))
    return (exo, cor, question)

