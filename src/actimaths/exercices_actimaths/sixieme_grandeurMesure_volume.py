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
uniteVolume = [ "mm^3", "cm^3", "dm^3", "m^3", "dam^3", "hm^3", "km^3"]

def dimension():
    i = random.randrange(2,10)
    j = random.randrange(2,10)
    if i > j:
        longueur = i
        largeur = j
    else:
        longueur = j
        largeur = i 
    hauteur = random.randrange(2,6)
    unite = random.randrange(7)
    return longueur,largeur,hauteur,unite

def tex_pave_droit(enonce,longueur,largeur,hauteur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle={135,-135,45,135,-135,-45,-45,45},PointSymbol=none](-3,1){A}(2,1){B}(3,2){C}(-2,2){D}(-3,-2){E}(2,-2){F}(3,-1){G}(-2,-1){H}")
    enonce.append("\\pspolygon(A)(E)(F)(B)")
    enonce.append("\\pspolygon(A)(B)(C)(D)")
    enonce.append("\\pspolygon(B)(F)(G)(C)")
    enonce.append("\\psline[linestyle=dashed](E)(H)")
    enonce.append("\\psline[linestyle=dashed](H)(G)")
    enonce.append("\\psline[linestyle=dashed](H)(D)")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (0,-0.5,-2,longueur,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (45,2.5,-1.5,largeur,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (90,3,0.5,hauteur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def PaveDroit(parametre):
    question = u"Calculer le volume du pavé droit :"
    exo = []
    cor = []
    (longueur,largeur,hauteur,unite) = dimension()
    tex_pave_droit(exo,longueur,largeur,hauteur,unite)
    tex_pave_droit(cor,longueur,largeur,hauteur,unite)
    cor.append("Volume = $L \\times l \\times h$ \\newline")
    cor.append("Volume = $%s \\times %s \\times %s$ \\newline" % (longueur,largeur,hauteur))
    cor.append("Volume = $\\boxed{\\unit[%s]{%s}}$" % (longueur*largeur*hauteur,uniteVolume[unite]))
    return (exo, cor, question)
