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
from math import floor

def rang_premiere_decimale(nombre):
    #Conversion de la partie décimale en liste
    nombre_list = [str(nombre)[i] for i in range(2,len(str(nombre)))]
    #Comptage du premier caractère différent de 0
    premiere_decimale = 0
    for i in range(len(nombre_list)):
        if nombre_list[i] != '0':
            premiere_decimale =  i + 1
            break
    return premiere_decimale

def encadrement(nombre):
    #Separation de la partie entière et décimale
    partieEntiere = int(floor(nombre))
    partieDecimale = nombre - partieEntiere
    #arrondi du nombre pour ne garder qu'un seul chiffre significatif
    if partieEntiere:
        precision = 1 - len(str(partieEntiere))
        arrondi = int(round(nombre, precision))
    else:
        precision = rang_premiere_decimale(partieDecimale)
        arrondi = round(nombre, precision)
    #valeur par defaut et exces
    if (arrondi > nombre):
        defaut = arrondi - 10 ** - precision
        exces = arrondi
    else:
        defaut = arrondi
        exces = arrondi + 10 ** - precision
    return (defaut, arrondi, exces)

def valeurEntier(nombre_min, nombre_max):
    nombre = random.randrange(nombre_min, nombre_max)
    return nombre

def valeurDecimal(nombre_min, nombre_max):
    #Generation du nombre
    e = random.randrange(3,6)
    partieEntiere = random.randrange(nombre_min, nombre_max)
    partieDecimale = random.randrange(100, 1000) * 10 ** -e
    nombre = partieEntiere + partieDecimale
    return nombre

def valeurNumerateur(numerateur, denominateurArrondi):
    #Partie entière et décimale + rang des 2 premiers chiffres pour le numerateur
    numerateur_partieEntiere            = int(floor(numerateur))
    numerateur_partieDecimale           = numerateur - numerateur_partieEntiere
    numerateur_partieEntiere_precision  = min(len(str(numerateur_partieEntiere)),2) - len(str(numerateur_partieEntiere))
    numerateur_partieDecimale_precision = 1 + rang_premiere_decimale(numerateur_partieDecimale)

    #Partie entière et décimale + rang du premier chiffre pour le denominateurArrondi
    denominateurArrondi_partieEntiere            = int(floor(denominateurArrondi))
    denominateurArrondi_partieDecimale           = denominateurArrondi - denominateurArrondi_partieEntiere
    denominateurArrondi_partieEntiere_precision  = 1 - len(str(denominateurArrondi_partieEntiere))
    denominateurArrondi_partieDecimale_precision = rang_premiere_decimale(denominateurArrondi_partieDecimale)

    #On ne prend que les 2 premiers chiffres du numerateur
    if numerateur_partieEntiere:
        numerateur_chiffre = int(floor(numerateur_partieEntiere * 10 ** numerateur_partieEntiere_precision))
    else:
        numerateur_chiffre = int(floor(numerateur_partieDecimale * 10 ** numerateur_partieDecimale_precision))

    #On ne prend que le 1er chiffre du denominateurArrondi
    if denominateurArrondi_partieEntiere:
        denominateurArrondi_chiffre = int(floor(denominateurArrondi_partieEntiere * 10 ** denominateurArrondi_partieEntiere_precision))
    else:
        denominateurArrondi_chiffre = int(floor(denominateurArrondi_partieDecimale * 10 ** denominateurArrondi_partieDecimale_precision))

    #On choisi le multiple de denominateurArrondi_chiffre le plus proche de numerateur_chiffre
    numerateurArrondi_chiffre = int(round(float(numerateur_chiffre) / denominateurArrondi_chiffre) * denominateurArrondi_chiffre)

    #On complète numerateurArrondi_chiffre pour qu'il fasse la même taille que numerateur
    if numerateur_partieEntiere:
         numerateurArrondi = int(numerateurArrondi_chiffre * 10 ** (- numerateur_partieEntiere_precision))
    else:
         numerateurArrondi = numerateurArrondi_chiffre * 10 ** (- numerateur_partieDecimale_precision)

    return (numerateurArrondi, denominateurArrondi_chiffre, numerateurArrondi_chiffre)

