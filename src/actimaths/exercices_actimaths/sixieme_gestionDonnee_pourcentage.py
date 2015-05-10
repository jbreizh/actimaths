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

objet = ['allumettes','billes','boules','timbres','pieces','crayons']
pourcentage = [10, 20, 25, 50]

def choixVariable(nombre_min,nombre_max):
    objet_choisi = objet[random.randrange(0, len(objet))]
    pourcentage_choisi = pourcentage[random.randrange(0, len(pourcentage))]
    part = random.randrange (nombre_min*pourcentage_choisi/100 ,nombre_max*pourcentage_choisi/100)
    total = part * 100 / pourcentage_choisi
    return objet_choisi, part, total, pourcentage_choisi

def CalculPartie(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (objet, part, total, pourcentage)= choixVariable(parametre[0],parametre[1])
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    if random.randrange(0,2):
        exo.append("Je prends $ \\ldots $ %s parmi $ %s $ \\newline" % (objet, total))
        exo.append(u"J\'ai donc pris $ %s  \\%% $ des %s" % (pourcentage, objet))
        cor.append("\\begin{tabular}{c|c}")
        cor.append(" ? & %s \\\\" % pourcentage)
        cor.append("\\hline")
        cor.append("%s & 100 \\\\" % total)
        cor.append("\\end{tabular} \\newline")
        cor.append("$ ? = %s \\times %s \\div 100 $ \\newline" % (pourcentage, total))
        cor.append("Je prends $ \\boxed{%s} $ %s parmi $ %s $ \\newline" % (part, objet, total))
        cor.append(u"J\'ai donc pris $ %s  \\%% $ des %s \\newline" % (pourcentage, objet))
    else:
        exo.append("Je prends $ %s $ %s parmi $ \\ldots $ \\newline" % (part, objet))
        exo.append(u"J\'ai donc pris $ %s  \\%% $ des %s" % (pourcentage, objet))
        cor.append("\\begin{tabular}{c|c}")
        cor.append(" %s & %s \\\\" % (part,pourcentage))
        cor.append("\\hline")
        cor.append("? & 100 \\\\")
        cor.append("\\end{tabular} \\newline")
        cor.append("$ ? = %s \\times 100 \\div %s $ \\newline" % (part, pourcentage))
        cor.append("Je prends $ %s $ %s parmi $ \\boxed{%s} $ \\newline" % (part, objet, total))
        cor.append(u"J\'ai donc pris $ %s  \\%% $ des %s" % (pourcentage, objet))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor,question)

def CalculPourcentage(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (objet, part, total, pourcentage)= choixVariable(parametre[0],parametre[1])
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("Je prends $ %s $ %s parmi $ %s $ \\newline" % (part, objet, total))
    exo.append(u"J\'ai donc pris $ \\ldots \\%% $ des %s" % objet)
    cor.append("\\begin{tabular}{c|c}")
    cor.append("%s & ? \\\\" % part)
    cor.append("\\hline")
    cor.append("%s & 100 \\\\" % total)
    cor.append("\\end{tabular} \\newline")
    cor.append("$ ? = %s \\times 100 \\div %s $ \\newline" % (part, total))
    cor.append("Je prends $ %s $ %s parmi $ %s $ \\newline" % (part, objet, total))
    cor.append(u"J\'ai donc pris $ \\boxed{%s \\%%} $ des %s" % (pourcentage, objet))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor,question)

def AppliquerPourcentage(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (objet, part, total, pourcentage)= choixVariable(parametre[0],parametre[1])
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("$ %s \\%% $ de $ %s $ vaut ..." % (pourcentage,total))
    cor.append("\\begin{tabular}{c|c}")
    cor.append("? & %s \\\\" % pourcentage)
    cor.append("\\hline")
    cor.append("%s & 100 \\\\" % total)
    cor.append("\\end{tabular} \\newline")
    cor.append("$ ? = %s \\times %s \\div 100 $ \\newline" % (total,pourcentage))
    cor.append("$ %s \\%% $ de $ %s $ vaut $ \\boxed{%s} $" % (pourcentage,total,part))
    exo.append("\\end{center}")
    cor.append("\\end{center}")
    return (exo, cor,question)

