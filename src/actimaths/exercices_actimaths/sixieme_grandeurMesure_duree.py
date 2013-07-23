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

uniteTemps = [ "s", "min", "h"]

def tex_heure(tex, heure, minute):
    tex.append("\\begin{center}")
    tex.append("\\psset{unit=0.5cm}")
    tex.append("\\begin{pspicture}(-5,-5)(5,5)")
    tex.append("\\pscircle[fillstyle=solid, fillcolor=white]{5}")
    tex.append("\\pscircle[fillstyle=solid, fillcolor=white]{4.5}")
    tex.append("\\pscircle[fillstyle=solid, fillcolor=white]{0.1}")
    tex.append("\\SpecialCoor")
    tex.append("\\multido{\\i=0+30}{12}{\\psline(4.5;\\i)(5;\\i)}")
    tex.append("\\multido{\\i=0+90}{4}{\\psline(4;\\i)(5;\\i)}")
    tex.append("\\psline[linewidth=0.2](0;0)(2;%s)" % (90 - heure*30 - minute*0.5))
    tex.append("\\psline[linewidth=0.1](0;0)(4;%s)" % (90 - minute*6))
    tex.append("\\NormalCoor")
    tex.append("\\end{pspicture}")
    tex.append("\\end{center}")

def LectureHorloge(parametre):
    heure = random.randrange(12)
    minute = random.randrange(0,60,5)
    # initialisation
    question = u"Quelle heure est-il ? :"
    exo = []
    cor = []
    # affichage de l'horloge
    tex_heure(exo, heure, minute)
    tex_heure(cor, heure, minute)
    # corrige
    cor.append("\\begin{center}")
    if minute > 9:
        cor.append("Il est $\\boxed{%sh%s}$ ou $\\boxed{%sh%s}$" %(heure, minute, heure+12, minute))
    else:
        cor.append("Il est $\\boxed{%sh0%s}$ ou $\\boxed{%sh0%s}$" %(heure, minute, heure+12, minute))
    cor.append("\\end{center}")
    return (exo, cor, question)
