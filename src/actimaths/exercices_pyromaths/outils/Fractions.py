#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..classes.Fractions import Fractions
from . import Arithmetique, Affichage
import random
import math


#===============================================================================
# Gère le calcul fractionnaire
#===============================================================================


def EffectueSommeFractions(fr1, fr2, s, pre, post):
    if s == "+":
        fr = fr1 + fr2
    else:
        fr = fr1 - fr2
    cor = []
    if fr1.n and fr2.n:
        ppcm = Arithmetique.ppcm(fr2.d, fr1.d)
        if abs(fr1.d) - abs(fr2.d):
            cor.append("%s%s%s%s%s" % (pre, Fractions.TeX(fr1, True,
                       coef=ppcm // abs(fr1.d)), s, Fractions.TeX(fr2,
                       True, coef=ppcm // abs(fr2.d)), post))
        if pre.rstrip().endswith('(') and post.lstrip().startswith(')'):
            pre = pre.rstrip()[:len(pre.rstrip()) - 1]
            post = post.lstrip()[1:]
        cor.append("%s%s%s" % (pre, Fractions.TeX(fr, True), post))
        if fr.n:
            frs = Fractions.simplifie(fr)
            if abs(frs.n) != abs(fr.n):
                cor.append("%s%s%s" % (pre, Fractions.TeX(frs, True,
                           coef=fr.d // frs.d), post))
                cor.append("%s%s%s" % (pre, Fractions.TeX(frs, True),
                           post))
    else:
        cor.append("%s%s%s" % (pre, Fractions.TeX(fr, True), post))
    return cor


def EffectueProduitFractions(fr1, fr2, pre, post):
    fr1s = Fractions.simplifie(fr1)
    fr2s = Fractions.simplifie(fr2)
    cor = []
    if fr1.n and fr2.n:
        if abs(fr1s.d) < abs(fr1.d) or abs(fr2s.d) < abs(fr2.d):
            cor.append("%s%s \\times %s%s" % (pre, Fractions.TeXSimplifie(fr1),
                       Fractions.TeXSimplifie(fr2), post))
            cor.append("%s%s \\times %s%s" % (pre, Fractions.TeX(fr1s,
                       True), Fractions.TeX(fr2s, True), post))
        fr = fr1s * fr2s
        frs = Fractions.simplifie(fr)
        if abs(frs.d - fr.d):
            cor.append("%s%s%s" % (pre, Fractions.TeXProduit(fr1s, fr2s),
                       post))
        cor.append("%s%s%s" % (pre, Fractions.TeX(frs, True), post))
    else:
        cor.append("%s%s%s" % (pre, Fractions.TeX(Fractions(0), True),
                   post))
    return cor


def EffectueQuotientFractions(fr1, fr2, pre, post):
    fr2 = Fractions(1, 1) / fr2
    cor = ["%s%s \\times %s%s" % (pre, Fractions.TeX(fr1, True),
           Fractions.TeX(fr2, True), post)]
    cor.extend(EffectueProduitFractions(fr1, fr2, pre, post))
    return cor

