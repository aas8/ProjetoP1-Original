# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:31:28 2018

@author: aas8
"""
import Usuarios as us
import Criptografia as cp
import Elementos as el
import datetime
import Log

dic_usuarios = {}
#dic_usuarios [login] = (nome,senha, acesso)
dic_usuarios['adm'] = ("Administrador", "adm", 3)
cp.decifrar_usuarios('usuarios.txt', dic_usuarios)

dic_elementos = {}
#dic_elementos [n. de lote] = (nome, marca, data de validade, quantidade)

acesso = 0
while acesso < 1 :
    opt = int(input("login[1], cadastro[2], sair[3]: "))
    if opt == 1:
        usr = input("Digite seu login: ")
        psw = input("Digite sua senha: ")
        acesso, usuario = us.login(dic_usuarios, usr, psw)
        if acesso == 0:
            print('FALHA NO LOGIN')
        else:
            print('Login efetuado como ', dic_usuarios[usuario][0])
            Log.log(usuario, 'login')
            break
    elif opt == 2:
        usr = input("Digite seu login: ")
        psw = input("Digite sua senha: ")
        nome = input("Digite seu nome: ")
        msg = us.cadastrar(usr, psw, nome, dic_usuarios)
        print(msg)
    elif opt == 3:
            cp.criptografar_usuarios(dic_usuarios, 'usuarios.txt')
            break

while acesso > 0:
    cp.decifrar_elementos('elementos.txt', dic_elementos)
    print("{}: nível de acesso {}".format(usuario, acesso))
    print ("[1] Pesquisar produto")
    print ("[2] Visualizar produtos")
    if acesso > 1:
        print ("[3] Adicionar produto")
        print ("[4] Editar quantidade de produto")
    if acesso > 2:    
        print ("[5] Excluir produto")
        print ("[6] Visualizar usuários")
        print ("[7] Editar usuário")
        print ("[8] Excluir usuário")
    print ("[0] Sair")
    opt = 1
    while opt > 0:
        opt = int(input("Digite uma opção: "))
        if opt == 1:
            numero = input("Digite o número do lote: ")
            nome = input("Digite o nome do produto: ")
            marca = input("Digite a marca: ")
            data = input("Data (mm/aa): ")        
            el.pesquisar_elemento(dic_elementos, numero, nome, marca, data[2:], data[5:])
            Log.log(usuario, 'pesquisa')
        elif opt == 2:
            index = int(input("Nome(0), Marca(1), Validade (2), Quantidade (3)\nOrdenar por: "))
            if index <= 3 and index >=0:
                pesquisa = el.visualizar_elementos(dic_elementos, index)
                print(pesquisa)
                for numero in pesquisa:
                    print(dic_elementos[numero])
            else:
                print("Opção inválida, tente novamente.")
        elif opt == 3 and acesso > 1:
            numero = input("Digite o número do lote: ")
            nome = input("Digite o nome do produto: ")
            marca = input("Digite a marca: ")
            data = input("Data (dd/mm/aaaa): ")
            qtd = input("Quantidade: ")
            el.adicionar_elemento(dic_elementos, numero, nome, marca, qtd, int(data[0:2]), int(data[3:5]), int(data[6:10]))
        elif opt == 4 and acesso > 1:
            numero = input("Digite o número do lote: ")
            if numero in dic_elementos:
                qtd = input("Quantidade: ")
                print(el.atualizar_elemento(dic_elementos, numero, qtd))
            else:
                print("Lote não encontrado")
        elif opt == 5 and acesso > 2:
            numero = input("Digite o número do lote: ")
            print(el.excluir_elemento(dic_elementos, numero))
        elif opt == 6 and acesso > 2:
            lista = us.visualizar_usuarios(dic_usuarios)
            for login in lista:
                print('{}: {} ({})'.format(login, dic_usuarios[login][0], dic_usuarios[login][2]))
        elif opt == 7 and acesso> 2:
            login = input("Login: ")
            print("[1] Editar nome")
            print("[2] Alterar senha")
            print("[3] Alterar nível de acesso")
            opt2 = int(input("Escolha uma opção: "))
            if opt2 == 1:
                nome = input("Nome: ")
            elif opt2 == 2:    
                senha = input("Senha: ")
            elif opt2 == 3:    
                acesso = int(input("Nível de acesso: "))
            else:
                print("Opção inválida!")
            us.editar(dic_usuarios, login, nome, senha, acesso)
            print("Alterações realizadas com sucesso!")
            agora = datetime.datetime.now()
        elif opt == 8 and acesso > 2:
            login = input("Login: ")
            print(us.excluir(dic_usuarios, login))
        elif opt == 0:
            Log.log(usuario, 'logout')
            cp.criptografar_usuarios(dic_usuarios, 'usuarios.txt')
            cp.criptografar_elementos(dic_elementos, 'elementos.txt')
            acesso = 0
            break
        else:
            print("Opção inválida!")            
                