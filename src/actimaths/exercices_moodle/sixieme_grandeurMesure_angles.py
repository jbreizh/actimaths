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

from math import sin,cos,pi,sqrt
from random import randrange
from outils import Geometrie


def eq_droites(A, B):
    (xA, yA) = A
    (xB, yB) = B
    a = ((yB - yA) * 1.0) / (xB - xA)
    b = ((xB * yA - xA * yB) * 1.0) / (xB - xA)
    return (a, b)


def inter_droites(A, B, C, D):
    """
    Calcule les coordonn\xc3\xa9es du point d'intersection des droites (AB) et (CD)
    """

    (a1, b1) = eq_droites(A, B)
    (a2, b2) = eq_droites(C, D)
    if a1 == a2:  #droites parallèles
        xI = A[0]
        yI = A[1]
    else:
        xI = ((b2 - b1) * 1.0) / (a1 - a2)
        yI = ((a1 * b2 - a2 * b1) * 1.0) / (a1 - a2)
    return (xI, yI)


def dist_pt_droite(A, B, C):
    """
    calcule la distance du point C \xc3\xa0 la droite (AB)
    """

    (a, b) = eq_droites(A, B)
    (xC, yC) = C
    d = (abs(a * xC - yC + b) * 1.0) / sqrt(a ** 2 + 1)
    return d


def dist_points(A, B):
    """ Calcul la distance entre deux points"""

    (xA, yA) = A
    (xB, yB) = B
    d = sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
    return d


def coord_projete(A, B, C):
    """
    Calcule les coordonn\xc3\xa9es du projet\xc3\xa9 orthogonal de C sur la droite (AB)
    """

    (xA, yA) = A
    (xB, yB) = B
    (xC, yC) = C
    n = dist_points(A, B)
    p = (xB - xA) / n
    q = (yB - yA) / n
    s = p * (xC - xA) + q * (yC - yA)
    return (xA + s * p, yA + s * q)


def verifie_distance_mini(A, B, C, D):
    """
    V\xc3\xa9rifie que la distance minimale entre [AB] et [AC] est sup\xc3\xa9rieure \xc3\xa0 dmin
    """

    dmin = 1.2
    (xA, yA) = A
    (xB, yB) = B
    if xA > xB:
        (xA, yA, xB, yB) = (xB, yB, xA, yA)
    (xC, yC) = C
    (xD, yD) = D
    if xC > xD:
        (xC, yC, xD, yD) = (xD, yD, xC, yC)
    (xI, yI) = inter_droites(A, B, C, D)
    if xA <= xI <= xB and xC <= xI <= xD or xA <= coord_projete(A, B, C)[0] <= \
        xB and dist_pt_droite(A, B, C) < dmin or xA <= coord_projete(A,
            B, D)[0] <= xB and dist_pt_droite(A, B, D) < dmin or xC <= \
        coord_projete(C, D, A)[0] <= xD and dist_pt_droite(C, D, A) < \
        dmin or xC <= coord_projete(C, D, B)[0] <= xD and dist_pt_droite(C,
            D, B) < dmin or dist_points(A, C) < dmin or dist_points(A, D) < \
        dmin or dist_points(B, C) < dmin or dist_points(B, D) < dmin:
        isValid = False
    else:
        isValid = True
    return isValid


def verifie_angle(lpoints, A, B, C):
    """
    V\xc3\xa9rifie que l'angle BAC ne coupe pas les autres angles d\xc3\xa9j\xc3\xa0 trac\xc3\xa9s
    """

    if len(lpoints) == 0:  #Premier angle créé
        isValid = True
    else:
        for i in range(len(lpoints)):
            (A1, B1, C1) = (lpoints[i])[:3]
            isValid = verifie_distance_mini(A, B, A1, B1) and \
                verifie_distance_mini(A, B, A1, C1) and \
                verifie_distance_mini(A, C, A1, B1) and \
                verifie_distance_mini(A, C, A1, C1)
            if not isValid:
                break
    return isValid


