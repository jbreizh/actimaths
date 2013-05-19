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

## Import globaux
from os import listdir
from os.path import join, isfile, isdir
from PyQt4 import QtGui, QtCore
from codecs import open
from lxml import etree
from lxml import _elementpath as DONTUSE # Astuce pour inclure lxml dans Py2exe
from time import strftime ,localtime
from threading import Thread
from sip import delete

## Import spécifique à Actimaths
from system import creation, lire_config, lire_liste_exercice
from values import HOME, CONFIGDIR, DATADIR, COPYRIGHTS, VERSION, WEBSITE, DESCRIPTION, CREDITS

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #============================================================
        #        lecture du fichier de configuration
        #============================================================
        self.fichier_configuration = join(CONFIGDIR,  "actimaths.xml")
        self.config = lire_config(self.fichier_configuration)
        
        #============================================================
        #        Initialisation
        #============================================================
        MainWindow.setWindowIcon(QtGui.QIcon(join(DATADIR, 'images','actimaths.png')))
        MainWindow.setWindowTitle("Actimaths")
        MainWindow.setGeometry(0, 44, 1000, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        ## 
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        ## 
        self.gridLayout_1 = QtGui.QGridLayout(self.centralwidget)

        #============================================================
        #        Boutons créer, quitter et annuler
        #============================================================
        ## 
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(9)
        self.gridLayout_1.addLayout(self.verticalLayout, 0, 1, 1, 1)
        ## Bouton Créer
        self.pushButton_ok = QtGui.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton_ok)
        self.pushButton_ok.setText(u"Créer")
        self.pushButton_ok.setToolTip(u"Créer à partir de sa sélection")
        self.pushButton_ok.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(46, 139, 87, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.connect(self.pushButton_ok,QtCore.SIGNAL("clicked()"), self.creer_les_exercices)
        ## Bouton Quitter
        self.pushButton_quit = QtGui.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton_quit)
        self.pushButton_quit.setText("Quitter")
        self.pushButton_quit.setToolTip(u"Quitter Actimaths")
        self.pushButton_quit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(238, 44, 44, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.connect(self.pushButton_quit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        ## Bouton Réinitialiser
        self.pushButton_erase = QtGui.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton_erase)
        self.pushButton_erase.setText(u"Réinitialiser")
        self.pushButton_erase.setToolTip(u"Remettre à zéro sa sélection")
        self.pushButton_erase.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.connect(self.pushButton_erase, QtCore.SIGNAL("clicked()"), self.effacer_choix_exercices)
        ## Espace
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        #============================================================
        #        Onglets de la zone centrale
        #============================================================
        ## Construction d'une zone d'onglet
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.gridLayout_1.addWidget(self.tabWidget, 0, 0, 1, 1)
        ## Construction des onglets
        self.construction_onglet(self.config['environnement'],self.config['affichage'])

        #============================================================
        #        Barre de menus
        #============================================================
        ## Construction de la barre
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.menubar)
        ## Menu Fichier
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setTitle("Fichier")
        ## Action Tous les Exercices 
        self.actionTous_les_exercices = QtGui.QAction(MainWindow)
        self.actionTous_les_exercices.setText("Tous les exercices")
        QtCore.QObject.connect(self.actionTous_les_exercices, QtCore.SIGNAL("triggered()"), self.creer_tous_les_exercices)
        ## Action Quitter
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setText("Quitter")
        QtCore.QObject.connect(self.actionQuitter, QtCore.SIGNAL("triggered()"), QtGui.qApp, QtCore.SLOT("quit()"))
        ## Construction du menu fichier
        self.menuFichier.addAction(self.actionTous_les_exercices)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())
        ## Menu Environnement
        self.menuEnvironnement = QtGui.QMenu(self.menubar)
        self.menuEnvironnement.setTitle(u"Environnement")
        ## Action Actimaths
        self.actionActimaths = QtGui.QAction(MainWindow)
        self.actionActimaths.setText("Actimaths")
        QtCore.QObject.connect(self.actionActimaths, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet("actimaths", self.affichage))
        ## Action Pyromaths
        self.actionPyromaths = QtGui.QAction(MainWindow)
        self.actionPyromaths.setText("Pyromaths")
        QtCore.QObject.connect(self.actionPyromaths, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet("pyromaths", self.affichage))
        ## Construction du menu Environnement
        self.menuEnvironnement.addAction(self.actionActimaths)
        self.menuEnvironnement.addAction(self.actionPyromaths)
        self.menubar.addAction(self.menuEnvironnement.menuAction())
        ## Menu Présentation
        self.menuAffichage = QtGui.QMenu(self.menubar)
        self.menuAffichage.setTitle(u"Affichage")
        ## Action Par niveaux
        self.actionPar_niveaux = QtGui.QAction(MainWindow)
        self.actionPar_niveaux.setText("Par niveaux")
        QtCore.QObject.connect(self.actionPar_niveaux, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet(self.environnement, "niveau"))
        ## Action Par domaine
        self.actionPar_domaine = QtGui.QAction(MainWindow)
        self.actionPar_domaine.setText("Par domaine")
        QtCore.QObject.connect(self.actionPar_domaine, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet(self.environnement, "domaine"))
        ## Action CSV
        self.actionCsv = QtGui.QAction(MainWindow)
        self.actionCsv.setText("Csv")
        QtCore.QObject.connect(self.actionCsv, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet(self.environnement, "csv"))
        ## Action Vide
        self.action_vide = QtGui.QAction(MainWindow)
        self.action_vide.setText("Vide")
        QtCore.QObject.connect(self.action_vide, QtCore.SIGNAL("triggered()"), lambda:self.construction_onglet(self.environnement, "vide"))
        ## Construction du menu Affichage
        self.menuAffichage.addAction(self.actionPar_niveaux)
        self.menuAffichage.addAction(self.actionPar_domaine)
        self.menuAffichage.addAction(self.actionCsv)
        self.menuAffichage.addSeparator()
        self.menuAffichage.addAction(self.action_vide)
        self.menubar.addAction(self.menuAffichage.menuAction())
        ## Menu Aide
        self.menu_propos = QtGui.QMenu(self.menubar)
        self.menu_propos.setTitle("Aide")
        ## Action Aide en ligne
        self.actionAide_en_ligne = QtGui.QAction(MainWindow)
        self.actionAide_en_ligne.setText(u"Aide en ligne")
        QtCore.QObject.connect(self.actionAide_en_ligne, QtCore.SIGNAL("triggered()"), self.site)
        ## Action À propos
        self.action_a_propos = QtGui.QAction(MainWindow)
        self.action_a_propos.setText(u"À propos")
        QtCore.QObject.connect(self.action_a_propos, QtCore.SIGNAL("triggered()"), self.about)
        ## Construction du menu Aide
        self.menu_propos.addAction(self.actionAide_en_ligne)
        self.menu_propos.addSeparator()
        self.menu_propos.addAction(self.action_a_propos)
        self.menubar.addAction(self.menu_propos.menuAction())

        #============================================================
        #        Barre d'état
        #============================================================
        self.barre_etat = QtGui.QStatusBar(MainWindow)
        ## Message d'aide
        self.barre_etat_label= QtGui.QLabel(self.barre_etat)
        self.barre_etat_label.setText(u"Pour avoir un aperçu d'un exercice, positionner le curseur de la souris sur le point d'interrogation.")
        self.barre_etat.insertWidget(0, self.barre_etat_label, 0)
        MainWindow.setStatusBar(self.barre_etat)

    ###============================================================
    ###   Fonctions d'interface
    ###============================================================
    ############## Construit les onglets
    def construction_onglet(self, environnement, affichage):
        ## On supprime tous les onglets et on les supprime pour recuperer la memoire
        self.tabWidget.clear()
        delete(self.tabWidget)
        self.tabWidget = None
        ## On reconstruit les onglets
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.gridLayout_1.addWidget(self.tabWidget, 0, 0, 1, 1)
        ## On met à jour dans la configuration l'environnement et l'affichage
        self.environnement = environnement
        self.affichage = affichage
        ## 
        if self.affichage == "csv":
            self.liste_exercice = []
            # On construit l'onglet Csv
            self.construction_onglet_csv()
        else:
            self.fichier_liste_exercice = join(DATADIR, self.environnement, "onglets", self.affichage+".xml")
            self.liste_exercice = lire_liste_exercice(self.fichier_liste_exercice)
            # On construit les onglets des exercices
            self.construction_onglet_exercice()
        ## On construit l'onglet option
        self.construction_onglet_option()

    ############## Construit l'onglet des exercices
    def construction_onglet_exercice(self):
        ## Initialisation
        self.onglet_exercice_scroll = []
        self.onglet_exercice_widget = []
        self.onglet_exercice_verticalLayout = []
        self.onglet_exercice_gridLayout = []
        self.onglet_exercice_label_categorie = []
        self.onglet_exercice_ligne = []
        self.onglet_exercice_spinBox_nombre = []
        self.onglet_exercice_label_aide = []
        self.onglet_exercice_label_nom = []
        self.onglet_exercice_spinBox_parametre = []
        ## Pour tous les onglets
        for onglet in range(len(self.liste_exercice)):
            ## Creation d'une zone de scroll
            self.onglet_exercice_scroll.append(QtGui.QScrollArea(self.tabWidget))
            self.onglet_exercice_scroll[onglet].setFrameStyle(QtGui.QFrame.StyledPanel)
            self.onglet_exercice_scroll[onglet].setWidgetResizable(True)
            self.tabWidget.addTab(self.onglet_exercice_scroll[onglet], self.liste_exercice[onglet][0])
            ## Creation d'un QWidget
            self.onglet_exercice_widget.append(QtGui.QWidget(self.onglet_exercice_scroll[onglet]))
            self.onglet_exercice_widget[onglet].setStyleSheet(" background-color: rgb(251, 251, 210);")
            self.onglet_exercice_scroll[onglet].setWidget(self.onglet_exercice_widget[onglet])
            ## Creation d'une grille verticale dans le QWidget
            self.onglet_exercice_verticalLayout.append(QtGui.QVBoxLayout(self.onglet_exercice_widget[onglet]))
            ## Initialisation
            self.onglet_exercice_label_categorie.append([])
            self.onglet_exercice_ligne.append([])
            self.onglet_exercice_spinBox_nombre.append([])
            self.onglet_exercice_label_aide.append([])
            self.onglet_exercice_label_nom.append([])
            self.onglet_exercice_spinBox_parametre.append([])
            self.onglet_exercice_gridLayout.append([])
            ## Pour tous les categories
            for categorie in range(len(self.liste_exercice[onglet][1])):     
                ## Initialisation
                self.onglet_exercice_ligne[onglet].append([])
                self.onglet_exercice_spinBox_nombre[onglet].append([])
                self.onglet_exercice_label_aide[onglet].append([])
                self.onglet_exercice_label_nom[onglet].append([])
                self.onglet_exercice_spinBox_parametre[onglet].append([])
                ## Intitulé du categorie
                self.onglet_exercice_label_categorie[onglet].append(QtGui.QLabel(self.onglet_exercice_widget[onglet]))
                self.onglet_exercice_label_categorie[onglet][categorie].setText(u"<center><strong>%s</strong></center>" % self.liste_exercice[onglet][1][categorie][0])
                self.onglet_exercice_verticalLayout[onglet].addWidget(self.onglet_exercice_label_categorie[onglet][categorie])
                ## Creation d'une grille dans le QWidget
                self.onglet_exercice_gridLayout[onglet].append(QtGui.QGridLayout())
                self.onglet_exercice_verticalLayout[onglet].addLayout(self.onglet_exercice_gridLayout[onglet][categorie])
                ## Pour tous les exercices
                for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                    ## Initialisation
                    self.onglet_exercice_spinBox_parametre[onglet][categorie].append([])
                    ## Ligne pour la couleur
                    self.onglet_exercice_ligne[onglet][categorie].append(QtGui.QWidget(self.onglet_exercice_widget[onglet]))
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_ligne[onglet][categorie][exercice], exercice, 1, 1, 20)
                    ## Nombre d'exercice
                    self.onglet_exercice_spinBox_nombre[onglet][categorie].append(QtGui.QSpinBox(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setToolTip(u"Choisissez le nombre d\'exercices de ce type à créer.")
                    self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice], exercice, 1)
                    ## Bulle d'aide
                    self.onglet_exercice_label_aide[onglet][categorie].append(QtGui.QLabel(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_label_aide[onglet][categorie][exercice].setText(r'<img src="%s" />' %  join(DATADIR, 'images','whatsthis.png'))
                    self.onglet_exercice_label_aide[onglet][categorie][exercice].setToolTip(r'<img src="%s" />' % join(DATADIR, 'images', 'vignettes','%s.png' % self.liste_exercice[onglet][1][categorie][1][exercice][2]))
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_label_aide[onglet][categorie][exercice], exercice, 2)
                    ## Intitulé de l'exercice
                    self.onglet_exercice_label_nom[onglet][categorie].append(QtGui.QLabel(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_label_nom[onglet][categorie][exercice].setText(u"%s" % self.liste_exercice[onglet][1][categorie][1][exercice][0])
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_label_nom[onglet][categorie][exercice], exercice, 4)
                    ## Ajout d'une colonne redimensionnable en largeur
                    self.onglet_exercice_gridLayout[onglet][categorie].addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), exercice, 5)
                    ## Mise en couleur pour faire une alternance de ligne claire et fonçée
                    if exercice%2:
                        self.onglet_exercice_ligne[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                        self.onglet_exercice_label_aide[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                        self.onglet_exercice_label_nom[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    else:
                        self.onglet_exercice_ligne[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                        self.onglet_exercice_label_aide[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                        self.onglet_exercice_label_nom[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    ## Pour tous les paramètres
                    for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice].append(QtGui.QSpinBox(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setStyleSheet("background-color: rgb(255, 255, 255);")
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setKeyboardTracking(False) 
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setToolTip(u"%s entre %s et %s." % (self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][0], self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][1], self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][2]))
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setRange(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][1]), int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][2]))
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setValue(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
                         self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre], exercice, 6 + parametre)
            ## Ajout d'une ligne redimensionnable en hauteur
            self.onglet_exercice_verticalLayout[onglet].addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))

    ############## Construit l'onglet des options
    def construction_onglet_option(self):
        ## Creation d'une zone de scroll
        self.onglet_option_scroll = QtGui.QScrollArea(self.tabWidget)
        self.onglet_option_scroll.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.onglet_option_scroll.setWidgetResizable(True)
        self.tabWidget.addTab(self.onglet_option_scroll, "Options")
        ## Creation d'un QWidget
        self.onglet_option_widget = QtGui.QWidget(self.onglet_option_scroll)
        self.onglet_option_widget.setStyleSheet("background-color: rgb(251, 251, 210);")
        self.onglet_option_scroll.setWidget(self.onglet_option_widget)
        ## Creation d'une grille dans le QWidget
        self.onglet_option_gridLayout = QtGui.QGridLayout(self.onglet_option_widget)
        ## Creation d'une grille horizontale dans la grille
        self.onglet_option_horizontalLayout = QtGui.QHBoxLayout()
        self.onglet_option_gridLayout.addLayout(self.onglet_option_horizontalLayout, 0, 0, 1, 2)
        ## Layout pour les noms d'options, en haut à gauche
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout.addLayout(self.verticalLayout_16)
        ## Label nom du fichier
        self.onglet_option_label_nom_fichier = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_nom_fichier.setText(u"Nom par défaut du fichier : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_nom_fichier)
        ## Label chemin par défaut pour l'enregistrement des fichiers
        self.onglet_option_label_chemin_fichier = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_chemin_fichier.setText(u"Chemin pour enregistrer les fichiers : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_chemin_fichier)
        ## Label titre des fiches
        self.onglet_option_label_titre_fiche = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_titre_fiche.setText("Titre de la fiche d'exercices : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_titre_fiche)
        ## Label nom de l'établissement
        self.onglet_option_label_nom_etablissement = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_nom_etablissement.setText(u"Nom de l'établissement : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_nom_etablissement)
        ## Label nom de l'auteur
        self.onglet_option_label_nom_auteur = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_nom_auteur.setText("Nom de l'auteur : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_nom_auteur)
        ## Label temps d'un slide
        self.onglet_option_label_temps_slide = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_temps_slide.setText("Temps par question en seconde : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_temps_slide)
        ## Label date de l'activité mentale
        self.onglet_option_label_date_activite = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_date_activite.setText(u"Date de l\'activité mentale : ")
        self.verticalLayout_16.addWidget(self.onglet_option_label_date_activite)
        ## Label niveau
        self.onglet_option_label_niveau = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_niveau.setText("Niveau :")
        self.verticalLayout_16.addWidget(self.onglet_option_label_niveau)
        ## Layout pour les noms d'options, en haut à droite
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout.addLayout(self.verticalLayout_17)
        ## LineEdit nom du fichier
        self.onglet_option_nom_fichier = QtGui.QLineEdit(self.onglet_option_widget)
        self.onglet_option_nom_fichier.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_option_nom_fichier.setText(self.config['nom_fichier'])
        self.verticalLayout_17.addWidget(self.onglet_option_nom_fichier)
        ## LineEdit chemin par défaut pour l'enregistrement des fichiers
        self.horizontalLayout_chemin = QtGui.QHBoxLayout()
        self.onglet_option_chemin = QtGui.QLineEdit(self.onglet_option_widget)
        self.onglet_option_chemin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_option_chemin.setText(self.config['chemin_fichier'])
        self.horizontalLayout_chemin.addWidget(self.onglet_option_chemin)
        ## Bouton parcourir
        self.onglet_option_pushButton_parcourir_chemin = QtGui.QPushButton(self.onglet_option_widget)
        self.onglet_option_pushButton_parcourir_chemin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.onglet_option_pushButton_parcourir_chemin.setText("Parcourir")
        QtCore.QObject.connect(self.onglet_option_pushButton_parcourir_chemin,QtCore.SIGNAL("clicked()"), self.option_parcourir_chemin)
        self.horizontalLayout_chemin.addWidget(self.onglet_option_pushButton_parcourir_chemin)
        self.verticalLayout_17.addLayout(self.horizontalLayout_chemin)
        ## LineEdit titre des fiches
        self.titre_fiche = QtGui.QLineEdit(self.onglet_option_widget)
        self.titre_fiche.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titre_fiche.setText(self.config['titre_fiche'])
        self.verticalLayout_17.addWidget(self.titre_fiche)
        ## LineEdit nom de l'établissement
        self.nom_etablissement = QtGui.QLineEdit(self.onglet_option_widget)
        self.nom_etablissement.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nom_etablissement.setText(self.config['nom_etablissement'])
        self.verticalLayout_17.addWidget(self.nom_etablissement)
        ## LineEdit nom de l'auteur
        self.nom_auteur = QtGui.QLineEdit(self.onglet_option_widget)
        self.nom_auteur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nom_auteur.setText(self.config['nom_auteur'])
        self.verticalLayout_17.addWidget(self.nom_auteur)
        ## LineEdit temps d'un slide
        self.temps_slide = QtGui.QLineEdit(self.onglet_option_widget)
        self.temps_slide.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temps_slide.setText(self.config['temps_slide'])
        self.verticalLayout_17.addWidget(self.temps_slide)
        ## LineEdit date de l'activité mentale
        self.date_activite = QtGui.QLineEdit(self.onglet_option_widget)
        self.date_activite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_activite.setText(strftime('%A %d %B %Y',localtime()) )
        self.verticalLayout_17.addWidget(self.date_activite)
        ## ComboBox niveau
        self.comboBox_niveau = QtGui.QComboBox(self.onglet_option_widget)
        self.comboBox_niveau.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_niveau.setEditable(True)
        self.comboBox_niveau.addItem(u"Sixième")
        self.comboBox_niveau.addItem(u"Cinquième")
        self.comboBox_niveau.addItem(u"Quatrième")
        self.comboBox_niveau.addItem(u"Troisième")
        self.verticalLayout_17.addWidget(self.comboBox_niveau)
        ## Ligne de séparation
        self.line = QtGui.QFrame(self.onglet_option_widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.onglet_option_gridLayout.addWidget(self.line, 1, 0, 1, 2)
        ## 
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.onglet_option_gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        ## 
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.horizontalLayout_3.addLayout(self.verticalLayout_21)
        ## CheckBox "présentation sujet ou non"
        self.checkBox_sujet_presentation = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_sujet_presentation.setText(u"Créer le sujet (présentation)")
        self.checkBox_sujet_presentation.setToolTip(u"Actimaths doit-il créer le sujet sous forme de présentation ?")
        self.checkBox_sujet_presentation.setChecked(int(self.config['sujet_presentation']))
        self.verticalLayout_21.addWidget(self.checkBox_sujet_presentation)
        ## CheckBox "présentation corrigés ou non"
        self.checkBox_corrige_presentation = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_corrige_presentation.setText(u"Créer le corrigé (présentation)")
        self.checkBox_corrige_presentation.setToolTip(u"Actimaths doit-il créer le corrigé sous forme de présentation ?")
        self.checkBox_corrige_presentation.setChecked(int(self.config['corrige_presentation']))
        self.verticalLayout_21.addWidget(self.checkBox_corrige_presentation)
        ## Pas de presentation dans l'environnement pyromaths
        if self.environnement == 'pyromaths':
            self.checkBox_sujet_presentation.setChecked(False)
            self.checkBox_sujet_presentation.setEnabled(False)
            self.checkBox_corrige_presentation.setChecked(False)
            self.checkBox_corrige_presentation.setEnabled(False)
        ## CheckBox "page sujet ou non"
        self.checkBox_sujet_page = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_sujet_page.setText(u"Créer le sujet (page)")
        self.checkBox_sujet_page.setToolTip(u"Actimaths doit-il créer le sujet sous forme de page ?")
        self.checkBox_sujet_page.setChecked(int(self.config['sujet_page']))
        self.verticalLayout_21.addWidget(self.checkBox_sujet_page)
        ## CheckBox "page corrigés ou non"
        self.checkBox_corrige_page = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_corrige_page.setText(u"Créer le corrigé (page)")
        self.checkBox_corrige_page.setToolTip(u"Actimaths doit-il créer le corrigé sous forme de page ?")
        self.checkBox_corrige_page.setChecked(int(self.config['corrige_page']))
        self.verticalLayout_21.addWidget(self.checkBox_corrige_page)
        ## Espace
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        ##
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.horizontalLayout_3.addLayout(self.verticalLayout_20)
        ##
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.verticalLayout_20.addLayout(self.horizontalLayout_2)
        ##
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.horizontalLayout_2.addLayout(self.verticalLayout_18)
        ## Label Modèle de présentation
        self.label_modele_presentation = QtGui.QLabel(self.onglet_option_widget)
        self.label_modele_presentation.setText(u"Modèle de présentation :")
        self.verticalLayout_18.addWidget(self.label_modele_presentation)
        ## Label Modèle de mise en page
        self.label_modele_page = QtGui.QLabel(self.onglet_option_widget)
        self.label_modele_page.setText(u"Modèle de page :")
        self.verticalLayout_18.addWidget(self.label_modele_page)
        ## Layout pour les noms d'options, en bas à droite
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.horizontalLayout_2.addLayout(self.verticalLayout_19)
        ## ComboBox modèles de présentation
        self.comboBox_modele_presentation = QtGui.QComboBox(self.onglet_option_widget)
        self.comboBox_modele_presentation.setStyleSheet("background-color: rgb(255, 255, 255);")
        modeles_presentation = []
        for fichier in listdir(join(DATADIR, self.environnement, 'modeles','presentation')):
            if isdir(join(join(DATADIR, self.environnement, 'modeles','presentation', fichier))):
                modeles_presentation.append(fichier)

        for i in range(len(modeles_presentation)):
            self.comboBox_modele_presentation.addItem(str(modeles_presentation[i]))
            if modeles_presentation[i] == self.config['modele_presentation']:
                self.comboBox_modele_presentation.setCurrentIndex(i)
        self.verticalLayout_19.addWidget(self.comboBox_modele_presentation)
        ## ComboBox modèles de page papier
        self.comboBox_modele_page = QtGui.QComboBox(self.onglet_option_widget)
        self.comboBox_modele_page.setStyleSheet("background-color: rgb(255, 255, 255);")
        modeles_page = []
        for fichier in listdir(join(DATADIR, self.environnement, 'modeles', 'page')):
            if isdir(join(join(DATADIR, self.environnement,'modeles', 'page', fichier))):
                modeles_page.append(fichier)

        for i in range(len(modeles_page)):
            self.comboBox_modele_page.addItem(str(modeles_page[i]))
            if modeles_page[i] == self.config['modele_page']:
                self.comboBox_modele_page.setCurrentIndex(i)
        self.verticalLayout_19.addWidget(self.comboBox_modele_page)
        ## Bouton enregistrer
        self.pushButton_enr_opt = QtGui.QPushButton(self.onglet_option_widget)
        self.pushButton_enr_opt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.pushButton_enr_opt.setText(u"Enregistrer dans les préférences")
        QtCore.QObject.connect(self.pushButton_enr_opt,QtCore.SIGNAL("clicked()"), self.enregistrer_config)
        self.onglet_option_gridLayout.addWidget(self.pushButton_enr_opt, 4, 1, 1, 1)
        ## 
        spacerItem14 = QtGui.QSpacerItem(20, 177, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.onglet_option_gridLayout.addItem(spacerItem14, 3, 1, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.onglet_option_gridLayout.addItem(spacerItem15, 4, 0, 1, 1)

    ############## Construit l'onglet csv
    def construction_onglet_csv(self):
        ## Creation d'une zone de scroll
        self.onglet_csv_scroll = QtGui.QScrollArea(self.tabWidget)
        self.onglet_csv_scroll.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.onglet_csv_scroll.setWidgetResizable(True)
        self.tabWidget.addTab(self.onglet_csv_scroll, "CSV")
        ## Creation d'un QWidget
        self.onglet_csv_widget = QtGui.QWidget(self.onglet_csv_scroll)
        self.onglet_csv_widget.setStyleSheet("background-color: rgb(251, 251, 210);")
        self.onglet_csv_scroll.setWidget(self.onglet_csv_widget)
        ## Creation d'une grille dans le QWidget
        self.onglet_csv_verticalLayout = QtGui.QVBoxLayout(self.onglet_csv_widget)
        ## Label chemin par défaut pour l'enregistrement des fichiers
        self.onglet_csv_horizontalLayout_chemin = QtGui.QHBoxLayout()
        self.onglet_csv_label_chemin = QtGui.QLabel(self.onglet_csv_widget)
        self.onglet_csv_label_chemin.setText(u"Chemin du fichier .csv : ")
        self.onglet_csv_horizontalLayout_chemin.addWidget(self.onglet_csv_label_chemin)
        ## LineEdit chemin du fichier csv
        self.onglet_csv_chemin = QtGui.QLineEdit(self.onglet_csv_widget)
        self.onglet_csv_chemin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_csv_chemin.setText(self.config['chemin_csv'])
        self.onglet_csv_horizontalLayout_chemin.addWidget(self.onglet_csv_chemin)
        ## Bouton parcourir du fichier csv
        self.onglet_csv_pushButton_parcourir_csv = QtGui.QPushButton(self.onglet_csv_widget)
        self.onglet_csv_pushButton_parcourir_csv.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.onglet_csv_pushButton_parcourir_csv.setText("Parcourir")
        QtCore.QObject.connect(self.onglet_csv_pushButton_parcourir_csv,QtCore.SIGNAL("clicked()"), self.option_parcourir_csv)
        self.onglet_csv_horizontalLayout_chemin.addWidget(self.onglet_csv_pushButton_parcourir_csv)
        self.onglet_csv_verticalLayout.addLayout(self.onglet_csv_horizontalLayout_chemin)

    ############## Crée la boîte de dialogue "À propos de...
    def about(self):
        text = u"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
                   <html>
                   <body>
                   <p> <span style="font-weight:600;">Version :</span> %s </p>
                   <p> <span style=" font-weight:600;">Description :</span> %s </p>
                   <p> <span style=" font-weight:600;">Remerciements :</span> </p>
                   <ul>
                   %s
                   </ul>
                   <p> <span style=" font-weight:600;">Crédit:</span> %s </p>
                   </body>
                   </html>"""
        credits = "\n"
        for nom in CREDITS:
            credits += "<li>" + nom + "</li>" + "\n"
        QtGui.QMessageBox.about(self.centralwidget, u'À propos de Actimaths', text % (VERSION, DESCRIPTION, credits, COPYRIGHTS))

    ############## Ouvre le navigateur internet par défaut sur la page d'aide en ligne du site d'Actimaths
    def site(self):
        import webbrowser
        webbrowser.open(WEBSITE)

    ###============================================================
    ###   Fonctions diverses
    ###============================================================
    ############## Remet toutes les SpinBox à zéro et vide la liste d'exercices sélectionnés
    def effacer_choix_exercices(self):
        self.liste_creation=[]
        for onglet in range(len(self.liste_exercice)):
            for categorie in range(len(self.liste_exercice[onglet][1])):
                for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                    self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setValue(0)
                    for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                        self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setValue(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))

    ############## Modifie le chemin d'enregistrement des fiches
    def option_parcourir_chemin(self):
        chemin = unicode(QtGui.QFileDialog().getExistingDirectory (self.centralwidget, u"Dossier où créer les fiches", unicode(self.onglet_option_chemin.text()), QtGui.QFileDialog.ShowDirsOnly))
        if chemin:
            self.onglet_option_chemin.setText(chemin)

    ############## Modifie le chemin vers le fichier csv
    def option_parcourir_csv(self):
        chemin_csv = unicode(QtGui.QFileDialog().getOpenFileName(self.centralwidget, 'Fichier .csv',  unicode(self.onglet_option_chemin.text()), "Documents csv (*.csv)"))
        if chemin_csv:
            self.onglet_csv_chemin.setText(chemin_csv)

    ############## Créé la liste d'exercice
    def valide_choix_exercices(self):
        self.liste_creation = []
        for onglet in range(len(self.liste_exercice)):
            for categorie in range(len(self.liste_exercice[onglet][1])):
                for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                    nombre_exercice = self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].value()
                    commande = self.liste_exercice[onglet][1][categorie][1][exercice][2]
                    valeur_parametre = []
                    for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                        valeur_parametre.append(self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].value())
                    for i in range(nombre_exercice):
                        self.liste_creation.append((commande, valeur_parametre))

    ###========================================================================
    ### Fonctions de gestion du fichier de configuration
    ###========================================================================
    ############## Fonction qui se charge d'enregistrer les options de l'interface dans le fichier de configuration après avoir complété le dictionnaire.
    def enregistrer_config(self):
        tree = etree.parse(self.fichier_configuration)
        root = tree.getroot()
        options = root.find('options')
        options .find('nom_fichier').text = unicode(self.onglet_option_nom_fichier.text())
        options .find('chemin_fichier').text = unicode(self.onglet_option_chemin.text())
        options .find('titre_fiche').text = unicode(self.titre_fiche.text())
        options .find('nom_etablissement').text = unicode(self.nom_etablissement.text())
        options .find('nom_auteur').text = unicode(self.nom_auteur.text())
        options .find('temps_slide').text = unicode(self.temps_slide.text())
        options .find('sujet_presentation').text  = str(self.checkBox_sujet_presentation.isChecked())
        options .find('corrige_presentation').text = str(self.checkBox_corrige_presentation.isChecked())
        options .find('sujet_page').text  = str(self.checkBox_sujet_page.isChecked())
        options .find('corrige_page').text = str(self.checkBox_corrige_page.isChecked())
        options .find('modele_presentation').text = unicode(self.comboBox_modele_presentation.currentText())
        options .find('modele_page').text = unicode(self.comboBox_modele_page.currentText())
        options .find('environnement').text = self.environnement
        options .find('affichage').text = self.affichage
        f = open(self.fichier_configuration, encoding='utf-8', mode='w')
        f.write(etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True).decode('utf-8', 'strict'))
        f.close()

    ###========================================================================
    ### Fonction de création des exercices
    ###========================================================================
    ############## Fonction créant des fiches exemples pour tous les niveaux avec tous les exercices
    def creer_tous_les_exercices(self):
        ## synchronisation des paramètres
        parametres = {'sujet_presentation': self.checkBox_sujet_presentation.isChecked(),
                      'corrige_presentation': self.checkBox_corrige_presentation.isChecked(),
                      'sujet_page': self.checkBox_sujet_page.isChecked(),
                      'corrige_page': self.checkBox_corrige_page.isChecked(),
                      'titre': unicode(self.titre_fiche.text()),
                      'nom_etablissement': unicode(self.nom_etablissement.text()),
                      'nom_auteur': unicode(self.nom_auteur.text()),
                      'temps_slide': unicode(self.temps_slide.text()),
                      'date_activite': unicode(self.date_activite.text()),
                      'niveau': unicode(self.comboBox_niveau.currentText()),
                      'nom_fichier': unicode(self.onglet_option_nom_fichier.text()),
                      'chemin_fichier': unicode(self.onglet_option_chemin.text()),
                      'environnement': self.environnement,
                      'affichage': self.affichage,
                      'modele_presentation': unicode(self.comboBox_modele_presentation.currentText()),
                      'modele_page': unicode(self.comboBox_modele_page.currentText())}
        ## Creation
        if self.affichage == "csv":
            QtGui.QMessageBox.warning(self.centralwidget, 'Attention !', u"Impossible de créer tous les exercices dans le mode CSV.", QtGui.QMessageBox.Ok ) 
        else:
            # Création de la liste contenant tous les exercices de l'environnement
            self.liste_creation = []
            for onglet in range(len(self.liste_exercice)):
                for categorie in range(len(self.liste_exercice[onglet][1])):
                    for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                        valeur_parametre = []
                        commande = self.liste_exercice[onglet][1][categorie][1][exercice][2]
                        for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                            valeur_parametre.append(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
                        self.liste_creation.append((commande, valeur_parametre))
            parametres ['liste_exos'] = self.liste_creation
            parametres ['chemin_csv'] = ""
            creation_exercice = Thread(None, creation, "creation_exercice", (parametres, ), None)
            creation_exercice.start()

    ############## Fonction créant des fiches à partir de la liste d'exercices
    def creer_les_exercices(self):
        ## synchronisation des paramètres
        parametres = {'sujet_presentation': self.checkBox_sujet_presentation.isChecked(),
                      'corrige_presentation': self.checkBox_corrige_presentation.isChecked(),
                      'sujet_page': self.checkBox_sujet_page.isChecked(),
                      'corrige_page': self.checkBox_corrige_page.isChecked(),
                      'titre': unicode(self.titre_fiche.text()),
                      'nom_etablissement': unicode(self.nom_etablissement.text()),
                      'nom_auteur': unicode(self.nom_auteur.text()),
                      'temps_slide': unicode(self.temps_slide.text()),
                      'date_activite': unicode(self.date_activite.text()),
                      'niveau': unicode(self.comboBox_niveau.currentText()),
                      'nom_fichier': unicode(self.onglet_option_nom_fichier.text()),
                      'chemin_fichier': unicode(self.onglet_option_chemin.text()),
                      'environnement': self.environnement,
                      'affichage': self.affichage,
                      'modele_presentation': unicode(self.comboBox_modele_presentation.currentText()),
                      'modele_page': unicode(self.comboBox_modele_page.currentText())}
        ## Creation
        if self.affichage == "csv":
            # Test de l'existence du fichier
            if not(isfile(unicode(self.onglet_csv_chemin.text()))):
                QtGui.QMessageBox.warning(self.centralwidget, 'Attention !', u"Fichier csv non valide.", QtGui.QMessageBox.Ok ) 
            else:
                parametres ['liste_exos'] = []
                parametres ['chemin_csv'] = unicode(self.onglet_csv_chemin.text())
                creation_exercice = Thread(None, creation, "creation_exercice", (parametres, ), None)
                creation_exercice.start()
        else:
            # Création de la liste d'exercices
            self.valide_choix_exercices()
            # Test de l'existence de la liste
            if self.liste_creation == []:
                QtGui.QMessageBox.warning(self.centralwidget, 'Attention !', u"Veuillez sélectionner des exercices...", QtGui.QMessageBox.Ok )    
            else:
                parametres ['liste_exos'] = self.liste_creation
                parametres ['chemin_csv'] = ""
                creation_exercice = Thread(None, creation, "creation_exercice", (parametres, ), None)
                creation_exercice.start()