############################Construction####################################################

def NombreEntier(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre = valeurEntier(parametre[0], parametre[1])
    (defaut, arrondi, exces) = encadrement(nombre)
    exo.append("$$ %s $$" % nombre)
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut, nombre, exces, nombre, arrondi))
    cor.append("L'ordre de grandeur de %s est %s" % (nombre, arrondi))
    return (exo, cor, question)

def NombreDecimal(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre = valeurDecimal(parametre[0], parametre[1])
    (defaut, arrondi, exces) = encadrement(nombre)
    exo.append("$$ %s $$" % nombre)
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut, nombre, exces, nombre, arrondi))
    cor.append("L'ordre de grandeur de %s est %s" % (nombre, arrondi))
    return (exo, cor, question)

def AdditionEntier(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre1 = valeurEntier(parametre[0], parametre[1])
    (defaut1, arrondi1, exces1) = encadrement(nombre1)
    nombre2 = valeurEntier(parametre[0], parametre[1])
    (defaut2, arrondi2, exces2) = encadrement(nombre2)
    exo.append("$$ %s + %s $$" % (nombre1, nombre2))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut1, nombre1, exces1, nombre1, arrondi1))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut2, nombre2, exces2, nombre2, arrondi2))
    cor.append("$%s + %s \\approx  %s + %s \\approx %s $" % (nombre1, nombre2, arrondi1, arrondi2, arrondi1 + arrondi2))
    return (exo, cor, question)

def AdditionDecimal(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre1 = valeurDecimal(parametre[0], parametre[1])
    (defaut1, arrondi1, exces1) = encadrement(nombre1)
    nombre2 = valeurDecimal(parametre[0], parametre[1])
    (defaut2, arrondi2, exces2) = encadrement(nombre2)
    exo.append("$$ %s + %s $$" % (nombre1, nombre2))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut1, nombre1, exces1, nombre1, arrondi1))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut2, nombre2, exces2, nombre2, arrondi2))
    cor.append("$%s + %s \\approx  %s + %s \\approx %s $" % (nombre1, nombre2, arrondi1, arrondi2, arrondi1 + arrondi2))
    return (exo, cor, question)

def SoustractionEntier(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre1Temp = valeurEntier(parametre[0], parametre[1])
    nombre2Temp = valeurEntier(parametre[0], parametre[1])
    if nombre1Temp > nombre2Temp:
        nombre1 = nombre1Temp
        nombre2 = nombre2Temp
    else:
        nombre1 = nombre2Temp
        nombre2 = nombre1Temp
    (defaut1, arrondi1, exces1) = encadrement(nombre1)
    (defaut2, arrondi2, exces2) = encadrement(nombre2)
    exo.append("$$ %s - %s $$" % (nombre1, nombre2))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut1, nombre1, exces1, nombre1, arrondi1))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut2, nombre2, exces2, nombre2, arrondi2))
    cor.append("$%s - %s \\approx  %s - %s \\approx %s $" % (nombre1, nombre2, arrondi1, arrondi2, arrondi1 - arrondi2))
    return (exo, cor, question)

def SoustractionDecimal(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre1Temp = valeurDecimal(parametre[0], parametre[1])
    nombre2Temp = valeurDecimal(parametre[0], parametre[1])
    if nombre1Temp > nombre2Temp:
        nombre1 = nombre1Temp
        nombre2 = nombre2Temp
    else:
        nombre1 = nombre2Temp
        nombre2 = nombre1Temp
    (defaut1, arrondi1, exces1) = encadrement(nombre1)
    (defaut2, arrondi2, exces2) = encadrement(nombre2)
    exo.append("$$ %s - %s $$" % (nombre1, nombre2))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut1, nombre1, exces1, nombre1, arrondi1))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut2, nombre2, exces2, nombre2, arrondi2))
    cor.append("$%s - %s \\approx  %s - %s \\approx %s $" % (nombre1, nombre2, arrondi1, arrondi2, arrondi1 - arrondi2))
    return (exo, cor, question)