def cree_angles(nb_angles, xmax, ymax):
    '''
    cr\xc3\xa9e une s\xc3\xa9rie d\'angles "non s\xc3\xa9quents"
    '''

    (xmax, ymax) = (xmax - .5, ymax - .5)  #taille de l'image en cm
    lg_seg = 6  #longueur des côtés des angles
    lpoints = []
    cpt = 0  #evite une boucle infinie
    while len(lpoints) < nb_angles and cpt < 1000:
        (xA, yA) = (randrange(5, xmax * 10) / 10.0, randrange(5, ymax *
                    10) / 10.0)
        alpha = randrange(360)  #angle entre un côté et l'horizontal
        if len(lpoints) < nb_angles / 2:
            beta = randrange(90, 180)  #crée un angle droit ou obtus
        else:
            beta = randrange(0, 75) + 15  #crée un angle aigu (entre 15° et 89°)
        xB = xA + lg_seg * cos((alpha * math.pi) / 180)
        yB = yA + lg_seg * sin((alpha * math.pi) / 180)
        xC = xA + lg_seg * cos(((alpha + beta) * pi) / 180)
        yC = yA + lg_seg * sin(((alpha + beta) * pi) / 180)
        (A, B, C) = ((xA, yA), (xB, yB), (xC, yC))
        if xA != xB and xA != xC and .5 < xB < xmax and .5 < yB < ymax and \
            .5 < xC < xmax and .5 < yC < ymax and verifie_angle(lpoints,
                A, B, C):
            lpoints.append((A, B, C, alpha, beta))
        else:
            cpt = cpt + 1

    #print len(lpoints)

    return lpoints


def figure_moodle(moodle, lpoints, lnoms):
    moodle_nom = u'Ángulos: Empareja con su medida'
    moodle_exo = u"Relaciona cada ángulo representado abajo (menor de 180º) con su medida y tipo:\n"
    moodle_exo += "$$\\fs3\\picture(600,120){"
    x_moodle = 70*cos(lpoints[0][4]*pi/180)
    y_moodle = 70*sin(lpoints[0][4]*pi/180)
    moodle_exo += ("(75,15){\\line(70,0)}(75,15){\\line(%s,%s)}(75,15){\\circle(45;0,%s)}(%s,%s){%s}(70,0){%s}(135,0){%s}" %
            (x_moodle, y_moodle, lpoints[0][4], 70+x_moodle+10, 15+y_moodle+5, lnoms[0][1], lnoms[0][0], lnoms[0][2]))
    x_moodle = 70*cos(lpoints[1][4]*pi/180)
    y_moodle = 70*sin(lpoints[1][4]*pi/180)
    moodle_exo += ("(225,15){\\line(70,0)}(225,15){\\line(%s,%s)}(225,15){\\circle(45;0,%s)}(%s,%s){%s}(220,0){%s}(285,0){%s}" %
            (x_moodle, y_moodle, lpoints[1][4], 225+x_moodle+0, 15+y_moodle+5, lnoms[1][1], lnoms[1][0], lnoms[1][2]))
    x_moodle = 70*cos(lpoints[2][4]*pi/180)
    y_moodle = 70*sin(lpoints[2][4]*pi/180)
    moodle_exo += ("(375,15){\\line(70,0)}(375,15){\\line(%s,%s)}(375,15){\\circle(45;0,%s)}(%s,%s){%s}(370,0){%s}(435,0){%s}" %
            (x_moodle, y_moodle, lpoints[2][4], 375+x_moodle+0, 15+y_moodle+5, lnoms[2][1], lnoms[2][0], lnoms[2][2]))
    x_moodle = 70*cos(lpoints[3][4]*pi/180)
    y_moodle = 70*sin(lpoints[3][4]*pi/180)
    moodle_exo += ("(525,15){\\line(70,0)}(525,15){\\line(%s,%s)}(525,15){\\circle(45;0,%s)}(%s,%s){%s}(520,0){%s}(575,0){%s}" %
            (x_moodle, y_moodle, lpoints[3][4], 525+x_moodle-10, 15+y_moodle+5, lnoms[3][1], lnoms[3][0], lnoms[3][2]))
    moodle_exo += "}$$"
    moodle_cor = [[],[],[],[]]
    for i in range(len(lnoms)):
        moodle_cor[i].append(u"$$\\widehat{%s%s%s}$$" % (lnoms[i][1], lnoms[i][0], lnoms[i][2]))
        if lpoints[i][4] < 90:
            moodle_cor[i].append(u"mide %sº y es un ángulo agudo" % lpoints[i][4])
        elif lpoints[i][4] > 90:
            moodle_cor[i].append(u"mide %sº y es un ángulo obtuso" % lpoints[i][4])
        else:
            moodle_cor[i].append(u"mide %sº y es un ángulo recto" % lpoints[i][4])
    moodle.append([moodle_nom, moodle_exo, moodle_cor])


def MesureAngles():
    nb_angles = 4
    (xmax, ymax) = (18, 8)  #taille de l'image en cm
    lnoms = []
    lpoints = []
    cpt = 0
    while len(lpoints) < nb_angles:
        if cpt > 1000:
            lpoints = []
            cpt = 0
        lpoints = cree_angles(nb_angles, xmax, ymax)
        cpt = cpt + 1
    tmpl = Geometrie.choix_points(3 * nb_angles)
    for i in range(nb_angles):
        lnoms.append(tuple(tmpl[3 * i:3 * i + 3]))

    moodle = [u"matching"]

    figure_moodle(moodle, lpoints, lnoms)

    return moodle
