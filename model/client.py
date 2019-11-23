#!/usr/bin/python
#-*- coding: utf-8 -*-

from utilisateur import Utilisateur

class Client(Utilisateur):
	
	def __init__(self, _id, nom, prenom, sexe, date_naissance, adresse, photo, telephone, email):
		super().__init__(_id, nom, prenom, sexe, date_naissance)
		self.adresse = adresse
		self.photo = photo
		self.telephone = telephone
		self.email = email
		
		self.comptes = list()

	
	def listerComptes(self, ):
		pass

	
	def afficher(self):
		self.__str__()
	
	
	def __str__(self):
		print(f"Client[id={self.id_}, nom={self.nom}, prenom={self.prenom}, sexe={self.sexe}, date_naissance={self.date_naissance}]")
