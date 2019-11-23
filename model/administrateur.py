#!/usr/bin/python
#-*- coding: utf-8 -*-

from utilisateur import utilisateur

class administrateur(utilisateur):
	
	def __init__(self, _id, nom, prenom, sexe, date_naissance):
		super().__init__(_id, nom, prenom, sexe, date_naissance)
		

	def creerUtilisateur(self, ):
		pass

	def modifierUtilisateur(self, ):
		pass

	def supprimerUtilisateur(self, ):
		pass

