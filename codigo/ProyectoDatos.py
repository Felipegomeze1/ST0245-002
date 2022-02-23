#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:08:49 2022

@author: felipegomez
"""

archivo = open('calles_de_medellin_con_acoso.csv', "r")
lineas = archivo.readlines()
elementos = []
for linea in lineas:
    elementos.append(linea.split(";"))
    



