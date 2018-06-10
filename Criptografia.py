# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:30:50 2018

@author: aas8
"""

import Elementos as el

def recuperar_chaves(arq):
    arquivo = open (arq, 'r')
    linha = arquivo.readline()
    arquivo.close()
    aux = ''
    for char in linha:
        if char != ' ':
            aux += char
        else:
            num1 = int(aux)
            aux = ''
    num2 = int(aux)
    return num1, num2

def criptografar_string(string, e, n):
    codigo = ''
    for x in string:
        y = (ord(x)**e)%n
        codigo += str(y)+'!'
    return codigo

def decifrar_codigo(string, d, n):
    texto = ''
    aux = ''
    for char in string:
        if char != '!' and char != '\n':
            aux += char
        elif char != '\n':
            y = int(aux)
            aux = ''
            x = chr((y**d)%n)
            texto += x
    return texto

def criptografar_usuarios(dicionario, arquivo):
    arq = open(arquivo, 'w')
    e, n = recuperar_chaves("chavePublica.txt")
    for chave in dicionario:
        arq.write(criptografar_string(chave, e, n))
        arq.write('+')
        arq.write(criptografar_string(dicionario[chave][0], e, n))
        arq.write('+')
        arq.write(criptografar_string(dicionario[chave][1], e, n))
        arq.write('+')
        arq.write(str(dicionario[chave][2]))
        arq.write('\n')
    arq.flush()
    arq.close()

def decifrar_usuarios(arquivo, dicionario):
    arq = open(arquivo, 'r')
    linha = arq.readline()
    d,n = recuperar_chaves("chavePrivada.txt")
    while linha != '':
            string = ''
            cont = 0
            for char in linha:
                if char != '+':
                    string += char
                else:
                    if cont == 0:
                        chave = decifrar_codigo(string, d, n)
                        string = ''
                        cont += 1
                    elif cont == 1:
                        nome = decifrar_codigo(string, d, n)
                        string = ''
                        cont += 1
                    elif cont == 2:
                        senha = decifrar_codigo(string, d, n)
                        string = ''
            acesso = int(string)
            dicionario[chave] = (nome, senha, acesso)
            linha = arq.readline()

def criptografar_elementos(dicionario,arquivo):
    arq = open(arquivo, 'w')
    e, n = recuperar_chaves("ChavePublica.txt")
    for chave in dicionario:
        arq.write(criptografar_string(chave, e, n))
        arq.write('+')            
        arq.write(criptografar_string(dicionario[chave][0],e, n))
        arq.write('+')
        arq.write(criptografar_string(dicionario[chave][1], e, n))
        arq.write('+')
        arq.write(criptografar_string(str(dicionario[chave][2]), e, n))
        arq.write('+')
        arq.write(str(dicionario[chave][3]))
        arq.write('\n')
    arq.flush()
    arq.close()
        
def decifrar_elementos(arq,dicionario):
    arquivo = open(arq, 'r')
    linha = arquivo.readline()
    d, n = recuperar_chaves("chavePrivada.txt")
    while linha != '':
        string = ''
        cont = 0
        for char in linha:
            if char != '+':
                string += char
            else:
                if cont == 0:
                    numero = decifrar_codigo(string, d, n)
                    string = ''
                    cont += 1
                elif cont == 1:
                    nome = decifrar_codigo(string, d, n)
                    string = ''
                    cont += 1
                elif cont == 2:
                    marca = decifrar_codigo(string, d, n)
                    string = ''
                    cont += 1
                elif cont == 3:
                    data = decifrar_codigo(string, d, n)
                    string = ''
        quantidade = int(string)
        el.adicionar_elemento(dicionario, numero, nome, marca, quantidade, *converte_data(data))
        linha = arquivo.readline()

def converte_data(string):
    aux = ''
    cont = 0
    for c in string:
        if c != '-':
            aux += c 
        else:
            if cont == 0:
                ano = int(aux)
            elif cont == 1:
                mes = int(aux)
            aux = ''
            cont += 1
    dia = int(aux)
    return dia, mes, ano