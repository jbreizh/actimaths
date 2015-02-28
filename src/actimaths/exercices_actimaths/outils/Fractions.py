#!/usr/bin/python
# -*- coding: utf-8 -*-

import Arithmetique, Affichage
import random
import math
import os

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
            cor.append("%s%s%s%s%s" % (pre, Fractions.TeX(fr1, True, coef=ppcm // abs(fr1.d)), s, Fractions.TeX(fr2, True, coef=ppcm // abs(fr2.d)), post))
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
    

class Fractions:

    """Classe permettant d'opérer sur les fractions.
    Une fraction est stockée ainsi : (numérateur, dénominateur)"""

    def __init__(self, n, d=1):
        self.numerateur = self.n = n
        self.denominateur = self.d = d


    def simplifie(self):

        # retourne la fraction rendue irréductible

        pgcd = Arithmetique.pgcd(self.n, self.d)
        return Fractions(self.n // pgcd, self.d // pgcd)

    def __str__(self):
        return self.TeX(signe=0,coef=None)
    def TeX(self, signe=0, coef=None):
        """Permet d'écrire une fraction au format TeX.

        @param signe: Si vrai, écrit la fraction avec un dénominateur positif
        @param coef: Multiplie le numérateur et le dénominateur par un même nombre
        """

        if signe:
            (self.n, self.d) = ((self.n * abs(self.d)) // self.d, abs(self.d))
        if self.n:
            if coef and coef != 1:
                text = "\\dfrac{%s_{\\times %s}}{%s_{\\times %s}}" % (self.n,
                        coef, self.d, coef)
            elif self.d != 1:
                text = "\\dfrac{%s}{%s}" % (self.n, self.d)
            else:
                text = "%s" % self.n
        else:
            text = "0"
        return text

    def TeXProduit(self, fraction):
        if self.d < 0:
            (self.n, self.d) = (-self.n, -self.d)
        if fraction.d < 0:
            (fraction.n, fraction.d) = (-fraction.n, -fraction.d)
        c1 = abs(Arithmetique.pgcd(self.n, fraction.d))
        c2 = abs(Arithmetique.pgcd(self.d, fraction.n))
        simplifiable = 0  # permet de savoir si on a simplifiée le produit
        if c1 > 1:
            n1 = "%s \\times \\cancel{%s}" % (self.n // c1, c1)
            d2 = "%s \\times \\cancel{%s}" % (fraction.d // c1, c1)
        else:
            n1 = self.n
            d2 = fraction.d
        if c2 > 1:
            d1 = "%s \\times \\bcancel{%s}" % (self.d // c2, c2)
            n2 = "%s \\times \\bcancel{%s}" % (fraction.n // c2, c2)
        else:
            d1 = self.d
            n2 = fraction.n
        return "%s \\times %s" % (Fractions.TeX(Fractions(n1, d1), signe=
                                  None), Fractions.TeX(Fractions(n2, d2),
                                  signe=None))

    def TeXSimplifie(self):
        frs = Fractions.simplifie(self)
        coef = abs(self.n // frs.n)
        if coef > 1:
            texte = \
                "\\dfrac{%s_{\\times \\cancel %s}}{%s_{\\times \\cancel %s}}" % \
                (self.n // coef, coef, self.d // coef, coef)
        else:
            texte = Fractions.TeX(self, signe=None)
        return texte

    def __add__(self, fraction):
        if (isinstance(fraction,int) or isinstance(fraction,float)):
            fraction=Fractions(fraction)
        if isinstance(fraction,Fractions):
            ppcm = Arithmetique.ppcm(self.d, fraction.d)
            return Fractions((self.n * ppcm) // self.d + (fraction.n * ppcm) //
                         fraction.d, ppcm)
        else:
            return fraction+self

    def __radd__(self,other):
        return self+other

    def __sub__(self, fraction):
        return self + (-fraction)
    def __rsub__(self,other):
        return (-self) + other

    def __mul__(self, fraction):
        if (isinstance(fraction,int) or isinstance(fraction,float)):
            fraction=Fractions(fraction)
        if isinstance(fraction,Fractions):
            return Fractions(self.n * fraction.n, self.d * fraction.d)
        else:
            return fraction*self

    def __rmul__(self,other):
        return self*other

    #def __truediv__(self, fraction): # pour Python 3
    def __div__(self, fraction):
            if (isinstance(fraction,int) or isinstance(fraction,float)):
                fraction=Fractions(fraction)
            if isinstance(fraction,Fractions):
                return Fractions(self.n * fraction.d, self.d * fraction.n)
            else:
                return self*~fraction
    def __rdiv__(self,other):
        return other*~self
    def __invert__(self):
        return Fractions(self.d,self.n)
    def __neg__(self):
        return Fractions(-self.n,self.d)

    def __pow__(self,n):
        result=1
        for i in range(n):
            result=result*self
        return result
    def __trunc__(self):
        return self.n//self.d

    def __lt__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            other=Fractions(other)
        if other.d*self.d > 0:
            return self.n*other.d < self.d * other.n
        else :
            return not(self.n*other.d < self.d * other.n)

    def __le__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            other=Fractions(other)
        if other.d*self.d > 0:
            return self.n*other.d <= self.d * other.n
        else :
            return not(self.n*other.d <= self.d * other.n)

    def __eq__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            other=Fractions(other)
        if isinstance(other,Fractions):
            return self.n*other.d == self.d * other.n

    def __ne__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            other=Fractions(other)
        return self.n*other.d != self.d * other.n

    def __gt__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            other=Fractions(other)
        if other.d*self.d > 0:
            return self.n*other.d > self.d * other.n
        else :
            return not(self.n*other.d > self.d * other.n)

    def __ge__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            other=Fractions(other)
        if other.d*self.d > 0:
            return self.n*other.d >= self.d * other.n
        else :
            return not(self.n*other.d >= self.d * other.n)

    def __float__(self):
        return 1.0*self.n/self.d

    def __int__(self):
        try:
          assert (self.n / self.d == int(self.n / self.d)), 'La fraction n\'est pas un nombre entier !'
          return int(self.n)
        except AssertionError, args:
          print '%s: %s' % (args.__class__.__name__, args)



