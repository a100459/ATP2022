import csv

import matplotlib.pyplot as plt

def lerObras():
    file = open("obras.csv",encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=";")

    lista = []
    for linha in csv_file:
        lista.append(tuple(linha))

    file.close()
    return lista

def contarObras():
    total = len(lerObras())
    return total 

def imprimeObras(obras):
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        print(f"|{nome[:10]:^20} | {desc[:25]:^30} | {comp[:20]:^25} | {ano:^10} ") 
    return


def ordenaTitulo(obras) :
    lista = []
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        lista.append((nome,ano))
    lista.sort(key = lambda x: x[0])
    return lista

def ordenaAno(obras):
    lista = []
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        lista.append((nome,ano))
    lista.sort(key = lambda x: x[1])
    return lista

def ordenaComp(obras):
    lista = []
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        if comp not in lista:
            lista.append(comp)
    lista.sort
    return lista
    
def distribPeriodo(obras):
    distrib = {}
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        if periodo in distrib.keys() :
            distrib[periodo] += 1
        else:
            distrib[periodo] = 1
    return distrib

def distribAno(obras):
    distrib = {}
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        if periodo in distrib.keys() :
            distrib[ano] += 1
        else:
            distrib[ano] = 1
    return distrib

def distribComp(obras):
    distrib = {}
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        if periodo in distrib.keys() :
            distrib[comp] += 1
        else:
            distrib[comp] = 1
    return distrib

def grafs(distrib):
    fig1 = plt.figure(figsize= (30,15))
    plt.bar(distrib.keys(),distrib.values(),color = "blue", width= 0.7)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.show()
    return
            
def inversaoestrutural(obras):
    res= []
    listaComp= []
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        if comp not in listaComp:
            listaComp.append(comp)
    for compositor in listaComp:
        listaObras= []
        for obra in obras:
            nome, desc, ano, periodo, comp, duracao, id = obra
            if  comp == compositor:
                listaObras.append(nome)
        res.append((compositor, listaObras))
    return res

def lerProb(lista):
    for tuplo in lista:
        autor, obras = tuplo
        i = 1
        branco = ""
        print(f"\n{autor:<30}|{obras[0]:<20}")
        while i != len(obras):
            print(f"{branco:<30}|{obras[i]:<20}")
            i += 1
    return



function=int(input("O que pretende fazer?"))
print('''Menu:
(1) Número de obras
(2) Lista de obras
(3) Listas ordenadas
(4) Distribuições
(5) Gráficos
(6) Problema da inversão estrutural
(0) Sair''')

import aula6

while function != 0:
    if function == 1:
        print("\nO número de obras é: "+str(aula6.contarObras(aula6.lerObras())))
    if function ==2:
        print("\nA lista de obras é:")
        aula6.imprimeObras(aula6.lerObras())
    if function ==3:
        print('''\nSub-menu:
        (1) Lista ordenada por título
        (2) Lista ordenada por ano
        (3) Lista ordenada de compositores
        (0) Sair''')
        subfunction=int(input("Que lista pretende ver?"))
        while subfunction != 0:
            if subfunction ==1:
                print("\nLista ordenada por título:")
                print(aula6.ordenaTitulo(aula6.lerObras()))
            if subfunction ==2:
                print("\nLista ordenada por ano:")
                print(aula6.ordenaAno(aula6.lerObras()))
            if subfunction ==3:
                print("\nLista ordenada de compositores:")
                print(aula6.ordenaComp(aula6.lerObras()))
            subfunction=int(input("Que lista pretende ver agora?"))
    if function == 4:
        print('''\nSub-menu:
        (1) Distribuição por período
        (2) Distribuição por ano
        (3) Distribuição por compositor
        (0) Sair''')
        subfunction=int(input("Que distribuição pretende ver?"))
        while subfunction != 0:
            if subfunction ==1:
                print("\nDistribuição por período:")
                print(aula6.distribPeriodo(aula6.lerObras()))
            if subfunction ==2:
                print("\nDistribuição por ano:")
                print(aula6.distribAno(aula6.lerObras()))
            if subfunction ==3:
                print("\nDistribuição por compositor:")
                print(aula6.distribComp(aula6.lerObras()))
            subfunction=int(input("Que distribuição pretende ver agora?"))
    if function == 5:
        subfunction=int(input("Que gráfico pretende ver?"))
        print('''\nSub-menu:
        (1) Gráfico por período
        (2) Gráfico por ano
        (3) Gráfico por compositor
        (0) Sair''')
        while subfunction != 0:
            if subfunction ==1:
                aula6.grafs(aula6.distribPeriodo(aula6.lerObras()))
            if subfunction ==2:
                aula6.grafs(aula6.distribAno(aula6.lerObras()))
            if subfunction ==3:
                aula6.grafs(aula6.distribComp(aula6.lerObras()))
            subfunction=int(input("Que gráfico pretende ver agora?"))
    if function == 6:
        print("\nTabela de obras por autor:")
        aula6.lerProb(aula6.inversaoestrutural(aula6.lerObras()))

    function=int(input("O que pretende fazer agora?"))