def MultiplicationEntier(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre1 = valeurEntier(parametre[0], parametre[1])
    (defaut1, arrondi1, exces1) = encadrement(nombre1)
    nombre2 = valeurEntier(parametre[0], parametre[1])
    (defaut2, arrondi2, exces2) = encadrement(nombre2)
    exo.append("$$ %s \\times %s $$" % (nombre1, nombre2))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut1, nombre1, exces1, nombre1, arrondi1))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut2, nombre2, exces2, nombre2, arrondi2))
    cor.append("$%s \\times %s \\approx  %s \\times %s \\approx %s $" % (nombre1, nombre2, arrondi1, arrondi2, arrondi1 * arrondi2))
    return (exo, cor, question)

def MultiplicationDecimal(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    nombre1 = valeurDecimal(parametre[0], parametre[1])
    (defaut1, arrondi1, exces1) = encadrement(nombre1)
    nombre2 = valeurDecimal(parametre[0], parametre[1])
    (defaut2, arrondi2, exces2) = encadrement(nombre2)
    exo.append("$$ %s \\times %s $$" % (nombre1, nombre2))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut1, nombre1, exces1, nombre1, arrondi1))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline" % (defaut2, nombre2, exces2, nombre2, arrondi2))
    cor.append("$%s \\times %s \\approx  %s \\times %s \\approx %s $" % (nombre1, nombre2, arrondi1, arrondi2, arrondi1 * arrondi2))
    return (exo, cor, question)

def DivisionEntier(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    denominateur = valeurEntier(parametre[0], parametre[1])
    (denominateur_defaut, denominateur_arrondi, denominateur_exces) = encadrement(denominateur)
    numerateur =  valeurEntier(parametre[0], parametre[1])
    (numerateur_arrondi, denominateur_arrondi_chiffre, numerateur_arrondi_chiffre) = valeurNumerateur(numerateur, denominateur_arrondi)
    exo.append("$$ %s \\div %s $$" % (numerateur, denominateur))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline"  % (denominateur_defaut, denominateur, denominateur_exces, denominateur, denominateur_arrondi))
    cor.append("$ %s \\times %s = %s $ donc $ %s \\approx %s $ \\newline" 
               % (denominateur_arrondi_chiffre, numerateur_arrondi_chiffre/denominateur_arrondi_chiffre, numerateur_arrondi_chiffre, numerateur, numerateur_arrondi) )
    cor.append("donc $%s \\div %s \\approx  %s \\div %s \\approx %s $" 
               % (numerateur, denominateur, numerateur_arrondi, denominateur_arrondi, float(numerateur_arrondi)/ denominateur_arrondi))
    return (exo, cor, question)

def DivisionDecimal(parametre):
    question = u"Donner un ordre de grandeur de :"
    exo = [ ]
    cor = [ ]
    denominateur = valeurDecimal(parametre[0], parametre[1])
    (denominateur_defaut, denominateur_arrondi, denominateur_exces) = encadrement(denominateur)
    numerateur =  valeurDecimal(parametre[0], parametre[1])
    (numerateur_arrondi, denominateur_arrondi_chiffre, numerateur_arrondi_chiffre) = valeurNumerateur(numerateur, denominateur_arrondi)
    exo.append("$$ %s \\div %s $$" % (numerateur, denominateur))
    cor.append("$ %s < %s < %s $ donc $ %s \\approx %s$ \\newline"  % (denominateur_defaut, denominateur, denominateur_exces, denominateur, denominateur_arrondi))
    cor.append("$ %s \\times %s = %s $ donc $ %s \\approx %s $ \\newline" 
               % (denominateur_arrondi_chiffre, numerateur_arrondi_chiffre/denominateur_arrondi_chiffre, numerateur_arrondi_chiffre, numerateur, numerateur_arrondi) )
    cor.append("donc $%s \\div %s \\approx  %s \\div %s \\approx %s $" 
               % (numerateur, denominateur, numerateur_arrondi, denominateur_arrondi, float(numerateur_arrondi)/ denominateur_arrondi))
    return (exo, cor, question)
