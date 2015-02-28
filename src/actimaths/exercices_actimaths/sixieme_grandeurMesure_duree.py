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


import math
import random
import string
from outils import Arithmetique, Affichage

#---------------fonction pour les additions sur les heures--------------------------------
def mon_int(t):  # retourne un entier texte sous la forme d'un nombre, zéro sinon
    if t == '':
        t = 0
    elif ('1234567890').count(t):
        t = int(t)
    else:
        t = 0
    return t

def liste_heure(nba_heure,nba_minute):
    deca = [str(nba_heure)[i] for i in range(len(str(nba_heure)))]
    deca.append('h')
    if nba_minute<10:
        deca.append('0')
    deca.extend(str(nba_minute)[i] for i in range(len(str(nba_minute))))
    return deca

def lignes(ligne, deca, lavtvirg, laprvirg):
    lavtvirga = deca.index('h')
    laprvirga = len(deca) - lavtvirga
    if lavtvirga < lavtvirg:
        for i in range(lavtvirg - lavtvirga):
            ligne.append('')
    for i in range(lavtvirga+1):
        ligne.append(str(deca[i]))
    if laprvirga < laprvirg:
        for i in range(laprvirg - laprvirga):
            ligne.append('')
    for i in range(lavtvirga+1,len(deca)):
        ligne.append(str(deca[i]))
    return ligne

def valeurs_addition(heure_min, heure_max):
    # heure 1
    nba_heure = random.randrange(heure_min, heure_max)
    nba_minute = random.randrange(0,60)
    deca = liste_heure(nba_heure,nba_minute)
    # heure 2
    nbb_heure = random.randrange(heure_min, heure_max)
    nbb_minute = random.randrange(0,60)
    decb = liste_heure(nbb_heure,nbb_minute)
    # resultat
    nbtotal_heure = nba_heure + nbb_heure
    nbtotal_minute = nba_minute + nbb_minute
    dectotal = liste_heure(nbtotal_heure,nbtotal_minute)
    # resultat avec les minutes corrigés
    nbtotal_heure_corrige = nbtotal_heure
    nbtotal_minute_corrige = nbtotal_minute
    while nbtotal_minute_corrige >= 60:
        nbtotal_heure_corrige += 1
        nbtotal_minute_corrige -= 60
    dectotal_corrige = liste_heure(nbtotal_heure_corrige,nbtotal_minute_corrige)
    # longueur max des heures et des minutes
    lavtvirg = dectotal.index('h')
    laprvirg = len(dectotal) - lavtvirg
    return (deca, decb, dectotal, dectotal_corrige, lavtvirg, laprvirg)

def retenues_addition(ligne1, ligne2):
    lg = len(ligne1)
    ligne0 = ['' for i in range(lg)]
    for i in range(lg - 1):
        #on met la retenue à 1 si le total depasse 9
        if mon_int(ligne1[(lg - i) - 1]) + mon_int(ligne2[(lg - i) - 1]) + mon_int(ligne0[(lg - i) - 1]) > 9:
            ligne0[(lg - i) - 2] = '1'
    return ligne0

def tex_addition(exo, cor, heure_min, heure_max):
    # paramètre
    (deca, decb, dectotal,dectotal_corrige, lavtvirg, laprvirg) = valeurs_addition(heure_min, heure_max)
    nba = ''.join(deca)
    nbb = ''.join(decb)
    nbtotal = ''.join(dectotal)
    nbtotal_corrige = ''.join(dectotal_corrige)
    # construction des lignes
    (ligne1, ligne2, ligne3) = ([''], ['+'],[''])
    ligne1 = lignes(ligne1, deca, lavtvirg, laprvirg)
    ligne2 = lignes(ligne2, decb, lavtvirg, laprvirg)
    ligne3 = lignes(ligne3, dectotal, lavtvirg, laprvirg)
    ligne0 = retenues_addition(ligne1, ligne2)
    # affichage
    if ligne0[0] == '1':
        ligne0[0] = '\\tiny 1'
    exo.append('$$ %s + %s = \\ldots $$' % (nba,nbb ))
    cor.append('\\begin{center}')
    cor.append('\\begin{footnotesize}')
    cor.append('\\begin{tabular}[t]{*{%s}{c}}' % (lavtvirg + laprvirg + 1))
    cor.append('%s \\\\' % ' & \\tiny '.join(ligne0))
    cor.append('%s \\\\' % ' & '.join(ligne1))
    cor.append('%s \\\\\n\\hline' % ' & '.join(ligne2))
    cor.append('%s \\\\' % ' & '.join(ligne3))
    cor.append('\\end{tabular}\\par')
    cor.append('\\end{footnotesize}')
    cor.append('\\end{center}')
    if nbtotal_corrige != nbtotal:
        cor.append(u"On transforme 60 min en 1h au résultat :")
        cor.append("$$%s+%s = \\boxed{%s}$$" % (nba,nbb,nbtotal_corrige))
    else:
        cor.append("$$%s+%s = \\boxed{%s}$$" % (nba,nbb,nbtotal))

