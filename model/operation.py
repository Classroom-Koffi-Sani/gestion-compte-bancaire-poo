#!/usr/bin/python
#-*- coding: utf-8 -*-

class Operation:
	def __init__(self, id_operation, type_operation, date_operation):
		self.id_operation = id_operation
		self.type_operation = type_operation
		self.date_operation = date_operation

		self.compte = compte
		compte.operations.append(self)

		self.gestionnaire = gestionnaire
		gestionnaire.operations.append(self)

	
	def afficher(self, ):
		pass

	def __str__(self):
		print(f"Operation[id_operation={self.id_operation}, type_operation={self.type_operation}, date_operation={self.date_operation}, sexe={self.sexe}]")