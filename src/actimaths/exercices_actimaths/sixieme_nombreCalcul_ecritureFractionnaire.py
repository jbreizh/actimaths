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
from outils import Affichage, Arithmetique

#===============================================================================
#    Écriture fractionnaire
#===============================================================================
def valeurs_frac():
    n1 = random.randrange(11, 10000)
    p1 = random.randrange(1, 4)
    return (n1, p1)

def choix_trou_frac(exo, cor, n1, p1):
    i = random.randrange(3)
    p2 = random.randrange(2)  #sert à compliquer un peu l'exercice
    if i > 1:
        exo.append('$$\\cfrac{%s}{%s}=\\ldots$$' % (Affichage.decimaux(n1 * 10 ** p2), Affichage.decimaux(10 ** (p1 + p2))))
        cor.append('$$\\cfrac{%s}{%s}=\\mathbf{%s}$$' % (Affichage.decimaux(n1 * 10 ** p2), Affichage.decimaux(10 ** (p1 + p2)), Affichage.decimaux(n1 * 10 ** (-p1), 1)))
    elif i > 0:
        exo.append('$$\\cfrac{%s}{\ldots}=%s$$' % (Affichage.decimaux(n1 * 10 ** p2), Affichage.decimaux(n1 * 10 ** (-p1), 1)))
        cor.append('$$\\cfrac{%s}{\\mathbf{%s}}=%s$$' % (Affichage.decimaux(n1 * 10 ** p2), Affichage.decimaux(10 ** (p1 + p2)), Affichage.decimaux(n1 * 10 ** (-p1), 1)))
    else:
        exo.append('$$\\cfrac{\ldots}{%s}=%s$$' % (Affichage.decimaux(10 ** (p1 + p2)), Affichage.decimaux(n1 * 10 ** (-p1), 1)))
        cor.append('$$\\cfrac{\\mathbf{%s}}{%s}=%s$$' % (Affichage.decimaux(n1 * 10 ** p2), Affichage.decimaux(10 ** (p1 + p2)), Affichage.decimaux(n1 * 10 ** (-p1), 1)))

def EcritureFractionnaire(parametre):
    question = u"Compléter :"
    exo = []
    cor = []
    (nombre, puissance) = valeurs_frac()
    choix_trou_frac(exo, cor, nombre, puissance)
    return (exo, cor, question)