#--------------Construction des exercices-----------------------
def AdditionHeure(parametre):
    question = "Poser l'addition d'heure :"
    exo = [ ]
    cor = [ ]
    tex_addition(exo, cor,parametre[0],parametre[1])
    return exo, cor, question

#---------------fonction pour les soustractions sur les heures--------------------------------
def valeurs_soustraction(heure_min, heure_max):
    # heure 2
    nbb_heure = random.randrange(heure_min, heure_max)
    nbb_minute = random.randrange(0,60)
    decb = liste_heure(nbb_heure,nbb_minute)
    while True:
        # heure 1
        nba_heure = random.randrange(heure_min, heure_max)
        nba_minute = random.randrange(0,60)
        deca = liste_heure(nba_heure,nba_minute)
        # heure 1 corrigés
        nba_heure_corrige = nba_heure
        nba_minute_corrige = nba_minute
        while nba_minute_corrige < nbb_minute:
            nba_heure_corrige -= 1
            nba_minute_corrige += 60
        deca_corrige = liste_heure(nba_heure_corrige,nba_minute_corrige)
        if nba_heure_corrige >= nbb_heure:
            break
    # resultat
    nbtotal_heure = nba_heure_corrige - nbb_heure
    nbtotal_minute = nba_minute_corrige - nbb_minute
    dectotal = liste_heure(nbtotal_heure,nbtotal_minute)
    # longueur max des heures et des minutes
    posa_corrige = deca_corrige.index('h')
    posb = decb.index('h')
    postotal = dectotal.index('h')
    lavtvirg = max(posa_corrige, posb, postotal)
    laprvirg = max(len(deca_corrige) - posa_corrige, len(decb) - posb, len(dectotal) - postotal)
    return (deca, deca_corrige, decb, dectotal, lavtvirg, laprvirg)

def retenues_soustraction(ligne1, ligne2):
    lg = len(ligne1)
    ret = 0
    for i in range(lg - 1):
        if not (ligne1[(lg - i) - 1] == 'h' and ret):
            if mon_int(ligne1[(lg - i) - 1]) < mon_int(ligne2[(lg - i) - 1]) + ret:
                ligne1[(lg - i) - 1] = '$_1$%s' % ligne1[(lg - i) - 1]
                tmpret = 1
            else:
                tmpret = 0
            if ret:
                ligne2[(lg - i) - 1] = '%s$_1$' % ligne2[(lg - i) - 1]
            ret = tmpret
    return (ligne1, ligne2)

def tex_soustraction(exo, cor, heure_min, heure_max):
    # paramètre
    (deca, deca_corrige, decb, dectotal, lavtvirg, laprvirg) = valeurs_soustraction(heure_min, heure_max)
    nba = ''.join(deca)
    nba_corrige = ''.join(deca_corrige)
    nbb = ''.join(decb)
    nbtotal = ''.join(dectotal)
    # construction des lignes
    (ligne1, ligne2,ligne3) = ([''], ['-'], [''])
    ligne1 = lignes(ligne1, deca_corrige, lavtvirg, laprvirg)
    ligne2 = lignes(ligne2, decb, lavtvirg, laprvirg)
    ligne3 = lignes(ligne3, dectotal, lavtvirg, laprvirg)
    (ligne1, ligne2) = retenues_soustraction(ligne1, ligne2)
    # affichage
    exo.append('$$ %s - %s = \\ldots $$' % (nba,nbb))
    if nba_corrige != nba:
        cor.append(u"On transforme 1h en 60min à la 1\iere{} heure :")
    cor.append('\\begin{center}')
    cor.append('\\begin{footnotesize}')
    cor.append('\\begin{tabular}[t]{*{%s}{c}}' % (lavtvirg + laprvirg + 1))
    cor.append('%s \\\\' % ' & '.join(ligne1))
    cor.append('%s \\\\\n\\hline' % ' & '.join(ligne2))
    cor.append('%s \\\\' % ' & '.join(ligne3))
    cor.append('\\end{tabular}\\par')
    cor.append('\\end{footnotesize}')
    cor.append('\\end{center}')
    cor.append("$$%s-%s = \\boxed{%s}$$" % (nba,nbb,nbtotal))

