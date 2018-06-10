# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:23:35 2018

@author: aas8
"""

import datetime

def log(usuario, acao):
    arquivo = open('log.txt', 'a')
    agora = str(datetime.datetime.now().date())
    arquivo.write('{}: {} na data {};\n'.format(usuario, acao, agora))
     
def compara_data(data):
    arquivo = open('log.txt', 'r')
    linha = arquivo.readline()
    lista = []
    while linha != '':
        if recupera_data(linha) == data:
            lista.append(linha)
        linha = arquivo.readline()
    return lista

def compara_usuario(usuario):
    arquivo = open('log.txt', 'r')
    linha = arquivo.readline()
    lista = []
    while linha != '':
        if recupera_login(linha) == usuario:
            lista.append(linha)
        linha = arquivo.readline()
    return lista

def recupera_data(string):
    lista = string.split(' ')
    data = lista.pop()
    return data[0:-1]

def recupera_login (string):
    lista = string.split(' ')
    data = lista.pop(0)
    return data[0:-1]