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

import random, math

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

def parametre_comptage():
    dimension_grille = random.randrange(10,15)
    taille_grille = float(4.5)/dimension_grille
    dimension_unite = random.randrange(1,3)
    nombre_unite = random.randrange(1,4)
    unite = random.randrange(7)
    dimension_figure = [random.randrange(2,dimension_grille-5,dimension_unite),  random.randrange(2,dimension_grille-5,dimension_unite)]
    return dimension_grille,taille_grille,dimension_unite,nombre_unite,unite,dimension_figure

def tex_carre(enonce,cote,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle={-135,-45,45,135},PointSymbol=none](-2,-2){A}(2,-2){B}(2,2){C}(-2,2){D}")
    enonce.append("\\pspolygon(A)(B)(C)(D)")
    enonce.append("\\pstRightAngle{B}{A}{D}")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (0,0,-2,cote,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_rectangle(enonce,longueur,largeur,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle={-135,-45,45,135},PointSymbol=none](-3,-2){A}(3,-2){B}(3,2){C}(-3,2){D}")
    enonce.append("\\pspolygon(A)(B)(C)(D)")
    enonce.append("\\pstRightAngle{B}{A}{D}")
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (0,0,-2,longueur,uniteLongueur[unite]))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (90,3,0,largeur,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_disque(enonce,rayon,unite):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=0.5cm}")
    enonce.append("\\begin{pspicture}(-5,-3)(5,3)")
    enonce.append("\\pstGeonode[PosAngle=-90,PointSymbol=x](0,0){O}")
    enonce.append("\\pscircle(O){2.5}")
    enonce.append("\\uput{0.25}[0]{45}(0,0){$\\unit[%s]{%s}$}" % (rayon,uniteLongueur[unite]))
    enonce.append("\\rput{45}(0,0){\\psline{<->}(O)(2.5,0)}")
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def tex_comptage(enonce,dimension_grille,taille_grille,dimension_unite,nombre_unite,unite,dimension_figure):
    enonce.append("\\begin{center}")
    enonce.append("\\psset{unit=%scm}" % taille_grille)
    enonce.append("\\begin{pspicture}(%s,%s)" % (dimension_grille,dimension_grille))
    enonce.append("\\psgrid[gridcolor=gray, griddots=5, subgriddiv=0, gridlabels=0pt](%s,%s)" % (dimension_grille,dimension_grille))
    enonce.append("\\psline[linecolor=red, showpoints=true](1,1)(%s,1)" % (dimension_unite+1))
    enonce.append("\\psframe[linecolor=blue](4,4)(%s,%s)" % (dimension_figure[0]+4, dimension_figure[1]+4))
    enonce.append("\\rput[t]{%s}(%s,%s){$\\unit[%s]{%s}$}" % (0,1+float(dimension_unite)/2,0.8,nombre_unite,uniteLongueur[unite]))
    enonce.append("\\end{pspicture}")
    enonce.append("\\end{center}")

def Carre(parametre):
    question = u"Calculer le périmètre du carré :"
    exo = []
    cor = []
    (longueur,largeur,unite) = dimension()
    tex_carre(exo,longueur,unite)
    tex_carre(cor,longueur,unite)
    cor.append(u"Périmètre = $\\text{côté} \\times 4$ \\newline")
    cor.append(u"Périmètre = $%s \\times 4$ \\newline" % longueur)
    cor.append(u"Périmètre = $\\boxed{\\unit[%s]{%s}}$" % (longueur*4,uniteLongueur[unite]))
    return (exo, cor, question)

def Rectangle(parametre):
    question = u"Calculer le périmètre du rectangle :"
    exo = []
    cor = []
    (longueur,largeur,unite) = dimension()
    tex_rectangle(exo,longueur,largeur,unite)
    tex_rectangle(cor,longueur,largeur,unite)
    cor.append(u"Périmètre = $(L + l) \\times 2$ \\newline")
    cor.append(u"Périmètre = $( %s  + %s ) \\times 2$ \\newline" % (longueur,largeur))
    cor.append(u"Périmètre = $%s \\times 2$ \\newline" % (longueur+ largeur))
    cor.append(u"Périmètre = $\\boxed{\\unit[%s]{%s}}$" % (longueur*2+largeur*2,uniteLongueur[unite]))
    return (exo, cor, question)

def Disque(parametre):
    question = u"Calculer le périmètre du cercle :"
    exo = []
    cor = []
    rayon = random.randrange(2,10)
    unite = random.randrange(7)
    tex_disque(exo,rayon,unite)
    tex_disque(cor,rayon,unite)
    cor.append(u"Périmètre = $2 \\times \\text{rayon} \\times \\pi$ \\newline")
    cor.append(u"Périmètre = $2 \\times %s \\times \\pi$ \\newline" % rayon)
    cor.append(u"Périmètre = $\\boxed{\\unit[%s \\times\\pi]{%s}} $ \\newline" % (rayon*2,uniteLongueur[unite]))
    cor.append(u"Périmètre $\\approx \\unit[%s]{%s}$" % (round(math.pi*rayon*2,2),uniteLongueur[unite]))
    return (exo, cor, question)

def Comptage(parametre):
    question = u"Donne le périmètre du rectangle :"
    exo = []
    cor = []
    (dimension_grille,taille_grille,dimension_unite,nombre_unite,unite,dimension_figure) = parametre_comptage()
    tex_comptage(exo,dimension_grille,taille_grille,dimension_unite,nombre_unite,unite,dimension_figure)
    tex_comptage(cor,dimension_grille,taille_grille,dimension_unite,nombre_unite,unite,dimension_figure)
    nombreSegment = (2*dimension_figure[0]+2*dimension_figure[1])/dimension_unite
    cor.append(u"Il y a %s segments rouges dans le contour bleu \\newline" % nombreSegment)
    cor.append(u"Périmètre = $%s \\times %s$ = $\\boxed{\\unit[%s]{%s}}$" % (nombreSegment,nombre_unite,nombreSegment*nombre_unite,uniteLongueur[unite]))
    return (exo, cor, question)
