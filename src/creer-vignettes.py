#!/usr/bin/python
# -*- coding: utf-8 -*-
from os.path import join
from actimaths.system import creation, lire_liste_exercice
from subprocess import call


environnement = 'pyromaths'
fichier_liste_exercice = join(dirname(__file__), "exercices_%s" % environnement, 'onglets' , 'niveau.xml')
liste_exercice = lire_liste_exercice(fichier_liste_exercice)
parametres = {'sujet_presentation': True,
              'corrige_presentation': False,
              'sujet_page': False,
              'corrige_page': False,
              'titre': 'test',
              'nom_etablissement': 'test',
              'nom_auteur': 'test',
              'temps_slide': '1',
              'date_activite': '1',
              'niveau': 'test',
              'nom_fichier': 'test',
              'chemin_fichier': '/tmp/',
              'environnement': environnement,
              'affichage': 'niveau',
              'chemin_csv': '',
              'modele_presentation': 'Vignette',
              'modele_page': ''}

log = open('/tmp/preview-actimaths.log' , 'w')
for onglet in range(len(liste_exercice)):
    for categorie in range(len(liste_exercice[onglet][1])):
        for exercice in range(len(liste_exercice[onglet][1][categorie][1])):
            valeur_parametre = []
            commande = liste_exercice[onglet][1][categorie][1][exercice][2]
            for parametre in range(len(liste_exercice[onglet][1][categorie][1][exercice][1])):
                valeur_parametre.append(int(liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
            liste = ((commande, valeur_parametre),)
            print liste
            parametres['liste_exos'] = liste
            creation(parametres)
            if environnement == 'pyromaths':
                call(["convert", "-density", "288", "/tmp/test-sujet-presentation.pdf", "-resize", "25%", "-crop", "710x560+0+0", "-trim", "/tmp/%s.png" % commande], stdout=log)
            elif environnement == 'actimaths':
                call(["convert", "-density", "288", "/tmp/test-sujet-presentation.pdf[1]", "-resize", "25%", "-crop", "182x210+0+40", "-trim", "/tmp/%s.png" % commande], stdout=log)
log.close()
