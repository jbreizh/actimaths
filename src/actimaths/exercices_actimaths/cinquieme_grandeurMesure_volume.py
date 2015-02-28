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

def dimension_cylindre():
    rayon = random.randrange(2,6)
    hauteur = random.randrange(2,11)
    unite = random.randrange(7)
    return rayon,hauteur,unite

def dimension_prisme():
    i = random.randrange(2,10)
    j = random.randrange(2,10)
    if i > j:
        baseTriangle = i
        hauteurTriangle = j
    else:
        baseTriangle = j
        hauteurTriangle = i 
    hauteur = random.randrange(2,6)
    unite = random.randrange(7)
    return baseTriangle,hauteurTriangle,hauteur,unite

def tex_cylindre(enonce,rayon,hauteur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle={-135,-135},PointSymbol=x](0,-2){O}(0,2){O'}")
    enonce.append("\\psellipse(0,2)(4,1)")
    enonce.append("\\psellipse(0,-2)(4,1)")
    enonce.append("\\psline(-4,-2)(-4,2)")
    enonce.append("\\psline(4,-2)(4,2)")
    enonce.append("\\psline[linestyle=dashed](O)(O')")
    enonce.append("\\psline{<->}(4.5,-2)(4.5,2)")
    enonce.append("\\psline{<->}(O)(4,-2)")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (0,2,-2,rayon,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (90,4.5,0,hauteur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_prisme_triangle_rectangle(enonce,baseTriangle,hauteurTriangle,hauteur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-4)(5,4)")
    enonce.append("\\pstGeonode[PosAngle={135,45,45,-135,-45,45},PointSymbol=none](-3,1){A}(3,1){B}(-1,3){C}(-3,-3){D}(3,-3){E}(-1,-1){F}")
    enonce.append("\\pspolygon(A)(B)(C)")
    enonce.append("\\pspolygon(A)(B)(E)(D)")
    enonce.append("\\psline[linestyle=dashed](D)(F)")
    enonce.append("\\psline[linestyle=dashed](F)(E)")
    enonce.append("\\psline[linestyle=dashed](F)(C)")
    enonce.append("\\pstRightAngle{D}{F}{E}")
    enonce.append("\\psline{<->}(-3,-2.75)(-1,-0.75)")
    enonce.append("\\psline{<->}(-1,-0.75)(3,-2.75)")
    enonce.append("\\psline{<->}(3.25,1)(3.25,-3)")
    enonce.append("\\rput[b]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (-26.56,1,-1.75,hauteurTriangle,uniteLongueur[unite]))
    enonce.append("\\rput[b]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (45,-2,-1.75,baseTriangle,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (90,3.25,-1,hauteur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_prisme_triangle(enonce,baseTriangle,hauteurTriangle,hauteur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-4)(5,4)")
    enonce.append("\\pstGeonode[PosAngle={135,45,45,-135,-45,45},PointSymbol=none](-3,1){A}(3,1){B}(-1,3){C}(-3,-3){D}(3,-3){E}(-1,-1){F}")
    enonce.append("\\pspolygon(A)(B)(C)")
    enonce.append("\\pspolygon(A)(B)(E)(D)")
    enonce.append("\\psline[linestyle=dashed](D)(F)")
    enonce.append("\\psline[linestyle=dashed](F)(E)")
    enonce.append("\\psline[linestyle=dashed](F)(C)")
    enonce.append("\\psline{<->}(-1,-1)(-1,-3)")
    enonce.append("\\psline{<->}(-3,-3.25)(3,-3.25)")
    enonce.append("\\psline{<->}(3.25,1)(3.25,-3)")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (90,-1,-2,hauteurTriangle,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (0,0,-3.25,baseTriangle,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit{%s}{%s}$}" % (90,3.25,-1,hauteur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def Cylindre(parametre):
    question = "Calculer le volume du cylindre ($\\pi \\approx 3$) :"
    exo = []
    cor = []
    (rayon,hauteur,unite) = dimension_cylindre()
    tex_cylindre(exo,rayon,hauteur,unite)
    tex_cylindre(cor,rayon,hauteur,unite)
    cor.append("Volume = $B \\times h$ \\newline")
    cor.append("B = $\\pi \\times r \\times r \\approx 3 \\times %s \\times %s \\approx \\unit{%s}{%s}$ \\newline" %(rayon,rayon,3*rayon*rayon,uniteAire[unite]))
    cor.append("Volume $\\approx %s \\times %s \\approx\\boxed{\\unit{%s}{%s}}$" % (3*rayon*rayon,hauteur,3*rayon*rayon*hauteur,uniteVolume[unite]))
    return (exo, cor, question)

def PrismeTriangleRectangle(parametre):
    question = "Calculer le volume du prisme :"
    exo = []
    cor = []
    (baseTriangle,hauteurTriangle,hauteur,unite) = dimension_prisme()
    tex_prisme_triangle_rectangle(exo,baseTriangle,hauteurTriangle,hauteur,unite)
    tex_prisme_triangle_rectangle(cor,baseTriangle,hauteurTriangle,hauteur,unite)
    cor.append("Volume = $B \\times h$ \\newline")
    cor.append("B = $( b \\times h ) \\div 2$ = $(%s \\times %s) \\div 2 = \\unit{%s}{%s}$ \\newline" %(baseTriangle,hauteurTriangle,float(baseTriangle*hauteurTriangle)/2,uniteAire[unite]))
    cor.append("Volume = $%s \\times %s$  = $\\boxed{\\unit{%s}{%s}}$" % (float(baseTriangle*hauteurTriangle)/2,hauteur,float(baseTriangle*hauteurTriangle*hauteur)/2,uniteVolume[unite]))
    return (exo, cor, question)

def PrismeTriangle(parametre):
    question = "Calculer le volume du prisme :"
    exo = []
    cor = []
    (baseTriangle,hauteurTriangle,hauteur,unite) = dimension_prisme()
    tex_prisme_triangle(exo,baseTriangle,hauteurTriangle,hauteur,unite)
    tex_prisme_triangle(cor,baseTriangle,hauteurTriangle,hauteur,unite)
    cor.append("Volume = $B \\times h$ \\newline")
    cor.append("B = $( b \\times h ) \\div 2$ = $(%s \\times %s) \\div 2 = \\unit{%s}{%s}$ \\newline" %(baseTriangle,hauteurTriangle,float(baseTriangle*hauteurTriangle)/2,uniteAire[unite]))
    cor.append("Volume = $%s \\times %s$  = $\\boxed{\\unit{%s}{%s}}$" % (float(baseTriangle*hauteurTriangle)/2,hauteur,float(baseTriangle*hauteurTriangle*hauteur)/2,uniteVolume[unite]))
    return (exo, cor, question)
