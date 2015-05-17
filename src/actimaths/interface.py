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
from os import listdir
from os.path import join, isfile, isdir, splitext
from PyQt4 import QtGui, QtCore
from codecs import open
from lxml import etree
from lxml import _elementpath as DONTUSE # Astuce pour inclure lxml dans Py2exe
from datetime import date, timedelta
from sip import delete
from functools import partial
from locale import setlocale, LC_TIME

## On utilise le pays de l'utilisateur (pour la date)
setlocale(LC_TIME,"")

## Import spécifique à Actimaths
from system import lire_config, lire_liste_exercice
from values import CONFIGDIR, COPYRIGHTS, VERSION, WEBSITE, DESCRIPTION, CREDITS, DATADIR
from exercices import creation

###========================================================================
### Class MainWindow
###========================================================================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #============================================================
        #        Initialisation
        #============================================================
        ## Lecture du fichier de configuration
        self.fichier_configuration = join(CONFIGDIR,  "actimaths.xml")
        self.config = lire_config(self.fichier_configuration)
        ## Fenètre principale
        MainWindow.setWindowIcon(QtGui.QIcon(join(DATADIR, "images","actimaths.png")))
        MainWindow.setWindowTitle("Actimaths")
        MainWindow.setGeometry(0, 44, 1100, 700)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        ## Widget principal
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        ## Grille principale
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)

        #============================================================
        #        Boutons créer, selectionner et reinitialiser
        #============================================================
        ## Conteneur vertical
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(9)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        ## Bouton Créer
        self.bouton_creer = QtGui.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.bouton_creer)
        self.bouton_creer.setText(u"Créer")
        self.bouton_creer.setToolTip(u"Créer les exercices de la liste de sélection")
        self.bouton_creer.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(46, 139, 87, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.connect(self.bouton_creer,QtCore.SIGNAL("clicked()"), self.creer_exercices)
        ## Bouton Sélectionner
        self.bouton_selectionner = QtGui.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.bouton_selectionner)
        self.bouton_selectionner.setText(u"Sélectionner")
        self.bouton_selectionner.setToolTip(u"Créer la liste de sélection")
        self.bouton_selectionner.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(51, 51, 255, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.connect(self.bouton_selectionner,QtCore.SIGNAL("clicked()"), self.actualiser_onglet_selection)
        ## Bouton Réinitialiser
        self.bouton_reinitialiser = QtGui.QPushButton(self.centralwidget)
        self.verticalLayout.addWidget(self.bouton_reinitialiser)
        self.bouton_reinitialiser.setText(u"Réinitialiser")
        self.bouton_reinitialiser.setToolTip(u"Réinitialise l'interface")
        self.bouton_reinitialiser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 105, 180, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.connect(self.bouton_reinitialiser, QtCore.SIGNAL("clicked()"), self.reinitialiser_onglet)
        ## Espace Vertical
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        #============================================================
        #        Onglets de la zone centrale
        #============================================================
        ## Construction d'une zone d'onglet
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        ## Construction des onglets
        self.construction_onglet(self.config["environnement"],self.config["affichage"])

        #============================================================
        #        Barre de menus
        #============================================================
        ## Construction de la barre
        self.barre_menu = QtGui.QMenuBar(MainWindow)
        self.barre_menu.setGeometry(QtCore.QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.barre_menu)
        ## Menu Fichier
        self.barre_menu_fichier = QtGui.QMenu(self.barre_menu)
        self.barre_menu_fichier.setTitle("Fichier")
        ## Action Tous les Exercices 
        self.barre_menu_fichier_tous_les_exercices = QtGui.QAction(MainWindow)
        self.barre_menu_fichier_tous_les_exercices.setText("Choisir tous les exercices")
        self.barre_menu_fichier_tous_les_exercices.setShortcut("Ctrl+A")
        QtCore.QObject.connect(self.barre_menu_fichier_tous_les_exercices, QtCore.SIGNAL("triggered()"), self.choisir_tous_les_exercices)
        ## Action Quitter
        self.barre_menu_fichier_quitter = QtGui.QAction(MainWindow)
        self.barre_menu_fichier_quitter.setText("Quitter")
        self.barre_menu_fichier_quitter.setShortcut("Ctrl+Q")
        QtCore.QObject.connect(self.barre_menu_fichier_quitter, QtCore.SIGNAL("triggered()"), QtGui.qApp, QtCore.SLOT("quit()"))
        ## Construction du menu fichier
        self.barre_menu_fichier.addAction(self.barre_menu_fichier_tous_les_exercices)
        self.barre_menu_fichier.addAction(self.barre_menu_fichier_quitter)
        self.barre_menu.addAction(self.barre_menu_fichier.menuAction())
        ## Menu Environnement
        self.barre_menu_environnement = QtGui.QMenu(self.barre_menu)
        self.barre_menu_environnement.setTitle(u"Environnement")
        ## Action Actimaths
        self.barre_menu_environnement_actimaths = QtGui.QAction(MainWindow)
        self.barre_menu_environnement_actimaths.setText("Actimaths")
        QtCore.QObject.connect(self.barre_menu_environnement_actimaths, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet("actimaths", self.affichage))
        ## Action Pyromaths
        self.barre_menu_environnement_pyromaths = QtGui.QAction(MainWindow)
        self.barre_menu_environnement_pyromaths.setText("Pyromaths")
        QtCore.QObject.connect(self.barre_menu_environnement_pyromaths, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet("pyromaths", self.affichage))
        ## Construction du menu Environnement
        self.barre_menu_environnement.addAction(self.barre_menu_environnement_actimaths)
        self.barre_menu_environnement.addAction(self.barre_menu_environnement_pyromaths)
        self.barre_menu.addAction(self.barre_menu_environnement.menuAction())
        ## Menu Présentation
        self.barre_menu_affichage = QtGui.QMenu(self.barre_menu)
        self.barre_menu_affichage.setTitle(u"Affichage")
        ## Action Par niveaux
        self.barre_menu_affichage_niveau = QtGui.QAction(MainWindow)
        self.barre_menu_affichage_niveau.setText("Par niveau")
        QtCore.QObject.connect(self.barre_menu_affichage_niveau, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet(self.environnement, "niveau"))
        ## Action Par domaine
        self.barre_menu_affichage_domaine = QtGui.QAction(MainWindow)
        self.barre_menu_affichage_domaine.setText("Par domaine")
        QtCore.QObject.connect(self.barre_menu_affichage_domaine, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet(self.environnement, "domaine"))
        ## Action CSV
        self.barre_menu_affichage_csv = QtGui.QAction(MainWindow)
        self.barre_menu_affichage_csv.setText("Csv")
        QtCore.QObject.connect(self.barre_menu_affichage_csv, QtCore.SIGNAL("triggered()"), lambda: self.construction_onglet(self.environnement, "csv"))
        ## Construction du menu Affichage
        self.barre_menu_affichage.addAction(self.barre_menu_affichage_niveau)
        self.barre_menu_affichage.addAction(self.barre_menu_affichage_domaine)
        self.barre_menu_affichage.addAction(self.barre_menu_affichage_csv)
        self.barre_menu.addAction(self.barre_menu_affichage.menuAction())
        ## Menu Aide
        self.barre_menu_aide = QtGui.QMenu(self.barre_menu)
        self.barre_menu_aide.setTitle("Aide")
        ## Action Aide en ligne
        self.barre_menu_aide_web = QtGui.QAction(MainWindow)
        self.barre_menu_aide_web.setText(u"Aide en ligne")
        QtCore.QObject.connect(self.barre_menu_aide_web, QtCore.SIGNAL("triggered()"), self.site)
        ## Action À propos
        self.barre_menu_aide_a_propos = QtGui.QAction(MainWindow)
        self.barre_menu_aide_a_propos.setText(u"À propos")
        QtCore.QObject.connect(self.barre_menu_aide_a_propos, QtCore.SIGNAL("triggered()"), self.about)
        ## Construction du menu Aide
        self.barre_menu_aide.addAction(self.barre_menu_aide_web)
        self.barre_menu_aide.addAction(self.barre_menu_aide_a_propos)
        self.barre_menu.addAction(self.barre_menu_aide.menuAction())

        #============================================================
        #        Barre d'état
        #============================================================
        ## Construction de la barre d'état
        self.barre_etat = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.barre_etat)
        ## Barre d'avancement
        self.barre_etat_progressBar = QtGui.QProgressBar(self.barre_etat)
        self.barre_etat_progressBar.setRange(0,0)
        self.barre_etat_progressBar.setVisible(False)
        self.barre_etat.addWidget(self.barre_etat_progressBar)
        ## Message d'aide
        self.barre_etat_label= QtGui.QLabel(self.barre_etat)
        self.barre_etat_label.setText(u"En attente...")
        self.barre_etat.addWidget(self.barre_etat_label,1)

    ###============================================================
    ###   Fonctions d'interface
    ###============================================================
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
                   <p> <span style=" font-weight:600;">Crédit :</span> %s </p>
                   </body>
                   </html>"""
        credits = "\n"
        for nom in CREDITS:
            credits += "<li>" + nom + "</li>" + "\n"
        QtGui.QMessageBox.about(self.centralwidget, u"À propos de Actimaths", text % (VERSION, DESCRIPTION, credits, COPYRIGHTS))

    ############## Ouvre le navigateur internet par défaut sur la page d'aide en ligne du site d'Actimaths
    def site(self):
        import webbrowser
        webbrowser.open(WEBSITE)

    ############## Remet les valeurs des SpinBox initiales
    def reinitialiser_onglet(self):
        ## On supprime le contenu de l'onglet sélection
        delete(self.onglet_selection_widget)
        self.onglet_selection_widget = None
        ## On vide la liste de sélection
        self.liste_exercice_selectionner = []
        ## initialisation de l'onglet selection
        self.initialisation_onglet_selection()
        ## réinitialisation des onglets exercices
        for onglet in range(len(self.liste_exercice)):
            for categorie in range(len(self.liste_exercice[onglet][1])):
                for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                    self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setValue(0)
                    self.onglet_exercice_spinBox_temps[onglet][categorie][exercice].setValue(int(self.liste_exercice[onglet][1][categorie][1][exercice][3]))
                    for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                        self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setValue(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
        ## Mise à jour du message de la barre d'état
        self.barre_etat_label.setText(u"Réinitialiser. En attente...")

    ############## Crée des fiches exemples pour tous les niveaux avec tous les exercices
    def choisir_tous_les_exercices(self):
        ## Creation
        if self.affichage == "csv":
            QtGui.QMessageBox.warning(self.centralwidget, "Attention !", u"Il n'a pas d'exercices à choisir pour l'affichage CSV.", QtGui.QMessageBox.Ok ) 
        else:
            # On choisit tous les exercices
            for onglet in range(len(self.liste_exercice)):
                for categorie in range(len(self.liste_exercice[onglet][1])):
                    for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                        self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setValue(1)

    ############## Cache la progressbar et le bouton d'annulation. Affiche le message de succes
    def tache_terminee(self):
        ## Masquer la progressBar
        self.barre_etat_progressBar.setVisible(False)
        ## Le bouton Annuler devient Creer
        self.bouton_creer.setText(u"Créer")
        self.bouton_creer.setToolTip(u"Créer les exercices de la liste de sélection")
        self.bouton_creer.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(46, 139, 87, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.disconnect(self.bouton_creer, QtCore.SIGNAL("clicked()"), self.annuler_tache)
        QtCore.QObject.connect(self.bouton_creer,QtCore.SIGNAL("clicked()"), self.creer_exercices)
        ## Mise à jour du message de la barre d'état
        self.barre_etat_label.setText(u"Création des exercices terminée. En attente...")

    ############## Cache la progressbar et le bouton d'annulation. Affiche le message d'annulation
    def tache_annulee(self):
        ## Masquer la progressBar
        self.barre_etat_progressBar.setVisible(False)
        ## Le bouton Annuler devient Creer
        self.bouton_creer.setText(u"Créer")
        self.bouton_creer.setToolTip(u"Créer les exercices de la liste de sélection")
        self.bouton_creer.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(46, 139, 87, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.disconnect(self.bouton_creer, QtCore.SIGNAL("clicked()"), self.annuler_tache)
        QtCore.QObject.connect(self.bouton_creer,QtCore.SIGNAL("clicked()"), self.creer_exercices)
        ## Mise à jour du message de la barre d'état
        self.barre_etat_label.setText(u"Création des exercices annulée. En attente...")

    ############## Construit les onglets
    def construction_onglet(self, environnement, affichage):
        ## On supprime tous les onglets et on les supprime pour recuperer la memoire
        self.tabWidget.clear()
        delete(self.tabWidget)
        self.tabWidget = None
        ## On reconstruit les onglets
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        ## On met à jour dans la configuration l'environnement et l'affichage
        self.environnement = environnement
        self.affichage = affichage
        ## Construction des onglets selon l'affichage
        if self.affichage == "csv":
            # On désactive les boutons sélectionner et réinitialiser
            self.bouton_selectionner.setEnabled(False)
            self.bouton_reinitialiser.setEnabled(False)
            # On vide la liste d'exercice
            self.liste_exercice = []
            # On construit l'onglet Csv
            self.construction_onglet_csv()
        else:
            # On désactive les boutons sélectionner et réinitialiser
            self.bouton_selectionner.setEnabled(True)
            self.bouton_reinitialiser.setEnabled(True)
            # On remplit la liste d'exercice
            self.fichier_liste_exercice = join(DATADIR,"onglets", self.environnement, "%s.xml" %self.affichage)
            self.liste_exercice = lire_liste_exercice(self.fichier_liste_exercice)
            # On construit les onglets des exercices
            self.construction_onglet_exercice()
            ## On construit les onglets des exercices sélectionnés
            self.construction_onglet_selection()
        ## On construit l'onglet options
        self.construction_onglet_option()

    ###========================================================================
    ### Fonctions des onglets Exercices
    ###========================================================================
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
        self.onglet_exercice_spinBox_temps = []
        self.onglet_exercice_spinBox_parametre = []
        self.onglet_exercice_label_aide = []
        self.onglet_exercice_label_nom = []
        self.onglet_exercice_label_nombre = []
        self.onglet_exercice_label_temps = []
        self.onglet_exercice_label_parametre = []
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
            self.onglet_exercice_ligne.append([])
            self.onglet_exercice_label_categorie.append([])
            self.onglet_exercice_spinBox_nombre.append([])
            self.onglet_exercice_spinBox_temps.append([])
            self.onglet_exercice_spinBox_parametre.append([])
            self.onglet_exercice_label_aide.append([])
            self.onglet_exercice_label_nom.append([])
            self.onglet_exercice_label_nombre.append([])
            self.onglet_exercice_label_temps.append([])
            self.onglet_exercice_label_parametre.append([])
            self.onglet_exercice_gridLayout.append([])
            ## Pour tous les categories
            for categorie in range(len(self.liste_exercice[onglet][1])):     
                ## Initialisation
                self.onglet_exercice_ligne[onglet].append([])
                self.onglet_exercice_spinBox_nombre[onglet].append([])
                self.onglet_exercice_spinBox_temps[onglet].append([])
                self.onglet_exercice_spinBox_parametre[onglet].append([])
                self.onglet_exercice_label_aide[onglet].append([])
                self.onglet_exercice_label_nom[onglet].append([])
                self.onglet_exercice_label_nombre[onglet].append([])
                self.onglet_exercice_label_temps[onglet].append([])
                self.onglet_exercice_label_parametre[onglet].append([])
                ## Intitulé de la categorie
                self.onglet_exercice_label_categorie[onglet].append(QtGui.QLabel(self.onglet_exercice_widget[onglet]))
                self.onglet_exercice_label_categorie[onglet][categorie].setText(u"%s" % self.liste_exercice[onglet][1][categorie][0])
                self.onglet_exercice_label_categorie[onglet][categorie].setStyleSheet("font: bold 20px; qproperty-alignment: AlignCenter")
                if len(self.liste_exercice[onglet][1][categorie][1]) == 0:
                    self.onglet_exercice_label_categorie[onglet][categorie].setVisible(False)
                self.onglet_exercice_verticalLayout[onglet].addWidget(self.onglet_exercice_label_categorie[onglet][categorie])
                ## Creation d'une grille dans le QWidget
                self.onglet_exercice_gridLayout[onglet].append(QtGui.QGridLayout())
                self.onglet_exercice_gridLayout[onglet][categorie].setColumnMinimumWidth(6, 100)
                self.onglet_exercice_gridLayout[onglet][categorie].setColumnMinimumWidth(9, 100)
                self.onglet_exercice_gridLayout[onglet][categorie].setColumnMinimumWidth(10, 100)
                self.onglet_exercice_verticalLayout[onglet].addLayout(self.onglet_exercice_gridLayout[onglet][categorie])
                ## Pour tous les exercices
                for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                    ## Initialisation
                    self.onglet_exercice_spinBox_parametre[onglet][categorie].append([])
                    ## Ligne pour la couleur
                    self.onglet_exercice_ligne[onglet][categorie].append(QtGui.QWidget(self.onglet_exercice_widget[onglet]))
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_ligne[onglet][categorie][exercice], 2*exercice, 1, 2, 11)
                    ## Nombre d'exercice
                    self.onglet_exercice_spinBox_nombre[onglet][categorie].append(QtGui.QSpinBox(self.onglet_exercice_widget[onglet]))
                    self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setToolTip(u"Choisissez le nombre d\'exercices de ce type à créer.")
                    self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice], 2*exercice, 1, 2, 1)
                    ## Ajout d'une colonne redimensionnable en largeur
                    self.onglet_exercice_gridLayout[onglet][categorie].addItem(QtGui.QSpacerItem(20, 20), 2*exercice, 2, 2, 1)
                    ## Vignette
                    self.onglet_exercice_label_aide[onglet][categorie].append(QtGui.QLabel(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_label_aide[onglet][categorie][exercice].setText(r'<img src="%s" />' %  join(DATADIR, "vignettes" ,"%s" % self.environnement,"%s.jpg" % self.liste_exercice[onglet][1][categorie][1][exercice][2]))
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_label_aide[onglet][categorie][exercice], 2*exercice, 3, 2, 1)
                    ## Ajout d'une colonne redimensionnable en largeur
                    self.onglet_exercice_gridLayout[onglet][categorie].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), 2*exercice, 4, 2, 1)
                    ## Intitulé de l'exercice
                    self.onglet_exercice_label_nom[onglet][categorie].append(QtGui.QLabel(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_label_nom[onglet][categorie][exercice].setText(u"<center><strong>%s</strong></center>" % self.liste_exercice[onglet][1][categorie][1][exercice][0])
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_label_nom[onglet][categorie][exercice], 2*exercice, 4,1,8)
                    ## Label temps de l'exercice
                    self.onglet_exercice_label_temps[onglet][categorie].append(QtGui.QLabel(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_label_temps[onglet][categorie][exercice].setText(u"<u>Temps</u> :" )
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_label_temps[onglet][categorie][exercice], 2*exercice+1, 5)
                    ## Temps de l'exercice
                    self.onglet_exercice_spinBox_temps[onglet][categorie].append(QtGui.QSpinBox(self.onglet_exercice_widget[onglet]))
                    self.onglet_exercice_spinBox_temps[onglet][categorie][exercice].setToolTip(u"Choisissez le temps par slide entre 5 secondes et 90 secondes.")
                    self.onglet_exercice_spinBox_temps[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.onglet_exercice_spinBox_temps[onglet][categorie][exercice].setRange(5,90)
                    self.onglet_exercice_spinBox_temps[onglet][categorie][exercice].setValue(int(self.liste_exercice[onglet][1][categorie][1][exercice][3]))
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_spinBox_temps[onglet][categorie][exercice], 2*exercice+1, 6)
                    ## Ajout d'une colonne redimensionnable en largeur
                    self.onglet_exercice_gridLayout[onglet][categorie].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), 2*exercice, 7)
                    ## Label Nombre d'exercice
                    self.onglet_exercice_label_parametre[onglet][categorie].append(QtGui.QLabel(self.onglet_exercice_ligne[onglet][categorie][exercice]))
                    self.onglet_exercice_label_parametre[onglet][categorie][exercice].setText(u"<u>Paramètre</u> :" )
                    if len(self.liste_exercice[onglet][1][categorie][1][exercice][1]) == 0:
                        self.onglet_exercice_label_parametre[onglet][categorie][exercice].setVisible(False)
                    self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_label_parametre[onglet][categorie][exercice], 2*exercice+1, 8)
                    ## Pour tous les paramètres
                    for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice].append(QtGui.QSpinBox(self.onglet_exercice_widget[onglet]))
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setStyleSheet("background-color: rgb(255, 255, 255);")
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setKeyboardTracking(False) 
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setToolTip(u"Choisissez %s entre %s et %s." % (self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][0], self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][1], self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][2]))
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setRange(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][1]), int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][2]))
                         self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].setValue(int(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][3]))
                         self.onglet_exercice_gridLayout[onglet][categorie].addWidget(self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre], 2*exercice+1, 9+parametre)
                    ## Ajout d'une colonne redimensionnable en largeur
                    self.onglet_exercice_gridLayout[onglet][categorie].addItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), 2*exercice, 11, 2, 1)
                    ## Mise en couleur pour faire une alternance de ligne claire et fonçée
                    if exercice%2:
                        self.onglet_exercice_ligne[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                        self.onglet_exercice_label_aide[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                        self.onglet_exercice_label_nom[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                        self.onglet_exercice_label_temps[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                        self.onglet_exercice_label_parametre[onglet][categorie][exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    else:
                        self.onglet_exercice_ligne[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                        self.onglet_exercice_label_aide[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                        self.onglet_exercice_label_nom[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                        self.onglet_exercice_label_temps[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                        self.onglet_exercice_label_parametre[onglet][categorie][exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
            ## Ajout d'une ligne redimensionnable en hauteur
            self.onglet_exercice_verticalLayout[onglet].addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))

    ###========================================================================
    ### Fonctions de l'onglet CSV
    ###========================================================================
    ############## Construit l'onglet CSV
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
        self.onglet_csv_label_chemin.setText(u"Chemin du fichier CSV : ")
        self.onglet_csv_horizontalLayout_chemin.addWidget(self.onglet_csv_label_chemin)
        ## LineEdit chemin du fichier csv
        self.onglet_csv_chemin = QtGui.QLineEdit(self.onglet_csv_widget)
        self.onglet_csv_chemin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_csv_chemin.setText(self.config["chemin_csv"])
        self.onglet_csv_horizontalLayout_chemin.addWidget(self.onglet_csv_chemin)
        ## Bouton parcourir du fichier csv
        self.onglet_csv_pushButton_parcourir_csv = QtGui.QPushButton(self.onglet_csv_widget)
        self.onglet_csv_pushButton_parcourir_csv.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.onglet_csv_pushButton_parcourir_csv.setText("Parcourir")
        QtCore.QObject.connect(self.onglet_csv_pushButton_parcourir_csv,QtCore.SIGNAL("clicked()"), self.option_parcourir_chemin_csv)
        self.onglet_csv_horizontalLayout_chemin.addWidget(self.onglet_csv_pushButton_parcourir_csv)
        self.onglet_csv_verticalLayout.addLayout(self.onglet_csv_horizontalLayout_chemin)

    ############## Modifie le chemin vers le fichier csv
    def option_parcourir_chemin_csv(self):
        chemin_csv = unicode(QtGui.QFileDialog().getOpenFileName(self.centralwidget, "Fichier .csv",  unicode(self.onglet_option_chemin_fichier.text()), "Documents csv (*.csv)"))
        if chemin_csv:
            self.onglet_csv_chemin.setText(chemin_csv)

    ###========================================================================
    ### Fonctions de l'onglet Selection
    ###========================================================================
    ############## Construit l'onglet des exercices sélectionnés
    def construction_onglet_selection(self):
        ## Creation d'une zone de scroll
        self.onglet_selection_scroll = QtGui.QScrollArea(self.tabWidget)
        self.onglet_selection_scroll.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.onglet_selection_scroll.setWidgetResizable(True)
        self.tabWidget.addTab(self.onglet_selection_scroll, u"Sélection")
        ## initialisation de l'onglet selection
        self.initialisation_onglet_selection()
        ## Création de la liste d'exercices
        self.liste_exercice_selectionner = []

    ############## Initialise l'onglet des exercices sélectionnés
    def initialisation_onglet_selection(self):
        ## Creation d'un QWidget
        self.onglet_selection_widget = QtGui.QWidget(self.onglet_selection_scroll)
        self.onglet_selection_widget.setStyleSheet("background-color: rgb(251, 251, 210);")
        self.onglet_selection_scroll.setWidget(self.onglet_selection_widget)
        ## Creation d'une grille verticale dans le QWidget
        self.onglet_selection_verticalLayout = QtGui.QVBoxLayout(self.onglet_selection_widget)
        ## Intitulé du categorie
        self.onglet_selection_label_categorie = QtGui.QLabel(self.onglet_selection_widget)
        self.onglet_selection_label_categorie.setText(u"<center><strong>Liste de sélection</strong></center>")
        self.onglet_selection_verticalLayout.addWidget(self.onglet_selection_label_categorie)

    ############## remplit l'onglet des exercices sélectionnés
    def remplissage_onglet_selection(self):
        ## Test de l'existence de la liste de sélection
        if self.liste_exercice_selectionner == []:
            QtGui.QMessageBox.warning(self.centralwidget, "Attention !", u"Veuillez choisir des exercices...", QtGui.QMessageBox.Ok )
            ## On supprime le contenu de l'onglet selection
            delete(self.onglet_selection_widget)
            self.onglet_selection_widget = None
            ## initialisation de l'onglet selection
            self.initialisation_onglet_selection()    
        else:
            ## On supprime le contenu de l'onglet selection
            delete(self.onglet_selection_widget)
            self.onglet_selection_widget = None
            ## initialisation de l'onglet selection
            self.initialisation_onglet_selection()
            ## Creation d'une grille dans le QWidget
            self.onglet_selection_gridLayout = QtGui.QGridLayout()
            self.onglet_selection_gridLayout.setColumnMinimumWidth(7, 100)
            self.onglet_selection_gridLayout.setColumnMinimumWidth(10, 100)
            self.onglet_selection_gridLayout.setColumnMinimumWidth(11, 100)
            self.onglet_selection_verticalLayout.addLayout(self.onglet_selection_gridLayout)
            ## Création de la liste d'exercices
            self.onglet_selection_ligne = []
            self.onglet_selection_bouton_monter = []
            self.onglet_selection_bouton_descendre = []
            self.onglet_selection_spinBox_temps = []
            self.onglet_selection_label_aide = []
            self.onglet_selection_label_nom = []
            self.onglet_selection_label_temps = []
            self.onglet_selection_label_parametre = []
            self.onglet_selection_spinBox_parametre = []
            self.onglet_selection_bouton_supprimer = []
            for exercice in range(len(self.liste_exercice_selectionner)):
                ## Ligne pour la couleur
                self.onglet_selection_ligne.append(QtGui.QWidget(self.onglet_selection_widget))
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_ligne[exercice], 2*exercice, 1, 2, 13)
                ## Bouton Monter
                self.onglet_selection_bouton_monter.append(QtGui.QPushButton(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_bouton_monter[exercice].setIcon(QtGui.QIcon(join(DATADIR,"images","haut.png")))
                self.onglet_selection_bouton_monter[exercice].setToolTip(u"Monter l'exercice dans la liste")
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_bouton_monter[exercice], 2*exercice, 1,2,1)
                QtCore.QObject.connect(self.onglet_selection_bouton_monter[exercice],QtCore.SIGNAL("clicked()"), partial(self.deplacer_exercice,exercice,"haut"))
                if exercice == 0:
                    self.onglet_selection_bouton_monter[exercice].setEnabled(False)
                ## Bouton Descendre
                self.onglet_selection_bouton_descendre.append(QtGui.QPushButton(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_bouton_descendre[exercice].setIcon(QtGui.QIcon(join(DATADIR,"images","bas.png")))
                self.onglet_selection_bouton_descendre[exercice].setToolTip(u"Descendre l'exercice dans la liste")
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_bouton_descendre[exercice], 2*exercice, 2,2,1)
                QtCore.QObject.connect(self.onglet_selection_bouton_descendre[exercice],QtCore.SIGNAL("clicked()"), partial(self.deplacer_exercice,exercice,"bas"))
                if exercice == (len(self.liste_exercice_selectionner)-1):
                    self.onglet_selection_bouton_descendre[exercice].setEnabled(False)
                ## Bouton Supprimer
                self.onglet_selection_bouton_supprimer.append(QtGui.QPushButton(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_bouton_supprimer[exercice].setIcon(QtGui.QIcon(join(DATADIR,"images","supprimer.png")))
                self.onglet_selection_bouton_supprimer[exercice].setToolTip(u"Supprimer l'exercice de la liste")
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_bouton_supprimer[exercice], 2*exercice, 3,2,1)
                QtCore.QObject.connect(self.onglet_selection_bouton_supprimer[exercice],QtCore.SIGNAL("clicked()"), partial(self.supprimer_exercice,exercice))
                ## Ajout d'une colonne redimensionnable en largeur
                self.onglet_selection_gridLayout.addItem(QtGui.QSpacerItem(20, 20), 2*exercice, 4, 2, 1)
                ## Bulle d'aide
                self.onglet_selection_label_aide.append(QtGui.QLabel(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_label_aide[exercice].setText(r'<img src="%s" />' %join(DATADIR, "vignettes" ,"%s" % self.environnement,"%s.jpg" % self.liste_exercice_selectionner[exercice][1]))
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_label_aide[exercice], 2*exercice, 5,2,1)
                ## Ajout d'une colonne redimensionnable en largeur
                self.onglet_selection_gridLayout.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), 2*exercice, 6, 2, 1)
                ## Intitulé de l'exercice
                self.onglet_selection_label_nom.append(QtGui.QLabel(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_label_nom[exercice].setText(u"%s" % self.liste_exercice_selectionner[exercice][2])
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_label_nom[exercice], 2*exercice, 6,1,8)
                ## Label temps de l'exercice
                self.onglet_selection_label_temps.append(QtGui.QLabel(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_label_temps[exercice].setText(u"<u>Temps</u> :" )
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_label_temps[exercice], 2*exercice+1, 7)
                ## Temps de l'exercice
                self.onglet_selection_spinBox_temps.append(QtGui.QSpinBox(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_spinBox_temps[exercice].setToolTip(u"Choisissez le temps par slide entre 5 secondes et 90 secondes.")
                self.onglet_selection_spinBox_temps[exercice].setStyleSheet("background-color: rgb(255, 255, 255);")
                self.onglet_selection_spinBox_temps[exercice].setRange(5,90)
                self.onglet_selection_spinBox_temps[exercice].setValue(self.liste_exercice_selectionner[exercice][0])
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_spinBox_temps[exercice], 2*exercice+1, 8)
                ## Ajout d'une colonne redimensionnable en largeur
                self.onglet_selection_gridLayout.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), 2*exercice+1, 9)
                ## Label Nombre d'exercice
                self.onglet_selection_label_parametre.append(QtGui.QLabel(self.onglet_selection_ligne[exercice]))
                self.onglet_selection_label_parametre[exercice].setText(u"<u>Paramètre</u> :" )
                if len(self.liste_exercice_selectionner[exercice][3]) == 0:
                    self.onglet_selection_label_parametre[exercice].setVisible(False)
                self.onglet_selection_gridLayout.addWidget(self.onglet_selection_label_parametre[exercice], 2*exercice+1, 10)
                ## Initialisation
                self.onglet_selection_spinBox_parametre.append([])
                ## Pour tous les paramètres
                for parametre in range(len(self.liste_exercice_selectionner[exercice][3])):
                    self.onglet_selection_spinBox_parametre[exercice].append(QtGui.QSpinBox(self.onglet_selection_ligne[exercice]))
                    self.onglet_selection_spinBox_parametre[exercice][parametre].setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.onglet_selection_spinBox_parametre[exercice][parametre].setKeyboardTracking(False)
                    self.onglet_selection_spinBox_parametre[exercice][parametre].setToolTip(u"Choisissez %s entre %s et %s." % (self.liste_exercice_selectionner[exercice][3][parametre][0],self.liste_exercice_selectionner[exercice][3][parametre][1],self.liste_exercice_selectionner[exercice][3][parametre][2]))
                    self.onglet_selection_spinBox_parametre[exercice][parametre].setRange(int(self.liste_exercice_selectionner[exercice][3][parametre][1]), int(self.liste_exercice_selectionner[exercice][3][parametre][2])) 
                    self.onglet_selection_spinBox_parametre[exercice][parametre].setValue(int(self.liste_exercice_selectionner[exercice][3][parametre][3]))
                    self.onglet_selection_gridLayout.addWidget(self.onglet_selection_spinBox_parametre[exercice][parametre], 2*exercice+1, 11 + parametre)
                ## Ajout d'une colonne redimensionnable en largeur
                self.onglet_selection_gridLayout.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum), 2*exercice, 13, 2, 1)
                ## Mise en couleur pour faire une alternance de ligne claire et fonçée
                if exercice%2:
                    self.onglet_selection_ligne[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_bouton_monter[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_bouton_descendre[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_bouton_supprimer[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_label_aide[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_label_nom[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_label_temps[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                    self.onglet_selection_label_parametre[exercice].setStyleSheet("background-color: rgb(255, 247, 177);")
                else:
                    self.onglet_selection_ligne[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_bouton_monter[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_bouton_descendre[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_bouton_supprimer[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_label_aide[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_label_nom[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_label_temps[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
                    self.onglet_selection_label_parametre[exercice].setStyleSheet("background-color: rgb(251, 231, 178);")
            ## Ajout d'une ligne redimensionnable en hauteur
            self.onglet_selection_verticalLayout.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
            ## Mise à jour du message de la barre d'état
            self.barre_etat_label.setText(u"%s exercice(s) sélectionné(s). En attente..." %len(self.liste_exercice_selectionner))

    ############## Actualise l'onglet des exercices sélectionnés
    def actualiser_onglet_selection(self):
        ## Actualisation de la liste de sélection
        self.liste_exercice_selectionner = []
        for onglet in range(len(self.liste_exercice)):
            for categorie in range(len(self.liste_exercice[onglet][1])):
                for exercice in range(len(self.liste_exercice[onglet][1][categorie][1])):
                    nombre_exercice = self.onglet_exercice_spinBox_nombre[onglet][categorie][exercice].value()
                    for i in range(nombre_exercice):
                        temps_exercice = self.onglet_exercice_spinBox_temps[onglet][categorie][exercice].value()
                        commande_exercice = self.liste_exercice[onglet][1][categorie][1][exercice][2]
                        label_exercice = self.onglet_exercice_label_nom[onglet][categorie][exercice].text()
                        parametre_exercice = []
                        for parametre in range(len(self.liste_exercice[onglet][1][categorie][1][exercice][1])):
                            temp = []
                            temp.append(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][0])
                            temp.append(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][1])
                            temp.append(self.liste_exercice[onglet][1][categorie][1][exercice][1][parametre][2])
                            temp.append(self.onglet_exercice_spinBox_parametre[onglet][categorie][exercice][parametre].value())
                            parametre_exercice.append(temp)
                        self.liste_exercice_selectionner.append([temps_exercice,commande_exercice,label_exercice,parametre_exercice])
        ## Remplissage de l'onglet selection
        self.remplissage_onglet_selection()

    ############## Deplace l'exercice d'une ligne dans la liste de sélection
    def deplacer_exercice(self, index_exercice, direction):
        ## Sauvegarde des Widgets
        for exercice in range(len(self.liste_exercice_selectionner)):
            self.liste_exercice_selectionner[exercice][0] =  self.onglet_selection_spinBox_temps[exercice].value()
            for parametre in range(len(self.liste_exercice_selectionner[exercice][3])):
                self.liste_exercice_selectionner[exercice][3][parametre][3] = self.onglet_selection_spinBox_parametre[exercice][parametre].value()
        ## Inversion des exercices concerné dans la liste de sélection
        if direction == "haut":
            liste_exercice = [index_exercice-1,index_exercice]
        else:
            liste_exercice = [index_exercice,index_exercice+1]
        self.liste_exercice_selectionner[liste_exercice[0]],self.liste_exercice_selectionner[liste_exercice[1]]= self.liste_exercice_selectionner[liste_exercice[1]],self.liste_exercice_selectionner[liste_exercice[0]]
        ## Remplissage de l'onglet selection
        self.remplissage_onglet_selection()

    ############## Supprime un exercice de la liste de sélection
    def supprimer_exercice(self, index_exercice):
        ## Mise à jour de la liste de sélection
        del self.liste_exercice_selectionner[index_exercice]
        ## Remplissage de l'onglet selection
        self.remplissage_onglet_selection()

    ###========================================================================
    ### Fonctions de l'onglet Option
    ###========================================================================
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
        ## Creation d'une grille verticale dans le QWidget
        self.onglet_option_verticalLayout = QtGui.QVBoxLayout(self.onglet_option_widget)
        ############## Catégorie Système
        ## Intitulé de la categorie
        self.onglet_option_label_categorie_0 = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_categorie_0.setText(u"<center><strong>Système</strong></center>")
        self.onglet_option_verticalLayout.addWidget(self.onglet_option_label_categorie_0)
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_01 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout.addLayout(self.onglet_option_horizontalLayout_01)
        ## Conteneur vertical
        self.onglet_option_verticalLayout_01 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_01.addLayout(self.onglet_option_verticalLayout_01)
        ## Label nom du fichier
        self.onglet_option_label_nom_fichier = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_nom_fichier.setText(u"Nom par défaut du fichier : ")
        self.onglet_option_verticalLayout_01.addWidget(self.onglet_option_label_nom_fichier)
        ## Label chemin_fichier par défaut pour l'enregistrement des fichiers
        self.onglet_option_label_chemin_fichier = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_chemin_fichier.setText(u"Chemin pour enregistrer les fichiers : ")
        self.onglet_option_verticalLayout_01.addWidget(self.onglet_option_label_chemin_fichier)
        ## Label compilateur_externe
        self.onglet_option_label_compilateur_externe = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_compilateur_externe.setText(u"Utiliser le compilateur externe : ")
        self.onglet_option_verticalLayout_01.addWidget(self.onglet_option_label_compilateur_externe)
        ## Label chemin_compilateur_externe
        self.onglet_option_label_chemin_compilateur_externe = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_chemin_compilateur_externe.setText(u"Chemin vers le compilateur externe : ")
        self.onglet_option_verticalLayout_01.addWidget(self.onglet_option_label_chemin_compilateur_externe)
        ## Layout pour les noms d'options, en haut à droite
        self.onglet_option_verticalLayout_02 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_01.addLayout(self.onglet_option_verticalLayout_02)
        ## LineEdit nom du fichier
        self.onglet_option_nom_fichier = QtGui.QLineEdit(self.onglet_option_widget)
        self.onglet_option_nom_fichier.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_option_nom_fichier.setText(self.config["nom_fichier"])
        self.onglet_option_verticalLayout_02.addWidget(self.onglet_option_nom_fichier)
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_02 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout_02.addLayout(self.onglet_option_horizontalLayout_02)
        ## LineEdit chemin par défaut pour l'enregistrement des fichiers
        self.onglet_option_chemin_fichier = QtGui.QLineEdit(self.onglet_option_widget)
        self.onglet_option_chemin_fichier.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_option_chemin_fichier.setText(self.config["chemin_fichier"])
        self.onglet_option_horizontalLayout_02.addWidget(self.onglet_option_chemin_fichier)
        ## Bouton parcourir
        self.onglet_option_pushButton_parcourir_chemin_fichier = QtGui.QPushButton(self.onglet_option_widget)
        self.onglet_option_pushButton_parcourir_chemin_fichier.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.onglet_option_pushButton_parcourir_chemin_fichier.setText("Parcourir")
        QtCore.QObject.connect(self.onglet_option_pushButton_parcourir_chemin_fichier,QtCore.SIGNAL("clicked()"), self.option_parcourir_chemin_fichier)
        self.onglet_option_horizontalLayout_02.addWidget(self.onglet_option_pushButton_parcourir_chemin_fichier)
        ## CheckBox "Compilateur externe"
        self.checkBox_compilateur_externe = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_compilateur_externe.setToolTip(u"Actimaths doit-il utiliser le compilateur externe pour la compilation ?")
        self.checkBox_compilateur_externe.setChecked(int(self.config["compilateur_externe"]))
        QtCore.QObject.connect(self.checkBox_compilateur_externe,QtCore.SIGNAL("stateChanged(int)"), self.option_compilateur_externe)
        self.onglet_option_verticalLayout_02.addWidget(self.checkBox_compilateur_externe)
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_03 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout_02.addLayout(self.onglet_option_horizontalLayout_03)
        ## LineEdit chemin_compilateur_externe par défaut pour la compilation Latex
        self.onglet_option_chemin_compilateur_externe = QtGui.QLineEdit(self.onglet_option_widget)
        self.onglet_option_chemin_compilateur_externe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.onglet_option_chemin_compilateur_externe.setText(self.config["chemin_compilateur_externe"])
        self.onglet_option_horizontalLayout_03.addWidget(self.onglet_option_chemin_compilateur_externe)
        ## Bouton parcourir
        self.onglet_option_pushButton_parcourir_chemin_compilateur_externe = QtGui.QPushButton(self.onglet_option_widget)
        self.onglet_option_pushButton_parcourir_chemin_compilateur_externe.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.onglet_option_pushButton_parcourir_chemin_compilateur_externe.setText("Parcourir")
        QtCore.QObject.connect(self.onglet_option_pushButton_parcourir_chemin_compilateur_externe,QtCore.SIGNAL("clicked()"), self.option_parcourir_chemin_compilateur_externe)
        self.onglet_option_horizontalLayout_03.addWidget(self.onglet_option_pushButton_parcourir_chemin_compilateur_externe)
        ############## Catégorie Information
        ## Intitulé de la categorie
        self.onglet_option_label_categorie_1 = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_categorie_1.setText(u"<center><strong>Informations</strong></center>")
        self.onglet_option_verticalLayout.addWidget(self.onglet_option_label_categorie_1)
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_1 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout.addLayout(self.onglet_option_horizontalLayout_1)
        ## Conteneur vertical
        self.onglet_option_verticalLayout_1 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_1.addLayout(self.onglet_option_verticalLayout_1)
        ## Label titre des fiches
        self.onglet_option_label_titre_fiche = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_titre_fiche.setText("Titre de la fiche d'exercices : ")
        self.onglet_option_verticalLayout_1.addWidget(self.onglet_option_label_titre_fiche)
        ## Label nom de l'établissement
        self.onglet_option_label_nom_etablissement = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_nom_etablissement.setText(u"Nom de l'établissement : ")
        self.onglet_option_verticalLayout_1.addWidget(self.onglet_option_label_nom_etablissement)
        ## Label nom de l'auteur
        self.onglet_option_label_nom_auteur = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_nom_auteur.setText("Nom de l'auteur : ")
        self.onglet_option_verticalLayout_1.addWidget(self.onglet_option_label_nom_auteur)
        ## Label date de l'activité mentale
        self.onglet_option_label_date_activite = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_date_activite.setText(u"Date de l\'activité mentale : ")
        self.onglet_option_verticalLayout_1.addWidget(self.onglet_option_label_date_activite)
        ## Label niveau
        self.onglet_option_label_niveau = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_niveau.setText("Niveau :")
        self.onglet_option_verticalLayout_1.addWidget(self.onglet_option_label_niveau)
        ## Layout pour les noms d'options, en haut à droite
        self.onglet_option_verticalLayout_2 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_1.addLayout(self.onglet_option_verticalLayout_2)
        ## LineEdit titre des fiches
        self.titre_fiche = QtGui.QLineEdit(self.onglet_option_widget)
        self.titre_fiche.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titre_fiche.setText(self.config["titre_fiche"])
        self.onglet_option_verticalLayout_2.addWidget(self.titre_fiche)
        ## LineEdit nom de l'établissement
        self.nom_etablissement = QtGui.QLineEdit(self.onglet_option_widget)
        self.nom_etablissement.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nom_etablissement.setText(self.config["nom_etablissement"])
        self.onglet_option_verticalLayout_2.addWidget(self.nom_etablissement)
        ## LineEdit nom de l'auteur
        self.nom_auteur = QtGui.QLineEdit(self.onglet_option_widget)
        self.nom_auteur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nom_auteur.setText(self.config["nom_auteur"])
        self.onglet_option_verticalLayout_2.addWidget(self.nom_auteur)
        ## ComboBox date de l'activité mentale
        self.date_activite = QtGui.QComboBox(self.onglet_option_widget)
        self.date_activite.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_activite.setEditable(True)
        self.date_activite.addItem(date.today().strftime("%A %d %B %Y").decode("utf-8","replace"))
        self.date_activite.addItem((date.today()+timedelta(days=1)).strftime("%A %d %B %Y").decode("utf-8","replace"))
        self.date_activite.addItem((date.today()+timedelta(days=2)).strftime("%A %d %B %Y").decode("utf-8","replace"))
        self.date_activite.addItem((date.today()+timedelta(days=3)).strftime("%A %d %B %Y").decode("utf-8","replace"))
        self.onglet_option_verticalLayout_2.addWidget(self.date_activite)
        ## ComboBox niveau
        self.comboBox_niveau = QtGui.QComboBox(self.onglet_option_widget)
        self.comboBox_niveau.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_niveau.setEditable(True)
        self.comboBox_niveau.addItem(u"Sixième")
        self.comboBox_niveau.addItem(u"Cinquième")
        self.comboBox_niveau.addItem(u"Quatrième")
        self.comboBox_niveau.addItem(u"Troisième")
        self.onglet_option_verticalLayout_2.addWidget(self.comboBox_niveau)
        ## Ligne de séparation
        self.ligne_separation_1 = QtGui.QFrame(self.onglet_option_widget)
        self.ligne_separation_1.setFrameShape(QtGui.QFrame.HLine)
        self.ligne_separation_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.onglet_option_verticalLayout.addWidget(self.ligne_separation_1)
        ############## Catégorie Modèle et sortie
        ## Intitulé de la categorie
        self.onglet_option_label_categorie_2 = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_categorie_2.setText(u"<center><strong>Modèles et sorties</strong></center>")
        self.onglet_option_verticalLayout.addWidget(self.onglet_option_label_categorie_2)
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_3 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout.addLayout(self.onglet_option_horizontalLayout_3)
        ## Conteneur vertical
        self.onglet_option_verticalLayout_3 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_3.addLayout(self.onglet_option_verticalLayout_3)
        ## CheckBox "présentation sujet ou non"
        self.checkBox_sujet_presentation = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_sujet_presentation.setText(u"Créer le sujet vidéoprojetable")
        self.checkBox_sujet_presentation.setToolTip(u"Actimaths doit-il créer le sujet vidéoprojetable ?")
        self.checkBox_sujet_presentation.setChecked(int(self.config["sujet_presentation"]))
        QtCore.QObject.connect(self.checkBox_sujet_presentation,QtCore.SIGNAL("stateChanged(int)"), self.option_modele_presentation)
        self.onglet_option_verticalLayout_3.addWidget(self.checkBox_sujet_presentation)
        ## CheckBox "page sujet ou non"
        self.checkBox_sujet_page = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_sujet_page.setText(u"Créer le sujet papier")
        self.checkBox_sujet_page.setToolTip(u"Actimaths doit-il créer le sujet papier imprimable ?")
        self.checkBox_sujet_page.setChecked(int(self.config["sujet_page"]))
        QtCore.QObject.connect(self.checkBox_sujet_page,QtCore.SIGNAL("stateChanged(int)"), self.option_modele_page)
        self.onglet_option_verticalLayout_3.addWidget(self.checkBox_sujet_page)
        ## Conteneur vertical
        self.onglet_option_verticalLayout_4 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_3.addLayout(self.onglet_option_verticalLayout_4)
        ## CheckBox "présentation corrigés ou non"
        self.checkBox_corrige_presentation = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_corrige_presentation.setText(u"Créer le corrigé vidéoprojetable")
        self.checkBox_corrige_presentation.setToolTip(u"Actimaths doit-il créer le corrigé vidéoprojetable ?")
        self.checkBox_corrige_presentation.setChecked(int(self.config["corrige_presentation"]))
        QtCore.QObject.connect(self.checkBox_corrige_presentation,QtCore.SIGNAL("stateChanged(int)"), self.option_modele_presentation)
        self.onglet_option_verticalLayout_4.addWidget(self.checkBox_corrige_presentation)
        ## CheckBox "page corrigés ou non"
        self.checkBox_corrige_page = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_corrige_page.setText(u"Créer le corrigé papier")
        self.checkBox_corrige_page.setToolTip(u"Actimaths doit-il créer le corrigé papier imprimable ?")
        self.checkBox_corrige_page.setChecked(int(self.config["corrige_page"]))
        QtCore.QObject.connect(self.checkBox_corrige_page,QtCore.SIGNAL("stateChanged(int)"), self.option_modele_page)
        self.onglet_option_verticalLayout_4.addWidget(self.checkBox_corrige_page)
        ## Espace horizontal
        self.onglet_option_horizontalLayout_3.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        ## Conteneur vertical
        self.onglet_option_verticalLayout_5 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_3.addLayout(self.onglet_option_verticalLayout_5)
        ## Label Modèle de présentation
        self.label_modele_presentation = QtGui.QLabel(self.onglet_option_widget)
        self.label_modele_presentation.setText(u"Modèle vidéoprojetable :")
        self.onglet_option_verticalLayout_5.addWidget(self.label_modele_presentation)
        ## Label Modèle de mise en page
        self.label_modele_page = QtGui.QLabel(self.onglet_option_widget)
        self.label_modele_page.setText(u"Modèle papier :")
        self.onglet_option_verticalLayout_5.addWidget(self.label_modele_page)
        ## Conteneur vertical
        self.onglet_option_verticalLayout_6 = QtGui.QVBoxLayout()
        self.onglet_option_horizontalLayout_3.addLayout(self.onglet_option_verticalLayout_6)
        ## ComboBox modèles de présentation
        self.comboBox_modele_presentation = QtGui.QComboBox(self.onglet_option_widget)
        self.comboBox_modele_presentation.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.option_cherche_modele("presentation")
        self.onglet_option_verticalLayout_6.addWidget(self.comboBox_modele_presentation)
        ## ComboBox modèles de page papier
        self.comboBox_modele_page = QtGui.QComboBox(self.onglet_option_widget)
        self.comboBox_modele_page.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.option_cherche_modele("page")
        self.onglet_option_verticalLayout_6.addWidget(self.comboBox_modele_page)
        ## Ligne de séparation
        self.ligne_separation_2 = QtGui.QFrame(self.onglet_option_widget)
        self.ligne_separation_2.setFrameShape(QtGui.QFrame.HLine)
        self.ligne_separation_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.onglet_option_verticalLayout.addWidget(self.ligne_separation_2)
        ############## Catégorie Paramètre de compilation
        ## Intitulé de la categorie
        self.onglet_option_label_categorie_3 = QtGui.QLabel(self.onglet_option_widget)
        self.onglet_option_label_categorie_3.setText(u"<center><strong>Paramètres de compilation</strong></center>")
        self.onglet_option_verticalLayout.addWidget(self.onglet_option_label_categorie_3)
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_4 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout.addLayout(self.onglet_option_horizontalLayout_4)
        ## CheckBox "Creer les PDF"
        self.checkBox_creer_pdf = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_creer_pdf.setText(u"Créer les PDF")
        self.checkBox_creer_pdf.setToolTip(u"Actimaths doit-il créer les PDF à partir des sources TeX ?")
        self.checkBox_creer_pdf.setChecked(int(self.config["creer_pdf"]))
        QtCore.QObject.connect(self.checkBox_creer_pdf,QtCore.SIGNAL("stateChanged(int)"), self.option_creer_pdf)
        self.onglet_option_horizontalLayout_4.addWidget(self.checkBox_creer_pdf)
        ## CheckBox "Effacer les TeX"
        self.checkBox_effacer_tex = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_effacer_tex.setText(u"Effacer les TeX")
        self.checkBox_effacer_tex.setToolTip(u"Actimaths doit-il supprimer les sources TeX ?")
        self.checkBox_effacer_tex.setChecked(int(self.config["effacer_tex"]))
        self.onglet_option_horizontalLayout_4.addWidget(self.checkBox_effacer_tex)
        ## CheckBox "afficher les PDF ou non"
        self.checkBox_afficher_pdf = QtGui.QCheckBox(self.onglet_option_widget)
        self.checkBox_afficher_pdf.setText(u"Afficher les PDF")
        self.checkBox_afficher_pdf.setToolTip(u"Actimaths doit-il afficher les PDF à la fin de la création ?")
        self.checkBox_afficher_pdf.setChecked(int(self.config["afficher_pdf"]))
        self.onglet_option_horizontalLayout_4.addWidget(self.checkBox_afficher_pdf)
        ## Espace vertical
        self.onglet_option_verticalLayout.addItem(QtGui.QSpacerItem(20, 177, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
        ## Conteneur horizontal
        self.onglet_option_horizontalLayout_5 = QtGui.QHBoxLayout()
        self.onglet_option_verticalLayout.addLayout(self.onglet_option_horizontalLayout_5)
        ## Espace horizontal
        self.onglet_option_horizontalLayout_5.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        ## Bouton enregistrer
        self.pushButton_enr_opt = QtGui.QPushButton(self.onglet_option_widget)
        self.pushButton_enr_opt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0  rgba(255, 127, 0, 255), stop:1 rgba(255, 247, 177, 255));")
        self.pushButton_enr_opt.setText(u"Enregistrer dans les préférences")
        QtCore.QObject.connect(self.pushButton_enr_opt,QtCore.SIGNAL("clicked()"), self.enregistrer_config)
        self.onglet_option_horizontalLayout_5.addWidget(self.pushButton_enr_opt)
        ## Configuration de l'affichage selon le fichier de configuration ou l'environnement
        self.option_environnement()
        self.option_compilateur_externe()
        self.option_modele_presentation()
        self.option_modele_page()
        self.option_creer_pdf()

    ############## Modifie le chemin d'enregistrement des fiches
    def option_parcourir_chemin_fichier(self):
        chemin_fichier = unicode(QtGui.QFileDialog().getExistingDirectory (self.centralwidget, u"Dossier où créer les fiches", unicode(self.onglet_option_chemin_fichier.text()), QtGui.QFileDialog.ShowDirsOnly))
        if chemin_fichier:
            self.onglet_option_chemin_fichier.setText(chemin_fichier)

    ############## Modifie le chemin vers le compilateur externe
    def option_parcourir_chemin_compilateur_externe(self):
        chemin_compilateur_externe = unicode(QtGui.QFileDialog().getExistingDirectory (self.centralwidget, u"Dossier où trouver les exécutables Latex", unicode(self.onglet_option_chemin_compilateur_externe.text()), QtGui.QFileDialog.ShowDirsOnly))
        if chemin_compilateur_externe:
            self.onglet_option_chemin_compilateur_externe.setText(chemin_compilateur_externe)

    ############## Active les modèles de présentation selon l'environnement
    def option_cherche_modele(self,presentation):
        modeles = []
        for fichier in listdir(join(DATADIR,"modeles",self.environnement,presentation)):
            if splitext(fichier)[1] == ".tex":
                modeles.append(str(fichier[:len(fichier) - 4]))
        modeles.sort()
        for i in range(len(modeles)):
            if modeles[i] != "vignette":
                exec("self.comboBox_modele_%s.addItem(str(modeles[i]))" %presentation)
                if modeles[i] == self.config["modele_%s" %presentation]:
                    exec("self.comboBox_modele_%s.setCurrentIndex(i)" %presentation)

    ############## Active les modèles de présentation selon l'environnement
    def option_environnement(self):
        if self.environnement != "actimaths":
            self.checkBox_sujet_presentation.setChecked(False)
            self.checkBox_sujet_presentation.setEnabled(False)
            self.checkBox_corrige_presentation.setChecked(False)
            self.checkBox_corrige_presentation.setEnabled(False)
            self.label_modele_presentation.setEnabled(False)
            self.comboBox_modele_presentation.setEnabled(False)

    ############## Active l'affichage des PDF de l'onglet des options
    def option_compilateur_externe(self):
        if not self.checkBox_compilateur_externe.isChecked():
            self.onglet_option_chemin_compilateur_externe.setEnabled(False)
            self.onglet_option_pushButton_parcourir_chemin_compilateur_externe.setEnabled(False)
            self.onglet_option_label_chemin_compilateur_externe.setEnabled(False)
        else:
            self.onglet_option_chemin_compilateur_externe.setEnabled(True)
            self.onglet_option_pushButton_parcourir_chemin_compilateur_externe.setEnabled(True)
            self.onglet_option_label_chemin_compilateur_externe.setEnabled(True)

    ############## Active le choix du modèle de présentation de l'onglet des options
    def option_modele_presentation(self):
        if not self.checkBox_sujet_presentation.isChecked() and not self.checkBox_corrige_presentation.isChecked():
            self.label_modele_presentation.setEnabled(False)
            self.comboBox_modele_presentation.setEnabled(False)
        else:
            self.label_modele_presentation.setEnabled(True)
            self.comboBox_modele_presentation.setEnabled(True)

    ############## Active le choix du modèle de page de l'onglet des options
    def option_modele_page(self):
        if not self.checkBox_sujet_page.isChecked() and not self.checkBox_corrige_page.isChecked():
            self.label_modele_page.setEnabled(False)
            self.comboBox_modele_page.setEnabled(False)
        else:
            self.label_modele_page.setEnabled(True)
            self.comboBox_modele_page.setEnabled(True)

    ############## Active l'affichage des PDF de l'onglet des options
    def option_creer_pdf(self):
        if not self.checkBox_creer_pdf.isChecked():
            self.checkBox_effacer_tex.setChecked(False)
            self.checkBox_effacer_tex.setEnabled(False)
            self.checkBox_afficher_pdf.setChecked(False)
            self.checkBox_afficher_pdf.setEnabled(False)
        else:
            self.checkBox_effacer_tex.setEnabled(True)
            self.checkBox_afficher_pdf.setEnabled(True)

    ###========================================================================
    ### Fonctions de gestion du fichier de configuration
    ###========================================================================
    ############## Fonction qui se charge d'enregistrer les options de l'interface dans le fichier de configuration après avoir complété le dictionnaire.
    def enregistrer_config(self):
        tree = etree.parse(self.fichier_configuration)
        root = tree.getroot()
        options = root.find("options")
        options .find("nom_fichier").text = unicode(self.onglet_option_nom_fichier.text())
        options .find("chemin_fichier").text = unicode(self.onglet_option_chemin_fichier.text())
        options .find("compilateur_externe").text = str(self.checkBox_compilateur_externe.isChecked())
        options .find("chemin_compilateur_externe").text = unicode(self.onglet_option_chemin_compilateur_externe.text())
        options .find("titre_fiche").text = unicode(self.titre_fiche.text())
        options .find("nom_etablissement").text = unicode(self.nom_etablissement.text())
        options .find("nom_auteur").text = unicode(self.nom_auteur.text())
        options .find("sujet_presentation").text  = str(self.checkBox_sujet_presentation.isChecked())
        options .find("corrige_presentation").text = str(self.checkBox_corrige_presentation.isChecked())
        options .find("sujet_page").text  = str(self.checkBox_sujet_page.isChecked())
        options .find("corrige_page").text = str(self.checkBox_corrige_page.isChecked())
        options .find("creer_pdf").text = str(self.checkBox_creer_pdf.isChecked())
        options .find("effacer_tex").text = str(self.checkBox_effacer_tex.isChecked())
        options .find("afficher_pdf").text = str(self.checkBox_afficher_pdf.isChecked())
        options .find("modele_presentation").text = unicode(self.comboBox_modele_presentation.currentText())
        options .find("modele_page").text = unicode(self.comboBox_modele_page.currentText())
        options .find("environnement").text = self.environnement
        options .find("affichage").text = self.affichage
        f = open(self.fichier_configuration, encoding="utf-8", mode="w")
        f.write(etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True).decode("utf-8", "strict"))
        f.close()

    ###========================================================================
    ### Fonction de création des exercices
    ###========================================================================
    ############## Crée les fiches à partir de la liste d'exercices
    def creer_exercices(self):
        ## synchronisation des paramètres
        self.parametres = {"sujet_presentation": self.checkBox_sujet_presentation.isChecked(),
                           "corrige_presentation": self.checkBox_corrige_presentation.isChecked(),
                           "sujet_page": self.checkBox_sujet_page.isChecked(),
                           "corrige_page": self.checkBox_corrige_page.isChecked(),
                           "titre": unicode(self.titre_fiche.text()),
                           "nom_etablissement": unicode(self.nom_etablissement.text()),
                           "nom_auteur": unicode(self.nom_auteur.text()),
                           "date_activite": unicode(self.date_activite.currentText()),
                           "niveau": unicode(self.comboBox_niveau.currentText()),
                           "nom_fichier": unicode(self.onglet_option_nom_fichier.text()),
                           "chemin_fichier": unicode(self.onglet_option_chemin_fichier.text()),
                           "compilateur_externe" : self.checkBox_compilateur_externe.isChecked(),
                           "chemin_compilateur_externe": unicode(self.onglet_option_chemin_compilateur_externe.text()),
                           "environnement": self.environnement,
                           "affichage": self.affichage,
                           "modele_presentation": unicode(self.comboBox_modele_presentation.currentText()),
                           "modele_page": unicode(self.comboBox_modele_page.currentText()),
                           "creer_pdf" : self.checkBox_creer_pdf.isChecked(),
                           "effacer_tex" : self.checkBox_effacer_tex.isChecked(),
                           "afficher_pdf" : self.checkBox_afficher_pdf.isChecked()}
        ## Creation
        if self.affichage == "csv":
            # Test de l'existence du fichier
            if not(isfile(unicode(self.onglet_csv_chemin.text()))):
                QtGui.QMessageBox.warning(self.centralwidget, "Attention !", u"Fichier csv non valide.", QtGui.QMessageBox.Ok ) 
            else:
                self.parametres ["liste_exercice"] = []
                self.parametres ["chemin_csv"] = unicode(self.onglet_csv_chemin.text())
                self.creer()
        else:
            # Création de la liste d'exercices
            self.parametres ["liste_exercice"] = []
            for exercice in range(len(self.liste_exercice_selectionner)):
                temps_exercice =  self.onglet_selection_spinBox_temps[exercice].value()
                commande_exercice = self.liste_exercice_selectionner[exercice][1]
                parametre_exercice = []
                for parametre in range(len(self.liste_exercice_selectionner[exercice][3])):
                    parametre_exercice.append(self.onglet_selection_spinBox_parametre[exercice][parametre].value())
                self.parametres ["liste_exercice"].append((temps_exercice, commande_exercice, parametre_exercice))
            # Test de l'existence de la liste
            if self.parametres ["liste_exercice"] == []:
                QtGui.QMessageBox.warning(self.centralwidget, "Attention !", u"Veuillez sélectionner des exercices...", QtGui.QMessageBox.Ok )    
            else:
                self.parametres ["chemin_csv"] = ""
                self.creer()

    ############## Fonction qui lance le Thread de création
    def creer(self):
        ## Le bouton creer devient annuler
        self.bouton_creer.setText(u"Annuler")
        self.bouton_creer.setToolTip(u"Annuler la création d'exercice en cours")
        self.bouton_creer.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(238, 44, 44, 255), stop:1 rgba(255, 247, 177, 255));")
        QtCore.QObject.disconnect(self.bouton_creer,QtCore.SIGNAL("clicked()"), self.creer_exercices)
        QtCore.QObject.connect(self.bouton_creer, QtCore.SIGNAL("clicked()"), self.annuler_tache)
        ## progressBar oscillante
        self.barre_etat_progressBar.setVisible(True)
        ## Mise à jour du message de la barre d'état
        self.barre_etat_label.setText(u"Création des exercices en cours. Veuillez patienter...")
        ## On créé et on lance le thread de creation
        self.myLongTask = TaskThread(self.parametres)
        self.myLongTask.tacheTerminee.connect(self.tache_terminee)
        self.myLongTask.tacheAnnulee.connect(self.tache_annulee)
        self.myLongTask.start()

    ############## Fonction qui stoppe le Thread de création
    def annuler_tache(self):
        ## Arrêt du Thread
        self.myLongTask.stop()

###========================================================================
### Class QThread
###========================================================================
class TaskThread(QtCore.QThread):
    tacheTerminee = QtCore.pyqtSignal()
    tacheAnnulee = QtCore.pyqtSignal()
    ## Créateur de la classe TaskThread
    def __init__(self, parametres,  parent=None):
        self.parametres = parametres
        QtCore.QThread.__init__(self, parent)
    ## Lanceur de TaskThread
    def run(self):
        creation(self.parametres)
        self.tacheTerminee.emit()
    ## Destructeur de TaskThread
    def stop(self):
        self.terminate()
        self.tacheAnnulee.emit()
