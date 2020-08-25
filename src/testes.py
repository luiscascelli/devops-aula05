# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:17:23 2020

DevOps

AC 1

testes.py

@author: Luis Antonio Matile Cascelli

"""

import jogovelha
import sys

erroInicializar = False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
    erroInicializar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar = True
    else:
        for elemento in linha:
            if elemento != '.':
                erroInicializar = True
                
if erroInicializar:
    sys.exit(1)
else:
    sys.exit(0)
