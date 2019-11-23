#!/usr/bin/python
#-*- coding: utf-8 -*-

class Utilisateur:
	
	def __init__(self, _id, nom, prenom, sexe, date_naissance):
		self._id = _id
		self.nom = nom
		self.prenom = prenom
		self.sexe = sexe
		self.date_naissance = date_naissance


	def afficher(self):
		self.__str__()
	
	
	def __str__(self):
		print(f"Utilisateur[id={self.id_}, nom={self.nom}, prenom={self.prenom}, sexe={self.sexe}, date_naissance={self.date_naissance}]")
