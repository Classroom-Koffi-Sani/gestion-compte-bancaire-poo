#!/usr/bin/python
#-*- coding: utf-8 -*-

from utilisateur import utilisateur

class gestionnaire(utilisateur):
	
	def __init__(self, _id, nom, prenom, sexe, date_naissance):
		super().__init__(_id, nom, prenom, sexe, date_naissance)
		
		self.compteCree = list()

		self.operations = list()
	