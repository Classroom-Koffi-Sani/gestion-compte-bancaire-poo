#!/usr/bin/python
#-*- coding: utf-8 -*-

from datetime import datetime

class Compte:
	def __init__(self, id_, num_compte, solde, type_, intitule, createur, proprietaire):
		self.id_ = id_
		self.num_compte = num_compte
		self.created_at = datetime.now()
		self.modified_at = datetime.now()
		self.solde = solde
		self.type = type_
		self.intitule = intitule
		
		self.createur = createur
		createur.compteCree.append(self)

		self.proprietaire = proprietaire
		proprietaire.comptes.append[self]

		self.operations = list()


	def afficher(self):
		self.__str__()
	
	
	def __str__(self):
		print(f"Compte[id={self.id_}, \
			num_compte={self.num_compte}, \
			solde={self.solde}, type_={self.type_}, \
			intitule={self.intitule}, \
			createur={self.createur}, \
			proprietaire={self.proprietaire}]"
		)