#--------------Construction des exercices-----------------------
def SoustractionHeure(parametre):
    question = "Poser la soustraction d'heure :"
    exo = [ ]
    cor = [ ]
    tex_soustraction(exo, cor ,parametre[0],parametre[1])
    return exo, cor, question

#---------------fonction pour l'horloge--------------------------------
def tex_horloge(tex, heure, minute):
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

#--------------Construction des exercices-----------------------
def LectureHorloge(parametre):
    heure = random.randrange(12)
    minute = random.randrange(0,60,5)
    # initialisation
    question = u"Quelle heure est-il ? :"
    exo = []
    cor = []
    # affichage de l'horloge
    tex_horloge(exo, heure, minute)
    tex_horloge(cor, heure, minute)
    # corrige
    cor.append("\\begin{center}")
    if minute > 9:
        cor.append("Il est $\\boxed{%sh%s}$ ou $\\boxed{%sh%s}$" %(heure, minute, heure+12, minute))
    else:
        cor.append("Il est $\\boxed{%sh0%s}$ ou $\\boxed{%sh0%s}$" %(heure, minute, heure+12, minute))
    cor.append("\\end{center}")
    return (exo, cor, question)

#---------------fonction pour les conversions--------------------------------
def tex_tableau(tex, contenu):
    nombreColonne = len(contenu)
    if nombreColonne != 0:
        nombreLigne = len(contenu[0])
        # entete du tableau
        tex.append("\\begin{center}")
        ligne = "\\begin{tabular}{|"
        for i in range(len(contenu)):
            ligne += "c|"
        ligne += "}"
        tex.append(ligne)
        # corps du tableau
        for i in range(nombreLigne):
            tex.append("\\hline")
            ligne = ""
            for j in range(nombreColonne):
                ligne += "%s" % contenu[j][i]
                if j != nombreColonne - 1:
                   ligne += "&"
            ligne += "\\\\"
            tex.append(ligne)
        tex.append("\\hline")
        # fin du tableau
        tex.append("\\end{tabular}")
        tex.append("\\end{center}")

#--------------Construction des exercices-----------------------
def ConversionHeureMinute(parametre):
    # variables
    heure =  random.randrange(parametre[0],parametre[1])
    minute = heure * 60
    choix = random.randrange(2)
    if choix:
        contenuTableauEnonce = [["Heure","Minute"],[1,60],[heure,"\\ldots"]]
    else:
        contenuTableauEnonce = [["Heure","Minute"],[1,60],["\\ldots",minute]]
    contenuTableauCorrige = [["Heure","Minute"],[1,60],[heure,minute]]
    # initialisation
    question = u"Fais la conversion :"
    exo = []
    cor = []
    # affichage du tableau
    tex_tableau(exo, contenuTableauEnonce)
    tex_tableau(cor, contenuTableauCorrige)
    # enonce et corrige
    if choix:
        exo.append("$$ %s h = \\ldots min $$" % heure)
        cor.append("$$ %s h = %s \\times 60 $$" % (heure, heure))
        cor.append("$$ %s h = \\boxed{%s min} $$" % (heure, minute))
    else:
        exo.append("$$ %s min = \\ldots h $$" % minute)
        cor.append("$$ %s min = %s \\div 60 $$" % (minute, minute))
        cor.append("$$ %s min = \\boxed{%s h} $$" % (minute, heure))
    return (exo, cor, question)

def ConversionMinuteSeconde(parametre):
    # variables
    minute =  random.randrange(parametre[0],parametre[1])
    seconde = minute * 60
    choix = random.randrange(2)
    if choix:
        contenuTableauEnonce = [["Minute","Seconde"],[1,60],[minute,"\\ldots"]]
    else:
        contenuTableauEnonce = [["Minute","Seconde"],[1,60],["\\ldots",seconde]]
    contenuTableauCorrige = [["Minute","Seconde"],[1,60],[minute,seconde]]
    # initialisation
    question = u"Fais la conversion :"
    exo = []
    cor = []
    # affichage du tableau
    tex_tableau(exo, contenuTableauEnonce)
    tex_tableau(cor, contenuTableauCorrige)
    # enonce et corrige
    if choix:
        exo.append("$$ %s min = \\ldots s $$" % minute)
        cor.append("$$ %s min = %s \\times 60 $$" % (minute, minute))
        cor.append("$$ %s min = \\boxed{%s s} $$" % (minute, seconde))
    else:
        exo.append("$$ %s s = \\ldots min $$" % seconde)
        cor.append("$$ %s s = %s \\div 60 $$" % (seconde, seconde))
        cor.append("$$ %s s = \\boxed{%s min} $$" % (seconde, minute))
    return (exo, cor, question)

