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
import math


def nodesep(ligne):
    """
    Défini les valeurs nodesep : 0 pour une extrémité, -0.5 pour une continuité
    @param ligne: droite, demi-droite, segment
    @type ligne: string
    """

    if ligne == 'une droite':
        retour = ['-6', '-6']
    elif ligne == 'une demi-droite':
        retour = ['0', '-6']
    else:
        retour = ['0', '0']
    return retour


def nom_points(n):
    """
    choisit n points parmi A, B, C, ..., Z
    @param n: nombre de points à choisir
    @type n: integer
    """

    points = [chr(i + 65) for i in range(26)]
    liste = []
    for i in range(n):
        liste.append(points.pop(random.randrange(len(points))))
    return liste

def coord_points(lpoints):
    """Définit les ordonnées de trois points nommés dont les noms sont dans lpoints"""
    ordonnees = [random.randrange(5, 16)/10.for i in range(3)]
    while abs(2*ordonnees[1]-ordonnees[0]-ordonnees[2])<.5:
        ordonnees = [random.randrange(5, 16)/10.for i in range(3)]
    random.shuffle(ordonnees)
    for i in range(3):
        ordonnees.insert(2*i+1,  lpoints[i])
    return tuple(ordonnees)

def symboles(ligne):
    """
    Retourne les couples (), [] ou [) correspondant au type de ligne
    @param ligne: droite, demi-droite ou segment
    @type ligne: string
    """

    if ligne == 'une droite':
        retour = ['(', ')']
    elif ligne == 'une demi-droite':
        retour = ['[', ')']
    else:
        retour = ['[', ']']
    return retour


def prepare_tuple(lpoints, ligne):
    """
    Prepare deux tuples pour permettre l'affichage de la question et
    de la solution
    @param lpoints: les points de la figure
    @type lpoints: liste de lettres
    @param ligne: droite, demi-droite ou segment
    @type ligne: string
    """

    (retour_exo, retour_sol) = ([], [])

    #choix des deux points permettant de tracer la ligne :
    templist = [i for i in range(len(lpoints))]
    deuxpoints = []
    for i in range(2):
        deuxpoints.append(lpoints[templist.pop(random.randrange(len(templist)))])

    #choix des symbole correspondant à la ligne :
    lsymboles = symboles(ligne)
    retour_sol.append(lsymboles[0])
    retour_sol.extend(deuxpoints)
    retour_sol.append(lsymboles[1])
    retour_sol.append(ligne)

    #choix des trous pour l'exercice :
    retour_exo = ['\\ldots', '\\ldots', '\\ldots', '\\ldots', '$\\ldots$']
    return (tuple(retour_exo), tuple(retour_sol))


def tex_figure(liste, lpoints, points_coord, nodesep=0):
    """
    Écrit dans un fichier tex la construction de 3 points et éventuellement
    une droite, une demi-droite ou un segment.
    @param liste: liste d'exos ou corrigés
    @type liste: liste
    @param lpoints: liste de 3 points
    @type lpoints: liste de 3 strings
    @param nodesep: liste des dépassements pour pstricks
    @type nodesep: liste de 2 strings
    """
    liste.append('\\begin{pspicture*}(-0.5,0.2)(4.5,2.2)')
    liste.append('\\psset{PointSymbol=x}')
    liste.append('\\pstGeonode[PosAngle=90](0.5,%s){%s}(2,%s){%s}(3.5,%s){%s}' %
               points_coord)
    if nodesep:
        liste.append('\\pstLineAB[nodesepA=%s, nodesepB=%s]{%s}{%s}' %
                   tuple(nodesep))
    liste.append('\\end{pspicture*}')


def DroiteDemidroiteSegment(parametre):
    question = u"Compléter :"
    exo = []
    cor = []

    lignes = ['une droite', 'une demi-droite', 'un segment']
    ligne = lignes[random.randrange(3)]
    nom = nom_points(3)
    coordonnee = coord_points(nom)
    (exer, solution) = prepare_tuple(nom, ligne)
    lnodesep = nodesep(ligne)
    lnodesep.extend(solution[1:3])

    tex_figure(exo, nom, coordonnee, lnodesep)
    tex_figure(cor, nom, coordonnee, lnodesep)
    exo.append('\\begin{center}')
    cor.append('\\begin{center}')
    exo.append('$%s %s%s %s$ est %s' % exer)
    cor.append('$%s %s%s %s$ est %s' % solution)
    exo.append('\\end{center}')
    cor.append('\\end{center}')
    return (exo, cor, question)
