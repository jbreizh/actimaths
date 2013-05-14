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

import math
import random
import string
from outils import Arithmetique, Affichage
      
def tex_formule_dix(l, exo, cor):
    if l[2] == '*':
        alea = random.randrange(0, 5)
        if alea > 1:
            exo.append('$$%s \\quad\\times\\quad %s \\quad = \\quad \\ldots$$' %(Affichage.decimaux(l[0], 1), Affichage.decimaux(l[1],1)))
            cor.append('$$%s \\times %s = \\mathbf{%s}$$' %(Affichage.decimaux(l[0],1),Affichage.decimaux(l[1],1), Affichage.decimaux(l[0] * l[1], 1)))
        elif alea > 0:
            exo.append('$$%s \\quad\\times\\quad \\ldots \\quad = \\quad %s$$' %(Affichage.decimaux(l[0], 1), Affichage.decimaux(l[0] *l[1], 1)))
            cor.append('$$%s \\times \\mathbf{%s} = %s$$' % (Affichage.decimaux(l[0], 1), Affichage.decimaux(l[1],1), Affichage.decimaux(l[0] * l[1], 1)))
        else:
            exo.append('$$\\ldots \\quad\\times\\quad %s \\quad = \\quad %s$$' %(Affichage.decimaux(l[1], 1), Affichage.decimaux(l[0] *l[1], 1)))
            cor.append('$$\\mathbf{%s} \\times %s = %s$$' %(Affichage.decimaux(l[0], 1), Affichage.decimaux(l[1],1), Affichage.decimaux(l[0] * l[1], 1)))
    else:
        alea = random.randrange(0, 5)
        if alea > 1:
            exo.append('$$%s \\quad\\div\\quad %s \\quad = \\quad \\ldots$$' % (Affichage.decimaux(l[0], 1), Affichage.decimaux(l[1],1)))
            cor.append('$$%s \\div %s = \\mathbf{%s}$$' % (Affichage.decimaux(l[0], 1), Affichage.decimaux(l[1], 1), Affichage.decimaux(l[0] / l[1], 1)))
        elif alea > 0:
            exo.append('$$%s \\quad\\div\\quad \\ldots \\quad = \\quad %s$$' % (Affichage.decimaux(l[0], 1), Affichage.decimaux(l[0] / l[1], 1)))
            cor.append('$$%s \\div \\mathbf{%s} = %s$$' % (Affichage.decimaux(l[0],1), Affichage.decimaux(l[1], 1), Affichage.decimaux(l[0] / l[1], 1)))
        else:
            exo.append('$$\\ldots \\quad\\div\\quad %s \\quad = \\quad %s$$' % (Affichage.decimaux(l[1], 1), Affichage.decimaux(l[0] / l[1], 1)))
            cor.append('$$\\mathbf{%s} \\div %s = %s$$' % (Affichage.decimaux(l[0],1), Affichage.decimaux(l[1], 1), Affichage.decimaux(l[0] / l[1], 1)))

def valeurs10(operation):  # renvoie nb valeur de chaque type : *10, /10, *0.1, /0.1
    l = []
    for i in range(2):
        if operation == 0:
            if random.randrange(0, 1):
                l.append((Arithmetique.valeur_alea(111, 999) * 10 ** random.randrange(-3,0), 10 ** (i + 1), '*'))
            else:
                l.append((10 ** (i + 1), Arithmetique.valeur_alea(111, 999) * 10 **random.randrange(-3, 0), '*'))
        if operation == 1:
            l.append((Arithmetique.valeur_alea(111, 999) * 10 ** random.randrange(-3,0), 10 ** (i + 1), '/'))
        if operation == 2:
            if random.randrange(0, 1):
                l.append((Arithmetique.valeur_alea(111, 999) * 10 ** random.randrange(-3,0), 10 ** (-i - 1), '*'))
            else:
                l.append((10 ** (-i - 1), Arithmetique.valeur_alea(111, 999) * 10 **random.randrange(-3, 0), '*'))
        if operation == 3:
            l.append((Arithmetique.valeur_alea(111, 999) * 10 ** random.randrange(-3,0), 10 ** (-i - 1), '/'))
    return l

def tex_dix(exo, cor, operation):
    l = valeurs10(operation)

    j = random.randrange(0, len(l))
    tex_formule_dix(l.pop(j), exo, cor)

def ProduitPuissanceDixPositive(parametre):
    question  = u"Compléter :"
    exo = [ ]
    cor = [ ]
    tex_dix(exo, cor, 0)
    return (exo, cor, question)

def QuotientPuissanceDixPositive(parametre):
    question  = u"Compléter :"
    exo = [ ]
    cor = [ ] 
    tex_dix(exo, cor, 1)
    return (exo, cor, question)

def ProduitPuissanceDixNegative(parametre):
    question  = u"Compléter :"
    exo = [ ]
    cor = [ ]
    tex_dix(exo, cor, 2)
    return (exo, cor, question)

def QuotientPuissanceDixNegative(parametre):
    question  = u"Compléter :"
    exo = [ ]
    cor = [ ]
    tex_dix(exo, cor, 3)
    return (exo, cor, question)
