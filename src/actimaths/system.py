#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Actimaths
# Un programme en Python qui permet de créer des presentation de
# mathématiques niveau collège ainsi que leur corrigé en LaTeX.
# Copyright (C) 2013 -- Jean-Baptiste Le Coz (jb.lecoz@gmail.com)
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

## Import globaux
from os.path import join, isfile
from codecs import open
from lxml import etree
from lxml import _elementpath as DONTUSE # Astuce pour inclure lxml dans Py2exe

## Import spécifique à Actimaths
from values import CONFIGDIR, HOME, LATEXDIR

###==============================================================
###        Gestion du fichier de configuration de actimaths
###==============================================================
############## Créé le fichier de configuration par défaut au format xml
def create_config_file():
    root = etree.Element("actimaths")
    child = etree.SubElement(root, "options")
    etree.SubElement(child, "nom_fichier").text="ActiviteMentale"
    etree.SubElement(child, "chemin_fichier").text="%s" % HOME
    etree.SubElement(child, "chemin_executable").text="%s" % LATEXDIR
    etree.SubElement(child, "chemin_csv").text="%s" % HOME
    etree.SubElement(child, "titre_fiche").text=u"Activite Mentale"
    etree.SubElement(child, "nom_etablissement").text=u"Établissement X"
    etree.SubElement(child, "nom_auteur").text="Mr. X"
    etree.SubElement(child, "sujet_presentation").text="True"
    etree.SubElement(child, "corrige_presentation").text="True"
    etree.SubElement(child, "modele_presentation").text="monoColonneCompteur(2)"
    etree.SubElement(child, "sujet_page").text="True"
    etree.SubElement(child, "corrige_page").text="True"
    etree.SubElement(child, "modele_page").text="monoColonne"
    etree.SubElement(child, "environnement").text="actimaths"
    etree.SubElement(child, "affichage").text="niveau"
    etree.SubElement(child, "creer_pdf").text="True"
    etree.SubElement(child, "effacer_tex").text="True"
    etree.SubElement(child, "afficher_pdf").text="True"
    return etree.tostring(root, pretty_print=True, encoding=unicode)

############## Indente correctement les fichiers xml. By Filip Salomonsson; published on February 06, 2007.  http://infix.se/2007/02/06/gentlemen-indent-your-xml
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
            if not e.tail or not e.tail.strip():
                e.tail = i + "  "
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
    return elem

############## Modifie le fichier de configuration si besoin, excepté les options utilisateur déjà configurées
def modify_config_file(file):
    modifie = False
    oldtree = etree.parse(file)
    oldroot = oldtree.getroot()
    newroot = etree.XML(create_config_file())
    for element in newroot.iter(tag=etree.Element):
        if not len(element):
            parents = [element]
            e = element.getparent()
            while e is not None:
                parents.insert(0,e)
                e = e.getparent()
            oldtag = oldroot
            for i in range(1, len(parents)):
                if oldtag.find(parents[i].tag) is None and i < len(parents) - 1 :
                    if i > 1:
                        etree.SubElement(oldroot.find(parents[i-1].tag), parents[i].tag)
                    else:
                        etree.SubElement(oldroot, parents[i].tag)
                    oldtag = oldtag.find(parents[i].tag)
                else:
                    oldtag = oldtag.find(parents[i].tag)
                if i == len(parents)-2: oldparent = oldtag
            if oldtag is None:
                # Ajoute un nouvel item dans le fichier xml
                modifie = True
                etree.SubElement(oldparent, element.tag).text =  element.text
            elif oldtag.text != element.text and parents[1].tag != "options":
                # Modifie un item existant s'il ne s'agit pas des options
                modifie = True
                oldtag.text =  element.text
    if modifie:
        f = open(join(CONFIGDIR, "actimaths.xml"), encoding='utf-8', mode = 'w')
        f.write(etree.tostring(indent(oldroot), pretty_print=True, encoding=unicode))
        f.close()

##############  Test de la création du fichier de configuration
def test(gui):
    if not isfile(join(CONFIGDIR, "actimaths.xml")):
        gui.erreur_critique(u"Impossible de lire le fichier de configuration." \
                u"Veuillez vérifier ce dernier ou faire remonter l'erreur " \
                u"sur le forum de actimaths.")

############## Lis le fichier de configuration actimaths.xml, enregistre les données dans un dictionnaire config
def lire_config(file):
    config = {}
    tree = etree.parse(file)
    root = tree.getroot()
    options = root.find('options')
    for child in options:
        if child.text == 'True':
            text = '1'
        elif child.text == 'False':
            text = '0'
        else :
            text = child.text
        config[child.tag] = text
    return config

###==============================================================
### Fonction de gestion de la liste d'exercice
###==============================================================
############## lis le fichier listant les exercices au format xml
def lire_liste_exercice(file):
    tree = etree.parse(file)
    root = tree.getroot()
    liste = []
    for onglet in root.iter("onglet"):
        nom_onglet = onglet.get("nom")
        liste_categorie = []
        for categorie in onglet.iter("categorie"):
            nom_categorie = categorie.get("nom")
            liste_exercice = []
            for exercice in categorie.iter("exercice"):
                nom_exercice = exercice.get("nom")
                commande_exercice = exercice.get("commande")
                temps_exercice = exercice.get("temps")
                liste_parametre = []
                for parametre in exercice.iter("parametre"):
                    nom_parametre = parametre.get("nom")
                    min_parametre = parametre.get("min")
                    max_parametre = parametre.get("max")
                    defaut_parametre = parametre.get("defaut")
                    liste_parametre.append([nom_parametre, min_parametre, max_parametre, defaut_parametre])
                liste_exercice.append([nom_exercice, liste_parametre, commande_exercice, temps_exercice])
            liste_categorie.append([nom_categorie, liste_exercice])
        liste.append([nom_onglet, liste_categorie])
    return liste
