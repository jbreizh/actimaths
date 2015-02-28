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

def parametre():
    objet = ['allumettes','billes','boules','timbres','pieces','crayons']
    i = random.randrange(0, len(objet))
    pourcentage = [10, 20, 25, 50]
    j = random.randrange(0, len(pourcentage))
    part = random.randrange (2, 10)
    total = part * 100 / pourcentage[j]
    return objet[i], part, total, pourcentage[j]

def tex_pourcentage(exo,cor):
    (objet, part, total, pourcentage)= parametre()
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    exo.append("Je prends $ %s $ %s parmi $ %s $. \\newline" % (part, objet, total))
    cor.append("Je prends $ %s $ %s parmi $ %s $. \\newline" % (part, objet, total))
    exo.append(u"J\'ai donc pris $ \\ldots \\%% $ des %s" % objet)
    cor.append(u"J\'ai donc pris $ \\boxed{%s \\%%} $ des %s" % (pourcentage, objet))
    exo.append("\\end{center}")
    cor.append("\\end{center}")

def tex_partie(exo,cor):
    (objet, part, total, pourcentage)= parametre()
    exo.append("\\begin{center}")
    cor.append("\\begin{center}")
    if random.randrange(0,2):
        exo.append("Je prends $ \\ldots $ %s parmi $ %s $. \\newline" % (objet, total))
        cor.append("Je prends $ \\boxed{%s} $ %s parmi $ %s $ \\newline" % (part, objet, total))   
    else:
        exo.append("Je prends $ %s $ %s parmi $ \\ldots $. \\newline" % (part, objet))
        cor.append("Je prends $ %s $ %s parmi $ \\boxed{%s} $ \\newline" % (part, objet, total))    
    exo.append(u"J\'ai donc pris $ %s  \\%% $ des %s." % (pourcentage, objet))
    cor.append(u"J\'ai donc pris $ %s  \\%% $ des %s." % (pourcentage, objet))
    exo.append("\\end{center}")
    cor.append("\\end{center}")

def CalculPartie(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    tex_partie(exo,cor)
    return (exo, cor,question)

def CalculPourcentage(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    tex_pourcentage(exo,cor)
    return (exo, cor,question)
