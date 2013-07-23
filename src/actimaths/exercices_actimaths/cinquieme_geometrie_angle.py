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

#------------------construction-----------------------------------------
def Supplementaire(parametre):
    # choix des variables
    choix = random.randrange(2)
    nomAngle = ["\\widehat{xOy}", "\\widehat{yOz}", "\\widehat{xOz}"]
    angle = random.randrange(20,160,5)
    mesureAngle = ["%s^\\circ" % angle, "%s^\\circ" % (180 - angle), "180^\\circ"]
    # initialisation
    question = u"$ %s $ et $ %s $ sont supplémentaires" % (nomAngle[0],nomAngle[1])
    exo = []
    cor = []
    # affichage
    exo.append("$ %s = %s $, calculer $ %s $" % (nomAngle[1 - choix],mesureAngle[1 - choix],nomAngle[choix]))
    cor.append("$$ %s + %s = %s $$" % (nomAngle[choix],nomAngle[1 - choix], nomAngle[2]))
    cor.append("$$ %s + %s = %s $$" % (nomAngle[choix],mesureAngle[1 - choix], mesureAngle[2]))
    cor.append("$$ %s = %s - %s $$" % (nomAngle[choix], mesureAngle[2],mesureAngle[1 - choix]))
    cor.append("$$ \\boxed{%s = %s} $$" % (nomAngle[choix],mesureAngle[choix]))
    return (exo, cor, question)

def SupplementaireSchema(parametre):
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
    cor.append("$$ %s + %s = %s $$" % (tex_nom[choix],tex_nom[1 - choix], tex_nom[2]))
    cor.append("$$ %s + %s = %s $$" % (tex_nom[choix],tex_mesure[1 - choix], tex_mesure[2]))
    cor.append("$$ %s = %s - %s $$" % (tex_nom[choix], tex_mesure[2],tex_mesure[1 - choix]))
    cor.append("$$ \\boxed{%s = %s} $$" % (tex_nom[choix],tex_mesure[choix]))
    return (exo, cor, question)

def Complementaire(parametre):
    # choix des variables
    choix = random.randrange(2)
    nomAngle = ["\\widehat{xOy}", "\\widehat{yOz}", "\\widehat{xOz}"]
    angle = random.randrange(20,80,5)
    mesureAngle = ["%s^\\circ" % angle, "%s^\\circ" % (90 - angle), "90^\\circ"]
    # initialisation
    question = u"$ %s $ et $ %s $ sont complémentaires" % (nomAngle[0],nomAngle[1])
    exo = []
    cor = []
    # affichage
    exo.append("$ %s = %s $, calculer $ %s $" % (nomAngle[1 - choix],mesureAngle[1 - choix],nomAngle[choix]))
    cor.append("$$ %s + %s = %s $$" % (nomAngle[choix],nomAngle[1 - choix], nomAngle[2]))
    cor.append("$$ %s + %s = %s $$" % (nomAngle[choix],mesureAngle[1 - choix], mesureAngle[2]))
    cor.append("$$ %s = %s - %s $$" % (nomAngle[choix], mesureAngle[2],mesureAngle[1 - choix]))
    cor.append("$$ \\boxed{%s = %s} $$" % (nomAngle[choix],mesureAngle[choix]))
    return (exo, cor, question)

def ComplementaireSchema(parametre):
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
    cor.append("$$ %s + %s = %s $$" % (tex_nom[choix],tex_nom[1 - choix], tex_nom[2]))
    cor.append("$$ %s + %s = %s $$" % (tex_nom[choix],tex_mesure[1 - choix], tex_mesure[2]))
    cor.append("$$ %s = %s - %s $$" % (tex_nom[choix], tex_mesure[2],tex_mesure[1 - choix]))
    cor.append("$$ \\boxed{%s = %s} $$" % (tex_nom[choix],tex_mesure[choix]))
    return (exo, cor, question)

def CorrespondantSchema(parametre):
    angle = random.randrange(20,80,5)
    mesure = [angle, 180 - angle, angle, 180 - angle, angle, 180 - angle, angle, 180 - angle]
    choix = random.randrange(8)
    mesure_enonce = []
    mesure_corrige = []
    for i in range(len(mesure)):
        if i == choix or i == choix+4 or i == choix - 4:
            mesure_enonce.append("?")
            mesure_corrige.append("%s^\\circ" % mesure[i])
        else:
            mesure_enonce.append("")
            mesure_corrige.append("")
    print mesure, choix, mesure_enonce, mesure_corrige
    # initialisation
    question = u"Calculer la mesure de l'angle :"
    exo = []
    cor = []


    return (exo, cor, question)
