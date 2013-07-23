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

uniteLongueur = [ "mm", "cm", "dm", "m", "dam", "hm", "km"]
uniteAire = [ "mm^2", "cm^2", "dm^2", "m^2", "dam^2", "hm^2", "km^2"]

def dimension():
    i = random.randrange(2,10)
    j = random.randrange(2,10)
    if i > j:
        longueur = i
        largeur = j
    else:
        longueur = j
        largeur = i 
    unite = random.randrange(7)
    return longueur,largeur,unite

def tex_parallelogramme(enonce,longueur,largeur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle={-135,-45,45,135},PointSymbol=none](-4,-2){A}(3,-2){B}(4,2){C}(-3,2){D}")
    enonce.append("\\pspolygon(A)(B)(C)(D)")
    enonce.append("\\pstGeonode[PosAngle={-90},PointSymbol=none](-3,-2){H}")
    enonce.append("\\psline(D)(H)")
    enonce.append("\\pstRightAngle{D}{H}{B}")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (0,-0.5,-2,longueur,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (90,-3,0,largeur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_triangle(enonce,base,hauteur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle={-135,-45,45,135},PointSymbol=none](-3,-2){A}(3,-2){B}(1,2){C}")
    enonce.append("\\pspolygon(A)(B)(C)")
    enonce.append("\\pstGeonode[PosAngle={-90},PointSymbol=none](1,-2){H}")
    enonce.append("\\psline(C)(H)")
    enonce.append("\\pstRightAngle{C}{H}{B}")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (0,0,-2,base,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (90,1,0,hauteur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def Parallelogramme(parametre):
    question = u"Calculer l\'aire du parallèlogramme :"
    exo = []
    cor = []
    (longueur,largeur,unite) = dimension()
    tex_parallelogramme(exo,longueur,largeur,unite)
    tex_parallelogramme(cor,longueur,largeur,unite)
    cor.append("Aire = $\\text{base} \\times \\text{hauteur}$ \\newline")
    cor.append("Aire = $%s \\times %s$ \\newline" % (longueur,largeur))
    cor.append("Aire = $\\boxed{\\unit[%s]{%s}}$" % (longueur*largeur,uniteAire[unite]))
    return (exo, cor, question)

def Triangle(parametre):
    question = u"Calculer l\'aire du triangle :"
    exo = []
    cor = []
    (base,hauteur,unite) = dimension()
    tex_triangle(exo,base,hauteur,unite)
    tex_triangle(cor,base,hauteur,unite)
    cor.append("Aire = $( \\text{Base} \\times \\text{hauteur} ) \\div 2$ \\newline")
    cor.append("Aire = $( %s \\times %s ) \\div 2$ \\newline" % (base,hauteur))
    cor.append("Aire = $%s \\div 2$ \\newline" % (base*hauteur))
    cor.append("Aire = $\\boxed{\\unit[%s]{%s}}$" % (float(base*hauteur)/2,uniteAire[unite]))
    return (exo, cor, question)
